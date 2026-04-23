<!-- markdownlint-disable -->

<h1 align="center">
    Popular Open Source Libraries for Power System Analysis
    <br>
</h1>

<p align="center">
    <strong>🏆  A ranked list of popular projects for Power System Analysis. Updated weekly.</strong>
</p>

<p align="center">
    <a href="https://best-of.org" title="Best-of Badge"><img src="http://bit.ly/3o3EHNN"></a>
    <a href="https://doi.org/10.5281/zenodo.14941137"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.14941137.svg" alt="DOI"></a>
    <a href="#Contents" title="Project Count"><img src="https://img.shields.io/badge/projects-170-blue.svg?color=5ac4bf"></a>
    <a href="#Contribution" title="Contributions are welcome"><img src="https://img.shields.io/badge/contributions-welcome-green.svg"></a>
    <img alt="GitHub Created At" src="https://img.shields.io/github/created-at/ps-wiki/best-of-ps">
    <a href="https://github.com/ps-wiki/best-of-ps/releases" title="Best-of Updates"><img src="https://img.shields.io/github/release-date/ps-wiki/best-of-ps?color=green&label=updated"></a>
    <a href="https://www.repostatus.org/#active"><img src="https://www.repostatus.org/badges/latest/active.svg" alt="Project Status: Active – The project has reached a stable, usable state and is being actively developed." /></a>
    <img alt="GitHub License" src="https://img.shields.io/github/license/ps-wiki/best-of-ps">
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/ps-wiki/best-of-ps">
    <a href="https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fps-wiki%2Fbest-of-ps"><img src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fps-wiki%2Fbest-of-ps&labelColor=%23697689&countColor=%23dce775&style=plastic&labelStyle=lower" /></a>
</p>

This curated list contains 170 open-source projects with a total of 82K stars grouped into 16 categories. All projects are ranked by a project-popularity score, which is calculated based on various metrics automatically collected from GitHub and different package managers. If you like to add or update projects, feel free to open an [issue](https://github.com/ps-wiki/best-of-ps/issues/new/choose), submit a [pull request](https://github.com/ps-wiki/best-of-ps/pulls), or directly edit the [projects.yaml](https://github.com/ps-wiki/best-of-ps/edit/main/projects.yaml). Contributions are very welcome!

## Contents

- [Phasor Simulation](#phasor-simulation) _16 projects_
- [EMT Simulation](#emt-simulation) _2 projects_
- [Steady State Simulation](#steady-state-simulation) _49 projects_
- [Interface](#interface) _24 projects_
- [Gas Simulation](#gas-simulation) _3 projects_
- [Co-Simulation Environment](#co-simulation-environment) _2 projects_
- [Optimization Modeling Language (primarily for optimization modeling)](#optimization-modeling-language-primarily-for-optimization-modeling) _6 projects_
- [Optimizer (capable of solving)](#optimizer-capable-of-solving) _19 projects_
- [Machine/Reinforcement Learning for Power Grid](#machinereinforcement-learning-for-power-grid) _4 projects_
- [Visualization](#visualization) _3 projects_
- [Messaging Environment](#messaging-environment) _2 projects_
- [Power System Data](#power-system-data) _21 projects_
- [Power Electronics](#power-electronics) _0 projects_
- [Database Management](#database-management) _2 projects_
- [Textbook](#textbook) _11 projects_
- [Large Language Model](#large-language-model) _5 projects_

## Explanation
- 🥇🥈🥉&nbsp; Combined project-quality score
- ⭐️&nbsp; Star count from GitHub
- 🐣&nbsp; New project _(less than 6 months old)_
- 💤&nbsp; Inactive project _(12 months no activity)_
- 🧊&nbsp; Long-inactive project _(24 months no visible activity)_
- 📈📉&nbsp; Project is trending up or down
- ➕&nbsp; Project was recently added
- ❗️&nbsp; Warning _(e.g. missing/risky license)_
- 👨‍💻&nbsp; Contributors count from GitHub
- 🔀&nbsp; Fork count from GitHub
- 📋&nbsp; Issue count from GitHub
- ⏱️&nbsp; Last update timestamp on package manager
- 📥&nbsp; Download count from package manager
- 📦&nbsp; Number of dependent projects
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13">&nbsp; Support Python
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13">&nbsp; Support Julia
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13">&nbsp; Support Octave
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13">&nbsp; Support Java
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13">&nbsp; Support C
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13">&nbsp; Support C++
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/modelica.ico" style="display:inline;" width="13" height="13">&nbsp; Support Modelica
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/rust.ico" style="display:inline;" width="13" height="13">&nbsp; Support Rust
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/r.ico" style="display:inline;" width="13" height="13">&nbsp; Support R
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13">&nbsp; Shipped with Jupyter Notebook examples
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13">&nbsp; Public GitHub Actions automation for validation, build, docs, release, publish, or deploy workflows
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13">&nbsp; Available on PyPI
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13">&nbsp; Available on Conda
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13">&nbsp; Developed mainly at a university
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13">&nbsp; Developed mainly at a national laboratory
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13">&nbsp; Developed mainly at a non-profit organization that is neither a university nor a national lab
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13">&nbsp; Developed mainly by volunteers
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13">&nbsp; Developed mainly at a for-profit organization

<br>

## Phasor Simulation

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://ltb.curent.org/">LTB ANDES</a></b> (🥇25 ·  ⭐ 350) - Transient Stability Simulator; CURENT LTB. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CURENT/andes) (👨‍💻 27 · 🔀 150 · 📦 29 · 📋 84 - 14% open · ⏱️ 11.03.2026):

	```
	git clone https://github.com/CURENT/andes
	```
- [PyPi](https://pypi.org/project/andes) (📥 4.2K / month · 📦 4 · ⏱️ 12.03.2026):
	```
	pip install andes
	```
- [Conda](https://anaconda.org/conda-forge/andes) (📥 750K · ⏱️ 27.03.2026):
	```
	conda install -c conda-forge andes
	```
- [Docker Hub](https://hub.docker.com/r/CURENT/andes):
	```
	docker pull CURENT/andes
	```
</details>
<details><summary><b><a href="http://dynawo.org">Dynaωo</a></b> (🥇22 ·  ⭐ 100) - C++/Modelica simulation tools for power systems. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/modelica.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dynawo/dynawo) (👨‍💻 62 · 🔀 31 · 📥 20K · 📋 1.7K - 11% open · ⏱️ 15.04.2026):

	```
	git clone https://github.com/dynawo/dynawo
	```
</details>
<details><summary><b><a href="https://www.gridlabd.org/">GridLAB-D</a></b> (🥈21 ·  ⭐ 200) - Distribution power system simulator. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/gridlab-d/gridlab-d) (👨‍💻 78 · 🔀 120 · 📥 8.8K · 📋 1.5K - 27% open · ⏱️ 28.05.2025):

	```
	git clone https://github.com/gridlab-d/gridlab-d
	```
</details>
<details><summary><b><a href="https://github.com/OpenIPSL/OpenIPSL">OpenIPSL</a></b> (🥈18 ·  ⭐ 110) - A Power System Library written in the Modelica. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/modelica.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/OpenIPSL/OpenIPSL) (👨‍💻 36 · 🔀 66 · 📥 510 · 📋 140 - 11% open · ⏱️ 13.04.2026):

	```
	git clone https://github.com/OpenIPSL/OpenIPSL
	```
</details>
<details><summary><b><a href="https://github.com/changgang/steps">STEPS</a></b> (🥈18 ·  ⭐ 69) - Balanced large-scale AC-DC hybrid power system analysis. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/changgang/steps) (👨‍💻 9 · 🔀 23 · 📥 78 · 📦 7 · 📋 4 - 25% open · ⏱️ 02.02.2026):

	```
	git clone https://github.com/changgang/steps
	```
- [PyPi](https://pypi.org/project/stepspy) (📥 160 / month · ⏱️ 02.02.2026):
	```
	pip install stepspy
	```
</details>
<details><summary><b><a href="https://gridpack.pnnl.gov/wiki/index.php/Main_Page">GridPACK</a></b> (🥈18 ·  ⭐ 61) - High-Performance Electric Grid Simulation. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/GridOPTICS/GridPACK) (👨‍💻 58 · 🔀 23 · 📥 650 · 📋 140 - 13% open · ⏱️ 09.04.2026):

	```
	git clone https://github.com/GridOPTICS/GridPACK
	```
</details>
<details><summary><b><a href="https://www.nlr.gov/analysis/sienna">PowerSimulationsDynamics.jl</a></b> (🥈15 ·  ⭐ 220) - Dynamic Power System simulations; NREL Sienna. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Sienna-Platform/PowerSimulationsDynamics.jl) (👨‍💻 17 · 🔀 55 · 📋 150 - 35% open · ⏱️ 21.04.2026):

	```
	git clone https://github.com/NREL-Sienna/PowerSimulationsDynamics.jl
	```
</details>
<details><summary><b><a href="https://xyce.sandia.gov/">Xyce</a></b> (🥉14 ·  ⭐ 130) - The Xyce Parallel Electronic Simulator. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Xyce/Xyce) (👨‍💻 8 · 🔀 17 · 📥 1.1K · 📋 120 - 36% open · ⏱️ 06.04.2026):

	```
	git clone https://github.com/Xyce/Xyce
	```
- [PyPi](https://pypi.org/project/xyce) (📥 22 / month):
	```
	pip install xyce
	```
- [Conda](https://anaconda.org/vlsida-eda/xyce) (📥 4.8K · ⏱️ 25.03.2025):
	```
	conda install -c vlsida-eda xyce
	```
</details>
<details><summary><b><a href="https://github.com/modelica-3rdparty/PowerSystems">PowerSystems</a></b> (🥉13 ·  ⭐ 77 · 💤) - Modelica 3rd party library for electrical power.. <code><a href="https://tldrlegal.com/search?q=Modelica%20License%202">❗️Modelica License 2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/modelica.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/modelica-3rdparty/PowerSystems) (👨‍💻 10 · 🔀 36 · 📋 41 - 34% open · ⏱️ 07.05.2024):

	```
	git clone https://github.com/modelica-3rdparty/PowerSystems
	```
</details>
<details><summary><b><a href="https://www.epri.com/OpenDER">OpenDER</a></b> (🥉12 ·  ⭐ 70) - Inverter-based DER simulation. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/epri-dev/OpenDER) (👨‍💻 2 · 🔀 29 · 📦 3 · ⏱️ 15.04.2025):

	```
	git clone https://github.com/epri-dev/OpenDER
	```
- [PyPi](https://pypi.org/project/opender) (📥 2.9K / month):
	```
	pip install opender
	```
</details>
<details><summary><b><a href="https://github.com/ANL-CEEESA/gensas">GenSAS</a></b> (🥉5 ·  ⭐ 1) - A C++ based generalized simulation tool based on semi-.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ANL-CEEESA/gensas) (👨‍💻 3 · 🔀 1 · ⏱️ 05.04.2026):

	```
	git clone https://github.com/ANL-CEEESA/gensas
	```
</details>
<details><summary>Show 5 hidden projects...</summary>

- <b><a href="https://github.com/ANL-CEEESA/powersas.m">PowerSAS.m</a></b> (🥉7 ·  ⭐ 21 · 🧊) - Power grid analysis framework based on semi-analytical.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://github.com/OpenHybridSim/OpenHybridSim-code">OpenHybridSim</a></b> (🥉6 ·  ⭐ 8 · 🧊) - EMT-TS hybrid simulation. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="http://faraday1.ucd.ie/psat.html">PSAT</a></b> (🥉4 ·  ⭐ 14 · 🧊) - Unofficial repository of PSAT by Prof. Federico Milano. <code><a href="https://tldrlegal.com/search?q=GPL">❗️GPL</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://github.com/HuaizhiWang/matmtdc">matmtdc</a></b> (🥉4 ·  ⭐ 12 · 🧊) - Dynamic analysis of AC/DC hybrid power systems. <code><a href="https://tldrlegal.com/search?q=undefined">❗️undefined</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://sites.ecse.rpi.edu/~chowj/">PST</a></b> (🥉3 ·  ⭐ 5 · 🧊) - Unofficial repository of PST by Prof. Joe Chow. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
</details>
<br>

## EMT Simulation

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://dpsim.fein-aachen.org/">DPsim</a></b> (🥇19 ·  ⭐ 120) - Simulation for both EMT and phasor. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/sogno-platform/dpsim) (👨‍💻 40 · 🔀 71 · 📦 14 · 📋 170 - 41% open · ⏱️ 15.04.2026):

	```
	git clone https://github.com/sogno-platform/dpsim
	```
- [PyPi](https://pypi.org/project/dpsim) (📥 70 / month):
	```
	pip install dpsim
	```
</details>
<details><summary><b><a href="https://github.com/NatLabRockies/ParaEMT_public">ParaEMT</a></b> (🥉8 ·  ⭐ 92) - Parallel EMT simulation. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NatLabRockies/ParaEMT_public) (👨‍💻 4 · 🔀 43 · 📋 6 - 83% open · ⏱️ 15.01.2026):

	```
	git clone https://github.com/NatLabRockies/ParaEMT_public
	```
</details>
<br>

## Steady State Simulation

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://www.pandapower.org/">pandapower</a></b> (🥇35 ·  ⭐ 1.2K) - Convenient Power System Modelling and Analysis. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/e2nIEE/pandapower) (👨‍💻 190 · 🔀 540 · 📦 550 · 📋 1.1K - 11% open · ⏱️ 23.04.2026):

	```
	git clone https://github.com/e2nIEE/pandapower
	```
- [PyPi](https://pypi.org/project/pandapower) (📥 250K / month):
	```
	pip install pandapower
	```
- [Conda](https://anaconda.org/conda-forge/pandapower) (📥 40K · ⏱️ 27.10.2025):
	```
	conda install -c conda-forge pandapower
	```
- [Docker Hub](https://hub.docker.com/r/pauldepraz/pandapowerapi) (📥 190 · ⏱️ 09.02.2021):
	```
	docker pull pauldepraz/pandapowerapi
	```
</details>
<details><summary><b><a href="https://pypsa.org">PyPSA</a></b> (🥇32 ·  ⭐ 2K) - Python for Power System Analysis. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/PyPSA) (👨‍💻 110 · 🔀 630 · 📦 320 · 📋 540 - 20% open · ⏱️ 22.04.2026):

	```
	git clone https://github.com/PyPSA/PyPSA
	```
- [PyPi](https://pypi.org/project/pypsa) (📥 34K / month):
	```
	pip install pypsa
	```
- [Conda](https://anaconda.org/conda-forge/pypsa) (📥 220K · ⏱️ 22.04.2026):
	```
	conda install -c conda-forge pypsa
	```
</details>
<details><summary><b><a href="https://github.com/PowerGridModel/power-grid-model">Power Grid Model</a></b> (🥇31 ·  ⭐ 220) - Steady-state distribution power system analysis. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PowerGridModel/power-grid-model) (👨‍💻 110 · 🔀 61 · 📥 1.3K · 📦 39 · 📋 310 - 35% open · ⏱️ 21.04.2026):

	```
	git clone https://github.com/PowerGridModel/power-grid-model
	```
- [PyPi](https://pypi.org/project/power-grid-model) (📥 95K / month · 📦 15 · ⏱️ 21.04.2026):
	```
	pip install power-grid-model
	```
- [Conda](https://anaconda.org/conda-forge/power-grid-model) (📥 4.7M · ⏱️ 21.04.2026):
	```
	conda install -c conda-forge power-grid-model
	```
</details>
<details><summary><b><a href="https://www.powsybl.org">PowSyBl Core</a></b> (🥇25 ·  ⭐ 170) - Framework to build power system software. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/powsybl/powsybl-core) (👨‍💻 130 · 🔀 56 · 📦 94 · 📋 680 - 27% open · ⏱️ 21.04.2026):

	```
	git clone https://github.com/powsybl/powsybl-core
	```
</details>
<details><summary><b><a href="https://www.eroots.tech/software">VeraGrid</a></b> (🥇24 ·  ⭐ 530) - Cross-platform power systems software, power flows,.. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/SanPen/VeraGrid) (👨‍💻 59 · 🔀 120 · 📥 59 · 📋 300 - 8% open · ⏱️ 22.04.2026):

	```
	git clone https://github.com/SanPen/VeraGrid
	```
- [PyPi](https://pypi.org/project/veragrid) (📥 1.1K / month):
	```
	pip install veragrid
	```
</details>
<details><summary><b><a href="https://matpower.org/">MATPOWER</a></b> (🥈23 ·  ⭐ 550) - Steady state power flow simulation. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/MATPOWER/matpower) (👨‍💻 23 · 🔀 180 · 📥 720K · 📋 230 - 6% open · ⏱️ 10.03.2026):

	```
	git clone https://github.com/MATPOWER/matpower
	```
- [Docker Hub](https://hub.docker.com/r/matpower/matpower) (📥 4.1K · ⏱️ 11.03.2026):
	```
	docker pull matpower/matpower
	```
</details>
<details><summary><b><a href="https://www.nlr.gov/analysis/sienna">PowerSimulations.jl</a></b> (🥈23 ·  ⭐ 320) - Power Systems optimization simulation and modeling;.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Sienna-Platform/PowerSimulations.jl) (👨‍💻 51 · 🔀 80 · 📋 480 - 13% open · ⏱️ 22.04.2026):

	```
	git clone https://github.com/NREL-Sienna/PowerSimulations.jl
	```
</details>
<details><summary><b><a href="https://www.powsybl.org">PyPowSyBl</a></b> (🥈23 ·  ⭐ 92) - A PowSyBl and Python integration. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/powsybl/pypowsybl) (👨‍💻 41 · 🔀 19 · 📥 480 · 📋 300 - 31% open · ⏱️ 23.04.2026):

	```
	git clone https://github.com/powsybl/pypowsybl
	```
- [PyPi](https://pypi.org/project/pypowsybl) (📥 12K / month · 📦 11 · ⏱️ 16.04.2026):
	```
	pip install pypowsybl
	```
</details>
<details><summary><b><a href="https://l2rpn.chalearn.org/">LightSim2Grid</a></b> (🥈23 ·  ⭐ 65) - A fast backend for the Grid2Op. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Grid2op/lightsim2grid) (👨‍💻 9 · 🔀 14 · 📥 300 · 📦 79 · 📋 62 - 24% open · ⏱️ 21.04.2026):

	```
	git clone https://github.com/BDonnot/lightsim2grid
	```
- [PyPi](https://pypi.org/project/LightSim2Grid) (📥 37K / month):
	```
	pip install LightSim2Grid
	```
- [Docker Hub](https://hub.docker.com/r/bdonnot/lightsim2grid) (📥 620 · ⏱️ 01.02.2022):
	```
	docker pull bdonnot/lightsim2grid
	```
</details>
<details><summary><b><a href="https://www.gurobi.com/features/gurobi-optimods/">Gurobi OptiMods</a></b> (🥈22 ·  ⭐ 180) - Implemented optimization use cases using Gurobi. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Gurobi/gurobi-optimods) (👨‍💻 17 · 🔀 37 · 📦 10 · 📋 83 - 25% open · ⏱️ 09.04.2026):

	```
	git clone https://github.com/Gurobi/gurobi-optimods
	```
- [PyPi](https://pypi.org/project/gurobi-optimods) (📥 1.8K / month):
	```
	pip install gurobi-optimods
	```
</details>
<details><summary><b><a href="https://pypsa.org">PyPSA-Eur</a></b> (🥈21 ·  ⭐ 560) - Sector-Coupled Optimisation Model of the European Energy.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/pypsa-eur) (👨‍💻 110 · 🔀 360 · 📋 650 - 29% open · ⏱️ 23.04.2026):

	```
	git clone https://github.com/PyPSA/pypsa-eur
	```
- [Docker Hub](https://hub.docker.com/r/nimfetrisa/pypsa-eur):
	```
	docker pull nimfetrisa/pypsa-eur
	```
</details>
<details><summary><b><a href="rwl.github.io/PYPOWER/api/">PYPOWER</a></b> (🥈21 ·  ⭐ 400) - Port of MATPOWER to Python. <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/rwl/PYPOWER) (👨‍💻 22 · 🔀 120 · 📦 160 · 📋 51 - 70% open · ⏱️ 24.11.2025):

	```
	git clone https://github.com/rwl/PYPOWER
	```
- [PyPi](https://pypi.org/project/PYPOWER) (📥 30K / month):
	```
	pip install PYPOWER
	```
- [Conda](https://anaconda.org/invenia/pypower) (📥 3.2K · ⏱️ 25.03.2025):
	```
	conda install -c invenia pypower
	```
- [Docker Hub](https://hub.docker.com/r/hwanghust/pypower) (📥 41 · ⏱️ 19.05.2019):
	```
	docker pull hwanghust/pypower
	```
</details>
<details><summary><b><a href="https://www.gridpath.io/">GridPath</a></b> (🥈21 ·  ⭐ 130) - Power system planning and operations. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/blue-marble/gridpath) (👨‍💻 13 · 🔀 65 · 📥 1.4K · 📦 5 · 📋 340 - 14% open · ⏱️ 22.04.2026):

	```
	git clone https://github.com/blue-marble/gridpath
	```
- [PyPi](https://pypi.org/project/GridPath) (📥 230 / month):
	```
	pip install GridPath
	```
</details>
<details><summary><b><a href="https://pypsa-meets-earth.github.io/">PyPSA-Earth</a></b> (🥈20 ·  ⭐ 340) - Open optimisation model for study energy system.. <code><a href="http://bit.ly/3pwmjO5">❗️AGPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/pypsa-meets-earth/pypsa-earth) (👨‍💻 90 · 🔀 300 · 📋 620 - 37% open · ⏱️ 20.04.2026):

	```
	git clone https://github.com/pypsa-meets-earth/pypsa-earth
	```
</details>
<details><summary><b><a href="https://github.com/pnnl/tesp">TESP</a></b> (🥈20 ·  ⭐ 48 · 📉) - Transactive Energy Simulation Platform. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/pnnl/tesp) (👨‍💻 31 · 🔀 41 · 📥 510 · 📦 2 · 📋 130 - 27% open · ⏱️ 05.02.2026):

	```
	git clone https://github.com/pnnl/tesp
	```
- [PyPi](https://pypi.org/project/tesp_support) (📥 310 / month):
	```
	pip install tesp_support
	```
</details>
<details><summary><b><a href="https://github.com/lanl-ansi/PowerModels.jl">PowerModels.jl</a></b> (🥈18 ·  ⭐ 460) - Power Network Optimization. <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/lanl-ansi/PowerModels.jl) (👨‍💻 32 · 🔀 160 · 📋 510 - 16% open · ⏱️ 13.04.2026):

	```
	git clone https://github.com/lanl-ansi/PowerModels.jl
	```
</details>
<details><summary><b><a href="https://www.nlr.gov/reopt/">REopt</a></b> (🥈18 ·  ⭐ 120) - Renewable Energy Integration & Optimization. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NatLabRockies/REopt_API) (👨‍💻 25 · 🔀 65 · 📥 570 · 📋 86 - 51% open · ⏱️ 06.03.2026):

	```
	git clone https://github.com/NatLabRockies/REopt_API
	```
</details>
<details><summary><b><a href="https://github.com/grid-parity-exchange/Prescient">Prescient</a></b> (🥈18 ·  ⭐ 40) - Production cost modeling for power generation and.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/grid-parity-exchange/Prescient) (👨‍💻 11 · 🔀 16 · 📦 11 · 📋 64 - 26% open · ⏱️ 06.10.2025):

	```
	git clone https://github.com/grid-parity-exchange/Prescient
	```
- [PyPi](https://pypi.org/project/gridx-prescient) (📥 23K / month):
	```
	pip install gridx-prescient
	```
</details>
<details><summary><b><a href="https://www.nlr.gov/analysis/sienna">PowerNetworkMatrices.jl</a></b> (🥈18 ·  ⭐ 30) - Power systems matrices; NREL Sienna. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Sienna-Platform/PowerNetworkMatrices.jl) (👨‍💻 15 · 🔀 21 · 📋 120 - 27% open · ⏱️ 21.04.2026):

	```
	git clone https://github.com/NREL-Sienna/PowerNetworkMatrices.jl
	```
</details>
<details><summary><b><a href="https://ltb.curent.org/">LTB AMS</a></b> (🥈18 ·  ⭐ 24 · 📈) - Scheduling Modeling and Simulation; CURENT LTB. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CURENT/ams) (👨‍💻 4 · 🔀 8 · 📥 94 · 📦 3 · 📋 24 - 54% open · ⏱️ 23.04.2026):

	```
	git clone https://github.com/CURENT/ams
	```
- [PyPi](https://pypi.org/project/ltbams) (📥 110 / month):
	```
	pip install ltbams
	```
- [Conda](https://anaconda.org/conda-forge/ltbams) (📥 30K · ⏱️ 23.12.2025):
	```
	conda install -c conda-forge ltbams
	```
</details>
<details><summary><b><a href="https://energy.mit.edu/genx/">GenX</a></b> (🥉17 ·  ⭐ 350) - Configurable capacity expansion model. <code><a href="http://bit.ly/2KucAZR">❗️GPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/GenXProject/GenX.jl) (👨‍💻 37 · 🔀 140 · 📋 330 - 19% open · ⏱️ 09.01.2026):

	```
	git clone https://github.com/GenXProject/GenX
	```
</details>
<details><summary><b><a href="https://pypsa.org">PyPSA-USA</a></b> (🥉17 ·  ⭐ 120) - Power System Model for the United States. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/pypsa-usa) (👨‍💻 16 · 🔀 45 · 📋 390 - 26% open · ⏱️ 10.02.2026):

	```
	git clone https://github.com/PyPSA/pypsa-usa
	```
</details>
<details><summary><b><a href="https://github.com/IIT-EnergySystemModels/openTEPES">openTEPES</a></b> (🥉17 ·  ⭐ 54) - Open Generation, Storage, and Transmission Operation.. <code><a href="http://bit.ly/3pwmjO5">❗️AGPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/IIT-EnergySystemModels/openTEPES) (👨‍💻 10 · 🔀 26 · 📥 120 · ⏱️ 17.04.2026):

	```
	git clone https://github.com/IIT-EnergySystemModels/openTEPES
	```
- [PyPi](https://pypi.org/project/openTEPES) (📥 530 / month):
	```
	pip install openTEPES
	```
</details>
<details><summary><b><a href="https://www.powsybl.org">Open RAO</a></b> (🥉17 ·  ⭐ 31) - Power systems coordinated capacity calculation and.. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/powsybl/powsybl-open-rao) (👨‍💻 41 · 🔀 8 · 📥 52 · 📋 230 - 31% open · ⏱️ 23.04.2026):

	```
	git clone https://github.com/powsybl/powsybl-open-rao
	```
</details>
<details><summary><b><a href="https://www.nlr.gov/analysis/sienna">PowerFlows.jl</a></b> (🥉17 ·  ⭐ 29) - Collection of Power Flow solution; NREL Sienna. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Sienna-Platform/PowerFlows.jl) (👨‍💻 14 · 🔀 24 · 📋 170 - 33% open · ⏱️ 20.04.2026):

	```
	git clone https://github.com/NREL-Sienna/PowerFlows.jl
	```
</details>
<details><summary><b><a href="https://github.com/ANL-CEEESA/UnitCommitment.jl">UnitCommitment.jl</a></b> (🥉16 ·  ⭐ 140) - Optimization package for the Security-Constrained.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ANL-CEEESA/UnitCommitment.jl) (👨‍💻 7 · 🔀 36 · ⏱️ 10.04.2026):

	```
	git clone https://github.com/ANL-CEEESA/UnitCommitment.jl
	```
</details>
<details><summary><b><a href="https://github.com/grid-parity-exchange/Egret">EGRET</a></b> (🥉15 ·  ⭐ 160) - Tools for Power Systems Optimization Modeling. <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/grid-parity-exchange/Egret) (👨‍💻 41 · 🔀 61 · 📋 87 - 56% open · ⏱️ 22.01.2026):

	```
	git clone https://github.com/grid-parity-exchange/Egret
	```
</details>
<details><summary><b><a href="https://www.gridpath.io/">ExaGO</a></b> (🥉15 ·  ⭐ 93) - Large-scale power grid optimization. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/pnnl/ExaGO) (👨‍💻 35 · 🔀 17 · 📋 100 - 1% open · ⏱️ 23.03.2026):

	```
	git clone https://github.com/pnnl/ExaGO
	```
</details>
<details><summary><b><a href="https://www.nlr.gov/analysis/reeds/">ReEDS-2.0</a></b> (🥉14 ·  ⭐ 180) - Capacity planning and dispatch model. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NatLabRockies/ReEDS-2.0) (👨‍💻 14 · 🔀 81 · 📋 32 - 21% open · ⏱️ 22.04.2026):

	```
	git clone https://github.com/NatLabRockies/ReEDS-2.0
	```
</details>
<details><summary><b><a href="https://github.com/bukhsh/oats">OATS</a></b> (🥉12 ·  ⭐ 29 · 💤) - Optimisation and Analysis Toolbox for Power Systems. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/bukhsh/oats) (👨‍💻 4 · 🔀 7 · 📦 3 · 📋 78 - 28% open · ⏱️ 11.12.2024):

	```
	git clone https://github.com/bukhsh/oats
	```
- [PyPi](https://pypi.org/project/oatspower) (📥 74 / month):
	```
	pip install oatspower
	```
</details>
<details><summary><b><a href="https://github.com/LBNL-ETA/DOPER">DOPER</a></b> (🥉12 ·  ⭐ 22) - Distributed Optimal and Predictive Energy Resources. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/LBNL-ETA/DOPER) (👨‍💻 3 · 🔀 11 · ⏱️ 23.04.2026):

	```
	git clone https://github.com/LBNL-ETA/DOPER
	```
</details>
<details><summary><b><a href="https://matpower.org/">MOST</a></b> (🥉11 ·  ⭐ 39) - MATPOWER Optimal Scheduling Tool. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/MATPOWER/most) (👨‍💻 2 · 🔀 14 · 📋 43 - 13% open · ⏱️ 16.02.2026):

	```
	git clone https://github.com/MATPOWER/most
	```
</details>
<details><summary><b><a href="https://github.com/pypsa-meets-earth/pypsa-distribution">PyPSA-Distribution</a></b> (🥉11 ·  ⭐ 29) - Multi-energy model for small scale applications in.. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/pypsa-meets-earth/pypsa-distribution) (👨‍💻 7 · 🔀 14 · 📋 29 - 68% open · ⏱️ 10.02.2026):

	```
	git clone https://github.com/pypsa-meets-earth/pypsa-distribution
	```
</details>
<details><summary><b><a href="https://www.nlr.gov/analysis/sienna">PowerSystemsInvestmentsPortfolios.jl</a></b> (🥉10 ·  ⭐ 14) - Data models for Power Systems investment models; NREL.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Sienna-Platform/PowerSystemsInvestmentsPortfolios.jl) (👨‍💻 7 · 🔀 9 · 📋 64 - 37% open · ⏱️ 21.04.2026):

	```
	git clone https://github.com/NREL-Sienna/PowerSystemsInvestmentsPortfolios.jl
	```
</details>
<details><summary><b><a href="https://github.com/ebalogun01/EV-EcoSim">EV-EcoSim</a></b> (🥉9 ·  ⭐ 26 · 💤) - A grid-aware co-simulation platform for the design and.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ebalogun01/EV-EcoSim) (🔀 5 · 📋 72 - 12% open · ⏱️ 19.04.2024):

	```
	git clone https://github.com/ebalogun01/EV-EcoSim/
	```
</details>
<details><summary><b><a href="https://www.nlr.gov/analysis/sienna">PowerSystemsInvestments.jl</a></b> (🥉8 ·  ⭐ 21) - Power Systems investment models; NREL Sienna. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Sienna-Platform/PowerSystemsInvestments.jl) (👨‍💻 4 · 🔀 12 · 📋 33 - 84% open · ⏱️ 21.07.2025):

	```
	git clone https://github.com/NREL-Sienna/PowerSystemsInvestments.jl
	```
</details>
<details><summary><b><a href="https://www2.econ.iastate.edu/tesfatsi/AMESMarketHome.htm">AMES - Version 5.0</a></b> (🥉7 ·  ⭐ 32) - Wholesale Power Market Test Bed. <code><a href="https://github.com/ames-market/AMES-V5.0/blob/master/LICENSE.rst">❗️Custom</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ames-market/AMES-V5.0) (👨‍💻 3 · 🔀 8 · ⏱️ 03.02.2026):

	```
	git clone https://github.com/ames-market/AMES-V5.0
	```
</details>
<details><summary><b><a href="https://esca.epri.com/usregen">US-REGEN</a></b> (🥉6 ·  ⭐ 21) - U.S. regional economy, greenhouse gas, and energy model. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/epri-dev/US-REGEN) (👨‍💻 2 · 🔀 3 · ⏱️ 27.05.2025):

	```
	git clone https://github.com/epri-dev/US-REGEN
	```
</details>
<details><summary><b><a href="https://github.com/ANL-CEEESA/EGRIP.jl">EGRIP.jl</a></b> (🥉6 ·  ⭐ 10) - Julia/MATALB package for power system restoration.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ANL-CEEESA/EGRIP.jl) (👨‍💻 5 · ⏱️ 06.05.2025):

	```
	git clone https://github.com/ANL-CEEESA/EGRIP.jl
	```
</details>
<details><summary><b><a href="https://github.com/NatLabRockies/ASSET">ASSET</a></b> (🥉5 ·  ⭐ 19) - Assess and analyze grid strength. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NatLabRockies/ASSET) (👨‍💻 2 · 🔀 7 · ⏱️ 05.05.2025):

	```
	git clone https://github.com/NatLabRockies/ASSET
	```
</details>
<details><summary><b><a href="https://github.com/PPGS-Tools/PyPSA-stochUC">PyPSA-stochUC</a></b> (🥉5 ·  ⭐ 18 · 💤) - Stochastic unit commitment extension for PyPSA with market.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PPGS-Tools/PyPSA-stochUC) (👨‍💻 2 · 🔀 4 · ⏱️ 09.12.2024):

	```
	git clone https://github.com/PPGS-Tools/PyPSA-stochUC
	```
</details>
<details><summary><b><a href="https://github.com/LSU-RAISE-LAB/DPLib">DPLib</a></b> (🥉5 ·  ⭐ 11) - MATLAB-based distributed benchmark library and.. <code><a href="https://tldrlegal.com/search?q=Academic%20and%20Research%20Use%20Only">❗️Academic and Research Use Only</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/LSU-RAISE-LAB/DPLib) (👨‍💻 2 · 🔀 3 · ⏱️ 26.01.2026):

	```
	git clone https://github.com/LSU-RAISE-LAB/DPLib
	```
</details>
<details><summary><b><a href="https://www.epri.com/pages/sa/opendss">OpenDSS</a></b> (🥉2) - Distribution system simulator. <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- _No project information available._</details>
<details><summary>Show 6 hidden projects...</summary>

- <b><a href="https://github.com/ames-market/psst">PSST</a></b> (🥉10 ·  ⭐ 44 · 🧊) - Power System Simulation Toolbox for SCUC and SCED in.. <code><a href="https://tldrlegal.com/search?q=AMES%20License">❗️AMES License</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://github.com/felipemarkson/dssdata">DSSData</a></b> (🥉8 ·  ⭐ 17 · 🧊) - A micro-framework for simulation and data analysis of.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://github.com/power-flow-analyzer/PowerFlowAnalyzer">PowerFlowAnalyzer</a></b> (🥉7 ·  ⭐ 7 · 🧊) - Toolbox for power system analysis. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://gitlab.com/tum-msv/hynet">hynet</a></b> (🥉6 ·  ⭐ 4 · 🧊) - Optimal power flow framework for hybrid AC/DC power systems. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://github.com/yasirroni/mypower">mypower</a></b> (🥉5 ·  ⭐ 8 · 🧊) - Supplementary function of MATPOWER in Python. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://www2.econ.iastate.edu/tesfatsi/AMESMarketHome.htm">AMES (V4.0)</a></b> (🥉3 ·  ⭐ 13 · 🧊) - Agent based Modeling of Electricity Systems. <code><a href="http://bit.ly/2KucAZR">❗️GPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
</details>
<br>

## Interface

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/PauloRadatz/py_dss_interface">py-dss-interface</a></b> (🥇20 ·  ⭐ 43 · 📉) - A package for access to direct dll version of OpenDSS. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PauloRadatz/py_dss_interface) (👨‍💻 7 · 🔀 12 · 📥 39 · 📦 41 · 📋 57 - 1% open · ⏱️ 15.04.2026):

	```
	git clone https://github.com/PauloRadatz/py_dss_interface
	```
- [PyPi](https://pypi.org/project/py-dss-interface) (📥 6K / month):
	```
	pip install py-dss-interface
	```
</details>
<details><summary><b><a href="https://github.com/UGM-EPSLab/matpowercaseframes">matpowercaseframes</a></b> (🥇20 ·  ⭐ 6) - Parse MATPOWER case into pandas DataFrame. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/UGM-EPSLab/matpowercaseframes) (👨‍💻 9 · 🔀 3 · 📦 37 · 📋 14 - 42% open · ⏱️ 01.04.2026):

	```
	git clone https://github.com/UGM-EPSLab/matpowercaseframes
	```
- [PyPi](https://pypi.org/project/matpowercaseframes) (📥 27K / month · 📦 7 · ⏱️ 01.04.2026):
	```
	pip install matpowercaseframes
	```
</details>
<details><summary><b><a href="https://github.com/NLR-Distribution-Suite/erad">ERAD</a></b> (🥈17 ·  ⭐ 24) - Toolkit for computing resilience metrics for power.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NLR-Distribution-Suite/erad) (👨‍💻 7 · 🔀 11 · ⏱️ 07.04.2026):

	```
	git clone https://github.com/NLR-Distribution-Suite/erad
	```
- [PyPi](https://pypi.org/project/NREL-erad) (📥 250 / month):
	```
	pip install NREL-erad
	```
</details>
<details><summary><b><a href="https://github.com/sogno-platform/cimpy">CIMpy</a></b> (🥈16 ·  ⭐ 71 · 💤) - CIM files to the XML/RDF format. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/sogno-platform/cimpy) (👨‍💻 10 · 🔀 25 · 📦 13 · 📋 17 - 29% open · ⏱️ 23.02.2025):

	```
	git clone https://github.com/sogno-platform/cimpy
	```
- [PyPi](https://pypi.org/project/cimpy) (📥 1.4K / month):
	```
	pip install cimpy
	```
</details>
<details><summary><b><a href="https://github.com/mzy2240/ESA">Easy SimAuto</a></b> (🥈16 ·  ⭐ 52) - Python interface to PowerWorld. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/mzy2240/ESA) (👨‍💻 13 · 🔀 16 · 📦 9 · 📋 100 - 18% open · ⏱️ 31.12.2025):

	```
	git clone https://github.com/mzy2240/ESA
	```
- [PyPi](https://pypi.org/project/esa) (📥 1.4K / month):
	```
	pip install esa
	```
</details>
<details><summary><b><a href="https://github.com/ieeh-tu-dresden/powerfactory-tools">powerfactory-tools</a></b> (🥈16 ·  ⭐ 51) - Python toolbox for control of DIgSILENT PowerFactory. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ieeh-tu-dresden/powerfactory-tools) (👨‍💻 3 · 🔀 9 · 📥 380 · 📦 2 · 📋 190 - 11% open · ⏱️ 02.04.2026):

	```
	git clone https://github.com/ieeh-tu-dresden/powerfactory-tools
	```
- [PyPi](https://pypi.org/project/ieeh-powerfactory-tools) (📥 270 / month):
	```
	pip install ieeh-powerfactory-tools
	```
</details>
<details><summary><b><a href="https://dss-extensions.org/">AltDSS/DSS C-API</a></b> (🥈16 ·  ⭐ 38 · 💤) - a plain C interface to OpenDSS. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dss-extensions/dss_capi) (👨‍💻 8 · 🔀 16 · 📥 34K · 📋 120 - 10% open · ⏱️ 11.07.2024):

	```
	git clone https://github.com/dss-extensions/dss_capi
	```
</details>
<details><summary><b><a href="https://github.com/yasirroni/matpower-pip">matpower-pip</a></b> (🥈16 ·  ⭐ 26) - Easy Python Access to MATPOWER. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/yasirroni/matpower-pip) (👨‍💻 2 · 🔀 3 · 📦 11 · 📋 21 - 28% open · ⏱️ 02.04.2026):

	```
	git clone https://github.com/yasirroni/matpower-pip
	```
- [PyPi](https://pypi.org/project/matpower) (📥 480 / month):
	```
	pip install matpower
	```
</details>
<details><summary><b><a href="https://www.nlr.gov/grid/pydss">PyDSS</a></b> (🥈14 ·  ⭐ 41) - A Python wrapper for OpenDSS. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NatLabRockies/PyDSS) (👨‍💻 23 · 🔀 27 · 📦 2 · 📋 29 - 44% open · ⏱️ 26.01.2026):

	```
	git clone https://github.com/NatLabRockies/PyDSS
	```
- [PyPi](https://pypi.org/project/pydss) (📥 57 / month):
	```
	pip install pydss
	```
</details>
<details><summary><b><a href="https://github.com/cimug-org/CIMTool">CIMTool</a></b> (🥉13 ·  ⭐ 66) - CIMugs CIMTool for the CIM. <code><a href="https://tldrlegal.com/search?q=LGPL-2.1">❗️LGPL-2.1</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cimug-org/CIMTool) (👨‍💻 17 · 🔀 11 · 📥 3.5K · 📋 120 - 33% open · ⏱️ 22.03.2026):

	```
	git clone https://github.com/CIMug-org/CIMTool
	```
</details>
<details><summary><b><a href="https://dss-extensions.org/">OpenDSSDirect.jl</a></b> (🥉12 ·  ⭐ 29) - Cross-platform Julia interface to OpenDSS. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dss-extensions/OpenDSSDirect.jl) (👨‍💻 9 · 🔀 6 · 📋 48 - 25% open · ⏱️ 17.02.2026):

	```
	git clone https://github.com/dss-extensions/OpenDSSDirect.jl
	```
</details>
<details><summary><b><a href="https://github.com/FraunhIEE-UniKassel-PowSysStability/powfacpy">powfacpy</a></b> (🥉10 ·  ⭐ 10) - Python wrapper around the DIgSILENT PowerFactory API. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/FraunhIEE-UniKassel-PowSysStability/powfacpy) (👨‍💻 2 · 🔀 3 · 📦 5 · 📋 41 - 17% open · ⏱️ 20.02.2026):

	```
	git clone https://github.com/FraunhIEE-UniKassel-PowSysStability/powfacpy
	```
- [PyPi](https://pypi.org/project/powfacpy) (📥 110 / month):
	```
	pip install powfacpy
	```
</details>
<details><summary><b><a href="https://github.com/cimug-org/CIMTool-Builders-Library">CIMTool-Builders-Library</a></b> (🥉8 ·  ⭐ 10) - Publically available XSLT builders. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cimug-org/CIMTool-Builders-Library) (👨‍💻 5 · 🔀 3 · ⏱️ 21.11.2025):

	```
	git clone https://github.com/CIMug-org/CIMTool-Builders-Library
	```
</details>
<details><summary><b><a href="https://dss-extensions.org/">DSS MATLAB</a></b> (🥉7 ·  ⭐ 11 · 💤) - MATLAB interface to OpenDSS. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dss-extensions/dss_matlab) (🔀 2 · 📥 1.3K · 📋 21 - 33% open · ⏱️ 30.10.2024):

	```
	git clone https://github.com/dss-extensions/dss_matlab
	```
</details>
<details><summary><b><a href="https://www.pscad.com/">mhi-pscad</a></b> (🥉6) - PSCAD Automation library. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [PyPi](https://pypi.org/project/mhi-pscad) (📥 6.4K / month):
	```
	pip install mhi-pscad
	```
</details>
<details><summary><b><a href="https://github.com/epri-dev/OpenDER_interface">OpenDER interface</a></b> (🥉5 ·  ⭐ 6 · 💤) - Interface for OpenDER. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/epri-dev/OpenDER_interface) (👨‍💻 2 · 🔀 2 · ⏱️ 10.02.2025):

	```
	git clone https://github.com/epri-dev/OpenDER_interface
	```
</details>
<details><summary>Show 8 hidden projects...</summary>

- <b><a href="https://dss-extensions.org/">OpenDSSDirect.py</a></b> (🥇21 ·  ⭐ 110 · 🧊) - A direct library interface to OpenDSS. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://dss-extensions.org/">AltDSS-Python</a></b> (🥈14 ·  ⭐ 18 · 🧊) - Modern Python bindings for an alternative.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://github.com/lanl-ansi/grg-pssedata">grg-pssedata</a></b> (🥉12 ·  ⭐ 35 · 🧊) - Python tools for working with PSSE v33 data files. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://github.com/RWTH-IAEW/cimpyorm">cimpyorm</a></b> (🥉11 ·  ⭐ 12 · 🧊) - Python ORM middleware for IEC CIM and CGMES datasets. <code><a href="https://tldrlegal.com/search?q=BSD-3.0">❗️BSD-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://dss-extensions.org/">DSS Sharp</a></b> (🥉7 ·  ⭐ 11 · 🧊) - C#/.NET wrapper library for DSS C-API. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://github.com/anderson-optimization/em-psse">PSSE RAW</a></b> (🥉5 ·  ⭐ 39 · 🧊) - PSSE RAW parser. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://ltb.curent.org">Andes.jl</a></b> (🥉5 ·  ⭐ 9 · 🧊) - Julia interface for ANDES. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://github.com/mzy2240/EasySimauto.jl">EasySimauto.jl</a></b> (🥉3 ·  ⭐ 7 · 🧊) - Julia interface for EasySimAuto and PowerWorld. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
</details>
<br>

## Gas Simulation

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://www.pandapipes.org/">pandapipes</a></b> (🥇26 ·  ⭐ 210) - Pipeflow Calculation Tool. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/e2nIEE/pandapipes) (👨‍💻 29 · 🔀 77 · 📦 41 · 📋 180 - 50% open · ⏱️ 17.04.2026):

	```
	git clone https://github.com/e2nIEE/pandapipes
	```
- [PyPi](https://pypi.org/project/pandapipes) (📥 10K / month · 📦 14 · ⏱️ 16.01.2026):
	```
	pip install pandapipes
	```
</details>
<details><summary><b><a href="https://github.com/lanl-ansi/GasModels.jl">GasModels.jl</a></b> (🥉18 ·  ⭐ 78) - Gas Network Optimization. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/lanl-ansi/GasModels.jl) (👨‍💻 19 · 🔀 22 · 📋 180 - 26% open · ⏱️ 09.04.2026):

	```
	git clone https://github.com/lanl-ansi/GasModels.jl
	```
</details>
<details><summary>Show 1 hidden projects...</summary>

- <b><a href="https://matpower.org/">MPNG</a></b> (🥉7 ·  ⭐ 11 · 🧊) - Simulator for Optimal Power and Natural Gas Flow. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
</details>
<br>

## Co-Simulation Environment

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://openmodelica.org">OpenModelica</a></b> (🥇29 ·  ⭐ 1.3K) - Modelica-based environment for modeling and simulation. <code><a href="https://tldrlegal.com/search?q=Modelica%20License%202">❗️Modelica License 2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/modelica.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/OpenModelica/OpenModelica) (👨‍💻 210 · 🔀 360 · 📥 510 · 📋 8.8K - 24% open · ⏱️ 23.04.2026):

	```
	git clone https://github.com/OpenModelica/OpenModelica
	```
- [Docker Hub](https://hub.docker.com/r/openmodelica/openmodelica) (📥 66K · ⭐ 6 · ⏱️ 26.02.2026):
	```
	docker pull openmodelica/openmodelica
	```
</details>
<details><summary><b><a href="https://precice.org/">precice</a></b> (🥉25 ·  ⭐ 930 · 📉) - Precise Code Interaction Coupling Environment. <code><a href="http://bit.ly/37RvQcA">❗️LGPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/precice/precice) (👨‍💻 76 · 🔀 270 · 📥 43K · 📋 960 - 20% open · ⏱️ 21.04.2026):

	```
	git clone https://github.com/precice/precice
	```
- [PyPi](https://pypi.org/project/pyprecice) (📥 1.8K / month):
	```
	pip install pyprecice
	```
- [Conda](https://anaconda.org/conda-forge/pyprecice) (📥 160K · ⏱️ 08.04.2026):
	```
	conda install -c conda-forge pyprecice
	```
- [Docker Hub](https://hub.docker.com/r/precice/precice) (📥 40K · ⏱️ 23.04.2026):
	```
	docker pull precice/precice
	```
</details>
<br>

## Optimization Modeling Language (primarily for optimization modeling)

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/cvxpy/cvxpy">CVXPY</a></b> (🥇41 ·  ⭐ 6.2K) - Convex optimization modeling language. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cvxpy/cvxpy) (👨‍💻 260 · 🔀 1.1K · 📥 790 · 📦 19K · 📋 1.6K - 9% open · ⏱️ 23.04.2026):

	```
	git clone https://github.com/cvxpy/cvxpy
	```
- [PyPi](https://pypi.org/project/cvxpy) (📥 3.6M / month):
	```
	pip install cvxpy
	```
- [Conda](https://anaconda.org/conda-forge/cvxpy) (📥 2.1M · ⏱️ 14.04.2026):
	```
	conda install -c conda-forge cvxpy
	```
</details>
<details><summary><b><a href="https://www.pyomo.org">Pyomo</a></b> (🥈40 ·  ⭐ 2.4K) - Python-based Optimization Modeling Language. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Pyomo/pyomo) (👨‍💻 200 · 🔀 550 · 📥 5.6K · 📦 4.8K · 📋 1.5K - 21% open · ⏱️ 22.04.2026):

	```
	git clone https://github.com/Pyomo/pyomo
	```
- [PyPi](https://pypi.org/project/Pyomo) (📥 1.1M / month):
	```
	pip install Pyomo
	```
- [Conda](https://anaconda.org/conda-forge/pyomo) (📥 2.1M · ⏱️ 20.02.2026):
	```
	conda install -c conda-forge pyomo
	```
</details>
<details><summary><b><a href="https://jump.dev">JuMP</a></b> (🥈25 ·  ⭐ 2.4K) - Julia-based Optimization Modeling Language. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/jump-dev/JuMP.jl) (👨‍💻 170 · 🔀 410 · 📋 1.5K - 1% open · ⏱️ 22.04.2026):

	```
	git clone https://github.com/jump-dev/JuMP.jl
	```
</details>
<details><summary><b><a href="https://github.com/metab0t/PyOptInterface">PyOptInterface</a></b> (🥉20 ·  ⭐ 310 · 📉) - Efficient modeling interface for optimization in.. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/metab0t/PyOptInterface) (👨‍💻 6 · 🔀 26 · 📦 21 · 📋 42 - 11% open · ⏱️ 07.04.2026):

	```
	git clone https://github.com/metab0t/PyOptInterface
	```
- [PyPi](https://pypi.org/project/pyoptinterface) (📥 7.8K / month):
	```
	pip install pyoptinterface
	```
</details>
<details><summary><b><a href="https://github.com/XiongPengNUS/rsome">RSOME</a></b> (🥉16 ·  ⭐ 340 · 💤) - Robust Stochastic Optimization Made Easy. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/XiongPengNUS/rsome) (👨‍💻 3 · 🔀 60 · 📋 42 - 9% open · ⏱️ 15.11.2024):

	```
	git clone https://github.com/XiongPengNUS/rsome
	```
- [PyPi](https://pypi.org/project/rsome) (📥 1.2K / month):
	```
	pip install rsome
	```
</details>
<details><summary><b><a href="https://github.com/exanauts/ExaModels.jl">ExaModels</a></b> (🥉15 ·  ⭐ 74) - An algebraic modeling and automatic differentiation tool.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/exanauts/ExaModels.jl) (👨‍💻 11 · 🔀 8 · 📋 50 - 14% open · ⏱️ 18.04.2026):

	```
	git clone https://github.com/exanauts/ExaModels.jl
	```
</details>
<br>

## Optimizer (capable of solving)

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://developers.google.com/optimization/">OR-Tools</a></b> (🥇39 ·  ⭐ 13K) - Google Optimization Tools. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/google/or-tools) (👨‍💻 200 · 🔀 2.4K · 📥 340K · 📦 370 · 📋 3.2K - 2% open · ⏱️ 31.03.2026):

	```
	git clone https://github.com/google/or-tools
	```
- [PyPi](https://pypi.org/project/ortools) (📥 6.3M / month · 📦 390 · ⏱️ 14.01.2026):
	```
	pip install ortools
	```
- [Conda](https://anaconda.org/conda-forge/ortools-python) (📥 150K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge ortools-python
	```
</details>
<details><summary><b><a href="https://highs.dev/">HiGHS</a></b> (🥇35 ·  ⭐ 1.6K · 📈) - Large-scale Sparse Linear Problem Optimizer. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/rust.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/r.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ERGO-Code/HiGHS) (👨‍💻 120 · 🔀 300 · 📥 36K · 📋 1.1K - 14% open · ⏱️ 08.04.2026):

	```
	git clone https://github.com/ERGO-Code/HiGHS
	```
- [PyPi](https://pypi.org/project/highspy) (📥 1.9M / month · 📦 170 · ⏱️ 06.04.2026):
	```
	pip install highspy
	```
- [Conda](https://anaconda.org/conda-forge/highs) (📥 63K · ⏱️ 06.04.2026):
	```
	conda install -c conda-forge highs
	```
</details>
<details><summary><b><a href="https://github.com/google/or-tools">Tulip</a></b> (🥈34 ·  ⭐ 13K) - Interior-point solver in pure Julia. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/google/or-tools) (👨‍💻 200 · 🔀 2.3K · 📥 340K · 📦 370 · 📋 3.2K - 2% open · ⏱️ 31.03.2026):

	```
	git clone https://github.com/google/or-tools
	```
</details>
<details><summary><b><a href="https://github.com/google/or-tools">Xopt</a></b> (🥈34 ·  ⭐ 13K) - Flexible high-level optimization in Python. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/google/or-tools) (👨‍💻 200 · 🔀 2.3K · 📥 340K · 📦 370 · 📋 3.2K - 2% open · ⏱️ 31.03.2026):

	```
	git clone https://github.com/google/or-tools
	```
- [PyPi](https://pypi.org/project/xopt) (📥 1.1K / month):
	```
	pip install xopt
	```
- [Conda](https://anaconda.org/conda-forge/xopt) (📥 78K · ⏱️ 20.03.2026):
	```
	conda install -c conda-forge xopt
	```
</details>
<details><summary><b><a href="https://osqp.org">OSQP</a></b> (🥈32 ·  ⭐ 2.1K · 📈) - Operator Splitting QP Solver. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/r.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/osqp/osqp) (👨‍💻 36 · 🔀 410 · 📥 200K · 📋 400 - 30% open · ⏱️ 10.11.2025):

	```
	git clone https://github.com/osqp/osqp
	```
- [PyPi](https://pypi.org/project/osqp) (📥 3.8M / month · 📦 150 · ⏱️ 11.02.2026):
	```
	pip install osqp
	```
- [Conda](https://anaconda.org/conda-forge/osqp) (📥 1.5M · ⏱️ 16.02.2026):
	```
	conda install -c conda-forge osqp
	```
</details>
<details><summary><b><a href="https://www.scipopt.org/">PySCIPOpt</a></b> (🥈31 ·  ⭐ 980) - Python interface for SCIP. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/scipopt/PySCIPOpt) (👨‍💻 89 · 🔀 280 · 📦 440 · 📋 640 - 3% open · ⏱️ 23.04.2026):

	```
	git clone https://github.com/scipopt/PySCIPOpt
	```
- [PyPi](https://pypi.org/project/PySCIPOpt) (📥 210K / month · 📦 94 · ⏱️ 05.02.2026):
	```
	pip install PySCIPOpt
	```
- [Conda](https://anaconda.org/conda-forge/pyscipopt) (📥 710K · ⏱️ 05.02.2026):
	```
	conda install -c conda-forge pyscipopt
	```
</details>
<details><summary><b><a href="https://github.com/cvxgrp/scs">SCS</a></b> (🥈31 ·  ⭐ 620 · 📈) - Splitting Conic Solver. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/r.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cvxgrp/scs) (👨‍💻 32 · 🔀 140 · 📋 190 - 22% open · ⏱️ 22.04.2026):

	```
	git clone https://github.com/cvxgrp/scs
	```
- [PyPi](https://pypi.org/project/scs) (📥 3M / month · 📦 72 · ⏱️ 09.01.2026):
	```
	pip install scs
	```
- [Conda](https://anaconda.org/conda-forge/scs) (📥 1.7M · ⏱️ 10.01.2026):
	```
	conda install -c conda-forge scs
	```
</details>
<details><summary><b><a href="https://cvxopt.org/">CVXOPT</a></b> (🥈29 ·  ⭐ 1K) - Python Software for Convex Optimization. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cvxopt/cvxopt) (👨‍💻 10 · 🔀 210 · 📦 15K · 📋 200 - 20% open · ⏱️ 02.03.2026):

	```
	git clone https://github.com/cvxopt/cvxopt
	```
- [PyPi](https://pypi.org/project/cvxopt) (📥 850K / month):
	```
	pip install cvxopt
	```
- [Conda](https://anaconda.org/conda-forge/cvxopt) (📥 1.9M · ⏱️ 13.03.2026):
	```
	conda install -c conda-forge cvxopt
	```
</details>
<details><summary><b><a href="https://www.coin-or.org/">Ipopt</a></b> (🥉25 ·  ⭐ 1.7K) - COIN-OR Interior Point Optimizer. <code><a href="http://bit.ly/2M0xmjV">EPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/coin-or/Ipopt) (👨‍💻 38 · 🔀 310 · 📥 30K · 📋 630 - 2% open · ⏱️ 06.03.2026):

	```
	git clone https://github.com/coin-or/Ipopt
	```
- [PyPi](https://pypi.org/project/ipopt) (📥 2.5K / month · 📦 10 · ⏱️ 07.04.2021):
	```
	pip install ipopt
	```
- [Conda](https://anaconda.org/conda-forge/ipopt) (📥 2.3M · ⏱️ 17.02.2026):
	```
	conda install -c conda-forge ipopt
	```
</details>
<details><summary><b><a href="https://www.coin-or.org/">CBC</a></b> (🥉25 ·  ⭐ 990) - COIN-OR Branch-and-Cut solver. <code><a href="http://bit.ly/2M0xmjV">EPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/coin-or/Cbc) (👨‍💻 35 · 🔀 140 · 📥 320K · 📋 550 - 28% open · ⏱️ 20.04.2026):

	```
	git clone https://github.com/coin-or/Cbc
	```
- [Conda](https://anaconda.org/conda-forge/coincbc) (📥 1.6M · ⏱️ 12.03.2026):
	```
	conda install -c conda-forge coincbc
	```
</details>
<details><summary><b><a href="https://www.coin-or.org/">Clp</a></b> (🥉25 ·  ⭐ 990) - COIN-OR Linear Programming Solver. <code><a href="http://bit.ly/2M0xmjV">EPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/coin-or/Cbc) (👨‍💻 35 · 🔀 140 · 📥 320K · 📋 550 - 28% open · ⏱️ 20.04.2026):

	```
	git clone https://github.com/coin-or/Cbc
	```
- [Conda](https://anaconda.org/conda-forge/coin-or-clp) (📥 1.5M · ⏱️ 12.03.2026):
	```
	conda install -c conda-forge coin-or-clp
	```
</details>
<details><summary><b><a href="https://github.com/oxfordcontrol/Clarabel.rs">Clarabel.rs</a></b> (🥉23 ·  ⭐ 560) - Interior-point solver for convex conic optimisation.. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/rust.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/oxfordcontrol/Clarabel.rs) (👨‍💻 11 · 🔀 42 · 📦 65 · 📋 67 - 25% open · ⏱️ 13.04.2026):

	```
	git clone https://github.com/oxfordcontrol/Clarabel.rs
	```
- [PyPi](https://pypi.org/project/clarabel) (📥 2.9M / month):
	```
	pip install clarabel
	```
- [Conda](https://anaconda.org/conda-forge/clarabel) (📥 370K · ⏱️ 17.12.2025):
	```
	conda install -c conda-forge clarabel
	```
</details>
<details><summary><b><a href="https://github.com/PREDICT-EPFL/piqp">PIQP</a></b> (🥉21 ·  ⭐ 140) - Proximal Interior Point Quadratic Programming solver. <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/r.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PREDICT-EPFL/piqp) (👨‍💻 6 · 🔀 21 · 📥 1.2K · 📦 52 · 📋 20 - 25% open · ⏱️ 29.03.2026):

	```
	git clone https://github.com/PREDICT-EPFL/piqp
	```
- [PyPi](https://pypi.org/project/piqp) (📥 25K / month · 📦 9 · ⏱️ 16.09.2025):
	```
	pip install piqp
	```
- [Conda](https://anaconda.org/conda-forge/piqp) (📥 310K · ⏱️ 09.01.2026):
	```
	conda install -c conda-forge piqp
	```
</details>
<details><summary><b><a href="https://ampl.com/">AMPLPY</a></b> (🥉19 ·  ⭐ 83) - Python API for AMPL. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ampl/amplpy) (👨‍💻 9 · 🔀 19 · 📦 140 · 📋 51 - 1% open · ⏱️ 16.02.2026):

	```
	git clone https://github.com/ampl/amplpy
	```
- [PyPi](https://pypi.org/project/amplpy) (📥 32K / month · 📦 11 · ⏱️ 08.12.2025):
	```
	pip install amplpy
	```
- [Conda](https://anaconda.org/conda-forge/amplpy) (📥 530K · ⏱️ 05.09.2025):
	```
	conda install -c conda-forge amplpy
	```
</details>
<details><summary><b><a href="https://github.com/oxfordcontrol/Clarabel.jl">Clarabel.jl</a></b> (🥉17 ·  ⭐ 260) - Interior-point solver for convex conic optimisation.. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/oxfordcontrol/Clarabel.jl) (👨‍💻 13 · 🔀 28 · 📋 74 - 14% open · ⏱️ 14.04.2026):

	```
	git clone https://github.com/oxfordcontrol/Clarabel.jl
	```
</details>
<details><summary><b><a href="https://github.com/MadNLP/MadNLP.jl">MadNLP</a></b> (🥉17 ·  ⭐ 240) - A solver for nonlinear programming with GPU support. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/MadNLP/MadNLP.jl) (👨‍💻 19 · 🔀 24 · 📋 140 - 21% open · ⏱️ 21.04.2026):

	```
	git clone https://github.com/MadNLP/MadNLP.jl
	```
</details>
<details><summary><b><a href="https://github.com/kvxopt/kvxopt">KVXOPT</a></b> (🥉15 ·  ⭐ 13) - CVXOPT with additional SuiteSparse wrappers. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/kvxopt/kvxopt) (👨‍💻 16 · 🔀 1 · 📥 5 · 📦 32 · ⏱️ 22.02.2026):

	```
	git clone https://github.com/sanurielf/kvxopt
	```
- [PyPi](https://pypi.org/project/kvxopt) (📥 5.4K / month):
	```
	pip install kvxopt
	```
- [Conda](https://anaconda.org/conda-forge/kvxopt) (📥 430K · ⏱️ 23.02.2026):
	```
	conda install -c conda-forge kvxopt
	```
</details>
<details><summary><b><a href="https://www.opti-verse.org/">OptiVerse</a></b> (🥉7 ·  ⭐ 12 · 💤) - A library with innovative optimization solutions. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/feyntech-opt/OptiVerse) (👨‍💻 5 · 🔀 12 · ⏱️ 15.02.2025):

	```
	git clone https://github.com/feyntech-opt/OptiVerse
	```
</details>
<details><summary>Show 1 hidden projects...</summary>

- <b><a href="https://github.com/embotech/ecos">ECOS</a></b> (🥉24 ·  ⭐ 540 · 🧊) - Conic solver for second-order cone programming. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/r.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
</details>
<br>

## Machine/Reinforcement Learning for Power Grid

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://l2rpn.chalearn.org/">Grid2Op</a></b> (🥇23 ·  ⭐ 430) - Modeling sequential decision making in power systems. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Grid2op/grid2op) (👨‍💻 32 · 🔀 140 · 📋 400 - 16% open · ⏱️ 04.02.2026):

	```
	git clone https://github.com/rte-france/Grid2Op
	```
- [PyPi](https://pypi.org/project/Grid2Op) (📥 6.2K / month):
	```
	pip install Grid2Op
	```
- [Docker Hub](https://hub.docker.com/r/bdonnot/grid2op) (📥 11K · ⭐ 1 · ⏱️ 05.07.2022):
	```
	docker pull bdonnot/grid2op
	```
</details>
<details><summary><b><a href="https://github.com/JarvisETHZ/Daline">Daline</a></b> (🥉6 ·  ⭐ 25) - A Data-driven Power Flow Linearization Toolbox. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/JarvisETHZ/Daline) (📥 6 · ⏱️ 29.01.2026):

	```
	git clone https://github.com/JarvisETHZ/Daline
	```
</details>
<details><summary>Show 2 hidden projects...</summary>

- <b><a href="https://github.com/RLGC-Project/RLGC">RLGC</a></b> (🥈9 ·  ⭐ 140 · 🧊) - RL for Grid Control (RLGC). <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://github.com/cuihantao/andes_gym">andes_gym</a></b> (🥉4 ·  ⭐ 14 · 🧊) - ANDES RL Environment for OpenAI Gym. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
</details>
<br>

## Visualization

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://www.powsybl.org">PowSyBl Diagram</a></b> (🥇19 ·  ⭐ 110) - single-line substation diagrams and network graph.. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/powsybl/powsybl-diagram) (👨‍💻 36 · 🔀 22 · 📦 33 · 📋 200 - 32% open · ⏱️ 20.04.2026):

	```
	git clone https://github.com/powsybl/powsybl-diagram
	```
</details>
<details><summary><b><a href="https://www.nlr.gov/analysis/sienna">PowerGraphics.jl</a></b> (🥉14 ·  ⭐ 33) - Visualization for PowerSimulations; NREL Sienna. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Sienna-Platform/PowerGraphics.jl) (👨‍💻 12 · 🔀 17 · 📋 42 - 42% open · ⏱️ 21.04.2026):

	```
	git clone https://github.com/NREL-Sienna/powergraphics.jl
	```
</details>
<details><summary><b><a href="https://ltb.curent.org/">LTB AGVis</a></b> (🥉10 ·  ⭐ 9) - Geographical Visualization for Power Grid; CURENT LTB. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CURENT/agvis) (👨‍💻 12 · 🔀 6 · 📥 18 · 📦 3 · 📋 25 - 36% open · ⏱️ 09.03.2026):

	```
	git clone https://github.com/CURENT/agvis
	```
- [PyPi](https://pypi.org/project/agvis) (📥 33 / month):
	```
	pip install agvis
	```
</details>
<br>

## Messaging Environment

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://helics.org/tools/">HELICS</a></b> (🥇23 ·  ⭐ 160) - Co-simulation framework. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/GMLC-TDC/HELICS) (👨‍💻 39 · 🔀 52 · 📥 32K · 📋 680 - 14% open · ⏱️ 16.08.2025):

	```
	git clone https://github.com/GMLC-TDC/HELICS
	```
- [PyPi](https://pypi.org/project/helics) (📥 5.5K / month · 📦 13 · ⏱️ 28.02.2025):
	```
	pip install helics
	```
- [Conda](https://anaconda.org/conda-forge/helics) (📥 22K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge helics
	```
</details>
<details><summary>Show 1 hidden projects...</summary>

- <b><a href="https://ltb.curent.org/">LTB DiME</a></b> (🥉7 ·  ⭐ 3 · 🧊) - Distributed Messaging Environment; CURENT LTB. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
</details>
<br>

## Power System Data

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

🔗&nbsp;<b><a href="https://github.com/Team-Nando/MV-LV-Networks">Australian MV-LV Networks</a></b> ( ⭐ 30 · 🧊)  - Large-scale three-phase Australian MV distribution.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://power-grid-lib.github.io">Power Grid Lib - Optimal Power Flow</a></b> ( ⭐ 400 · 🧊)  - Benchmarks for OPF. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://power-grid-lib.github.io">Power Grid Lib - Unit Commitment</a></b> ( ⭐ 120)  - Benchmarks for UC. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://power-grid-lib.github.io">Power Grid Lib - Optimal Power Flow with HVDC Lines</a></b> ( ⭐ 25 · 🧊)  - Benchmarks for OPF with HVDC. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/enliten/ENLITEN-Grid-Econ-Data">WECC-and-NPCC-Electricity-Economic-Data</a></b> ( ⭐ 14 · 💤)  - Economic data on WECC and NPCC. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://opendata.elia.be/pages/home/">OpenDataElia</a></b>  - Data by opendatasoft. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/owid/energy-data">Data on Energy</a></b> ( ⭐ 400)  - Data on energy by Our World in Data. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/tamu-engineering-research/COVID-EMDA">COVID-EMDA</a></b> ( ⭐ 60 · 💤)  - Cross-Domain Data Hub with Data in USA. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/rte-france/digital-fault-recording-database">Electrical Signals Databases</a></b> ( ⭐ 32 · 💤)  - Voltage and current samples from Digital Fault.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/lbl-hub/CSEE-Benchmark">A new power system benchmark</a></b> ( ⭐ 40)  - A new type of power system calculation example by the.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/NanpengYu/pmuBAGE">pmuBAGE</a></b> ( ⭐ 9 · 🧊)  - Synthetic phasor measurement unit dataset. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

<details><summary><b><a href="https://www.gridstatus.io">GridStatus</a></b> (🥇26 ·  ⭐ 410) - Extract data from ISOs and other sources. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/gridstatus/gridstatus) (👨‍💻 40 · 🔀 75 · 📦 27 · 📋 140 - 33% open · ⏱️ 23.04.2026):

	```
	git clone https://github.com/kmax12/gridstatus
	```
- [PyPi](https://pypi.org/project/gridstatus) (📥 110K / month · 📦 2 · ⏱️ 21.04.2026):
	```
	pip install gridstatus
	```
- [Conda](https://anaconda.org/services/gridstatus) (📥 40 · ⏱️ 25.03.2025):
	```
	conda install -c services gridstatus
	```
</details>
<details><summary><b><a href="https://pypsa.org">Atlite</a></b> (🥈24 ·  ⭐ 380) - Calculating Renewable Power Potentials. <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/atlite) (👨‍💻 45 · 🔀 130 · 📦 120 · 📋 170 - 32% open · ⏱️ 21.04.2026):

	```
	git clone https://github.com/PyPSA/atlite
	```
- [PyPi](https://pypi.org/project/atlite) (📥 4.6K / month · 📦 2 · ⏱️ 21.04.2026):
	```
	pip install atlite
	```
- [Conda](https://anaconda.org/conda-forge/atlite) (📥 140K · ⏱️ 21.04.2026):
	```
	conda install -c conda-forge atlite
	```
</details>
<details><summary><b><a href="https://pypsa.org">powerplantmatching</a></b> (🥈23 ·  ⭐ 220) - Tools to combine multiple power plant databases. <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/powerplantmatching) (👨‍💻 36 · 🔀 73 · 📥 87 · 📦 86 · 📋 120 - 22% open · ⏱️ 21.04.2026):

	```
	git clone https://github.com/PyPSA/powerplantmatching
	```
- [PyPi](https://pypi.org/project/powerplantmatching) (📥 1.5K / month · ⏱️ 11.02.2026):
	```
	pip install powerplantmatching
	```
- [Conda](https://anaconda.org/conda-forge/powerplantmatching) (📥 130K · ⏱️ 11.02.2026):
	```
	conda install -c conda-forge powerplantmatching
	```
</details>
<details><summary><b><a href="https://simbench.de/en/">SimBench</a></b> (🥈22 ·  ⭐ 130) - Benchmark dataset of German LV/MV/HV grids including.. <code><a href="https://tldrlegal.com/search?q=odbl-1.0">❗️odbl-1.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/e2nIEE/simbench) (👨‍💻 6 · 🔀 36 · 📦 50 · 📋 37 - 13% open · ⏱️ 02.04.2026):

	```
	git clone https://github.com/e2nIEE/simbench
	```
- [PyPi](https://pypi.org/project/simbench) (📥 8.3K / month · 📦 15 · ⏱️ 02.04.2026):
	```
	pip install simbench
	```
- [Conda](https://anaconda.org/conda-forge/simbench):
	```
	conda install -c conda-forge simbench
	```
</details>
<details><summary><b><a href="https://groups.io/g/powergenome">PowerGenome</a></b> (🥉16 ·  ⭐ 230) - Create inputs for power systems models. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PowerGenome/PowerGenome) (👨‍💻 18 · 🔀 73 · 📋 200 - 49% open · ⏱️ 13.02.2026):

	```
	git clone https://github.com/PowerGenome/PowerGenome
	```
- [PyPi](https://pypi.org/project/PowerGenome) (📥 68 / month · ⏱️ 21.03.2025):
	```
	pip install PowerGenome
	```
- [Conda](https://anaconda.org/conda-forge/powergenome) (📥 1.5K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge powergenome
	```
</details>
<details><summary><b><a href="https://github.com/GridMod/RTS-GMLC">RTS-GMLC</a></b> (🥉15 ·  ⭐ 230) - Reliability Test System dataset for Grid.. <code><a href="https://tldrlegal.com/search?q=DOE/NREL/ALLIANCE%20data%20use%20disclaimer%20agreement">❗️DOE/NREL/ALLIANCE data use disclaimer agreement</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/GridMod/RTS-GMLC) (👨‍💻 31 · 🔀 95 · 📋 120 - 20% open · ⏱️ 23.10.2025):

	```
	git clone https://github.com/GridMod/RTS-GMLC
	```
</details>
<details><summary><b><a href="https://www.energydatamodel.org/">EnergyDataModel</a></b> (🥉13 ·  ⭐ 74) - Represent energy systems as Python data classes. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/rebase-energy/EnergyDataModel) (👨‍💻 6 · 🔀 6 · ⏱️ 22.04.2026):

	```
	git clone https://github.com/rebase-energy/EnergyDataModel
	```
- [PyPi](https://pypi.org/project/energydatamodel) (📥 84 / month · 📦 2 · ⏱️ 05.10.2025):
	```
	pip install energydatamodel
	```
</details>
<details><summary><b><a href="https://github.com/cuihantao/PowerDynData.jl">PowerDynData.jl</a></b> (🥉6 ·  ⭐ 2 · 🐣) - Julia package for parsing PSS/E DYR dynamic data files. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cuihantao/PowerDynData.jl) (👨‍💻 4 · 🔀 1 · ⏱️ 04.01.2026):

	```
	git clone https://github.com/cuihantao/PowerDynData.jl
	```
</details>
<details><summary><b><a href="https://github.com/cuihantao/PowerfulCases">PowerfulCases</a></b> (🥉5 ·  ⭐ 3 · 🐣) - Test case data management for power systems simulation. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cuihantao/PowerfulCases) (⏱️ 19.01.2026):

	```
	git clone https://github.com/cuihantao/PowerfulCases
	```
- [PyPi](https://pypi.org/project/powerfulcases) (📥 12 / month):
	```
	pip install powerfulcases
	```
</details>
<details><summary>Show 1 hidden projects...</summary>

- <b><a href="https://deepsolar.web.app">DeepSolar</a></b> (🥉9 ·  ⭐ 270 · 🧊) - Houseshold-level solar panel identification with deep.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
</details>
<br>

## Power Electronics

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<br>

## Database Management

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/dsgrid/dsgrid">dsgrid</a></b> (🥇18 ·  ⭐ 33) - Demand-side grid projects, datasets and queries. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dsgrid/dsgrid) (👨‍💻 6 · 🔀 6 · 📦 1 · 📋 150 - 42% open · ⏱️ 31.03.2026):

	```
	git clone https://github.com/dsgrid/dsgrid
	```
- [PyPi](https://pypi.org/project/dsgrid) (📥 42 / month):
	```
	pip install dsgrid
	```
</details>
<details><summary><b><a href="https://github.com/NatLabRockies/dgen">dGen</a></b> (🥉15 ·  ⭐ 74) - The Distributed Generation Market Demand (dGen) model. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NatLabRockies/dgen) (👨‍💻 14 · 🔀 170 · 📋 45 - 53% open · ⏱️ 17.02.2026):

	```
	git clone https://github.com/NatLabRockies/dgen
	```
</details>
<br>

## Textbook

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

🔗&nbsp;<b><a href="https://powercybertraining.github.io">PowerCyber Training</a></b> ( ⭐ 11)  - PowerCyber Training modules source. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/Power-Systems-Textbook/TextbookSimulations">TextbookSimulations</a></b> ( ⭐ 12 · 🧊)  - Examples and problems accompanying Daniel Kirschens.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/CURENT/ece522">UTK ECE 522 - Power System Analysis II</a></b> ( ⭐ 6)  - Hands-on Project for Power System Analysis II (UTK.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/bcornelusse/ELEC0447-analysis-power-systems">ELEC0447 Analysis of Electric Power and Energy Systems</a></b> ( ⭐ 23)  - Masters course of power systems analysis at ULige. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/Team-Nando/Tutorial-DERHostingCapacity-0-dss_python">Tutorial on DER Hosting Capacity Part 0</a></b> ( ⭐ 6 · 💤)  - Using dss_python. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/Team-Nando/Tutorial-DERHostingCapacity-1-AdvancedTools_LV">Tutorial on DER Hosting Capacity Part 1</a></b> ( ⭐ 5 · 💤)  - Advanced Tools for the Analysis of Three-Phase.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/Team-Nando/Tutorial-DERHostingCapacity-2-TimeSeries_LV">Tutorial on DER Hosting Capacity Part 2</a></b> ( ⭐ 2 · 💤)  - Time-Series Analysis and PV Hosting Capacity of LV.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/Team-Nando/Tutorial-DERHostingCapacity-3-VoltWatt_LV">Tutorial on DER Hosting Capacity Part 3</a></b> ( ⭐ 1 · 💤)  - Volt-Watt Control and PV Hosting Capacity of LV.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/Team-Nando/Tutorial-DERHostingCapacity-4-MonteCarlo_MV-LV">Tutorial on DER Hosting Capacity Part 4</a></b> ( ⭐ 2 · 💤)  - Monte Carlo Assessment of PV Hosting Capacity of an.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://ltb.curent.org">LTB Demo</a></b> ( ⭐ 4)  - Ready-to-use LTB usage examples. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

<details><summary><b><a href="https://colib.net/">COLIB</a></b> (🥇7 ·  ⭐ 14) - Collaborative dynamic library. <code><a href="https://tldrlegal.com/search?q=CC-BY-4.0">❗️CC-BY-4.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CRESYM/colib0.github.io) (👨‍💻 12 · 🔀 4 · 📋 130 - 9% open · ⏱️ 12.05.2025):

	```
	git clone https://github.com/CRESYM/colib0.github.io
	```
</details>
<br>

## Large Language Model

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/open-energy-transition/pypsa-mcp">PyPSA MCP</a></b> (🥇12 ·  ⭐ 49) - PyPSA Energy Modeling for LLMs. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/open-energy-transition/pypsa-mcp) (👨‍💻 2 · 🔀 6 · 📥 5 · ⏱️ 20.03.2026):

	```
	git clone https://github.com/cdgaete/pypsa-mcp
	```
- [PyPi](https://pypi.org/project/pypsamcp) (📥 66 / month · ⏱️ 20.03.2026):
	```
	pip install pypsamcp
	```
</details>
<details><summary><b><a href="http://poweragent.seas.harvard.edu/">PowerMCP</a></b> (🥈10 ·  ⭐ 110) - Collection of MCP servers for power system software. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Power-Agent/PowerMCP) (👨‍💻 12 · 🔀 36 · 📋 2 - 50% open · ⏱️ 18.04.2026):

	```
	git clone https://github.com/Power-Agent/PowerMCP
	```
</details>
<details><summary><b><a href="https://ltb.curent.org/">P-V Curve LLM</a></b> (🥉8 ·  ⭐ 4) - Using LLMs in Power-Voltage Curves for Voltage Stability.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CURENT/pv-curve-llm) (👨‍💻 6 · 🔀 1 · ⏱️ 16.04.2026):

	```
	git clone https://github.com/CURENT/pv-curve-llm
	```
</details>
<details><summary><b><a href="http://poweragent.seas.harvard.edu/">PowerFM</a></b> (🥉6 ·  ⭐ 39) - Foundation models in the power and energy domain. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Power-Agent/PowerFM) (🔀 3 · ⏱️ 28.02.2026):

	```
	git clone https://github.com/Power-Agent/PowerFM
	```
</details>
<details><summary><b><a href="http://poweragent.seas.harvard.edu/">PowerWorkflow</a></b> (🥉6 ·  ⭐ 30) - Collection of agentic workflows for power system.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Power-Agent/PowerWF) (🔀 1 · ⏱️ 19.07.2025):

	```
	git clone https://github.com/Power-Agent/PowerWF
	```
</details>


---

## Project Popularity Score

- Has homepage link & description: `+ 1`
- Has an existing GitHub repository: `+ 1`
- Has a license: `+ 1`
- Has a commonly used license (e.g. MIT): `+ 1`
- Has multiple releases: `+ 1`
- Has stable releases based on semantic version: `+ 1`
- Has a release that is less than 6 months old: `+ 1`
- Repo was update in the last 3 months: `+ 1`
- Is older than 6 months: `+ 1`
- Metrics from GitHub & package mangers:
  - Number of stars: `+ log(COUNT / 2)`
  - Number of contributors: `+ log(COUNT / 2) - 1`
  - Number of commits: `+ log(COUNT / 2) - 1`
  - Number of forks: `+ log(COUNT / 2)`
  - Number of monthly downloads: `+ log(COUNT / 2) - 1`
  - Number of dependent projects: `+ log(COUNT / 1.5)`
  - Number of watchers: `+ log(COUNT / 2) - 1`
  - Number of closed issues: `+ log(COUNT / 2) - 1`

**NOTE**: This calculation is just chosen by ***EXPERIENCE***. There is ***NO*** scientific proof that this really reflects the ***QUALITY*** of a project.

## Project Data Collection

The data collection can be deficient for the projects that are not majorly hosted in GitHub.

## Related Resources

- [HIFLD Open](https://hifld-geoplatform.hub.arcgis.com/pages/hifld-open): Public domain data for community preparedness, resiliency, research, and more
- [FNET/GridEye Web Display](https://fnetpublic.utk.edu/): A low-cost, quickly deployable GPS-synchronized wide-area frequency measurement network
- [Grid Event Signature Library](https://gesl.ornl.gov/): An initiative spearheaded by ORNL and LLNL
- [Electric Grid Test Cases by TAMU](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/): The power system test cases on this page are do not contain Critical Energy Infrastructure Information (CEII) and are provided in a variety of different formats, including PowerWorld Simulator and PowerWorld DS (*.pwb, *.pwd, *.tsb, *.aux), Matpower (*.m), PSSE (*.raw, *.dyr), and PSLF (*.epc, *.dyd).
- [Energy Systems Datasets](https://ieee-pes-data-sharing.org/datasets): a platform provides comprehensive datasets for energy systems research and development, by IEEE Task Force on Data Sharing in Energy Systems
- [Electricity Map Data](https://portal.electricitymaps.com/datasets)
- [Der-CAM](https://dercam-app.lbl.gov/): Distributed Energy Resources Customer Adoption Model for DER investment planning
- [DOME](http://faraday1.ucd.ie/dome.html): A power system analysis tool, entirely based on Python as well as on public domain efficient C and Fortran libraries, by Prof. Federico Milano.
- [MatDyn](https://www.esat.kuleuven.be/electa/teaching/matdyn/): A free Matlab based open source program to perform dynamic analysis of electric power systems
- [G-PST Tools Portal](https://g-pst.github.io/tools/): An open tools portal with a classification approach
- [Open Source Software (OSS) for Electricity Market Research, Teaching, and Training](https://www2.econ.iastate.edu/tesfatsi/ElectricOSS.htm)
- [Open-Source-Power-Electronic-Tools](https://github.com/upb-lea/awesome-open-source-power-electronics)
- [PowerMatlab - Telegram Channel](https://t.me/powermatlab): matlab codes and simulation matlab files in field of power electrical engineering.

## Contribution

Contributions are encouraged and always welcome! If you like to add or update projects, choose one of the following ways:

- Open an issue by selecting one of the provided categories from the [issue page](https://github.com/ps-wiki/best-of-ps/issues/new/choose) and fill in the requested information.
- Modify the [projects.yaml](https://github.com/ps-wiki/best-of-ps/blob/main/projects.yaml) with your additions or changes, and submit a pull request. This can also be done directly via the [Github UI](https://github.com/ps-wiki/best-of-ps/edit/main/projects.yaml).

If you like to contribute to or share suggestions regarding the project metadata collection or markdown generation, please refer to the [best-of-generator](https://github.com/best-of-lists/best-of-generator) repository. If you like to create your own best-of list, we recommend to follow [this guide](https://github.com/best-of-lists/best-of/blob/main/create-best-of-list.md).

For more information on how to add or update projects, please read the [contribution guidelines](https://github.com/ps-wiki/best-of-ps/blob/main/CONTRIBUTING.md). By participating in this project, you agree to abide by its [Code of Conduct](https://github.com/ps-wiki/best-of-ps/blob/main/.github/CODE_OF_CONDUCT.md).

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
