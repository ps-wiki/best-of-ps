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
</p>

This curated list contains 170 open-source projects with a total of 57K stars grouped into 16 categories. All projects are ranked by a project-popularity score, which is calculated based on various metrics automatically collected from GitHub and different package managers. If you like to add or update projects, feel free to open an [issue](https://github.com/ps-wiki/best-of-ps/issues/new/choose), submit a [pull request](https://github.com/ps-wiki/best-of-ps/pulls), or directly edit the [projects.yaml](https://github.com/ps-wiki/best-of-ps/edit/main/projects.yaml). Contributions are very welcome!

## Contents

- [Electro-mechanical Transient Simulation](#electro-mechanical-transient-simulation) _13 projects_
- [Electro-magnetic Transient Simulation](#electro-magnetic-transient-simulation) _3 projects_
- [Steady-State Analysis and Optimization](#steady-state-analysis-and-optimization) _44 projects_
- [Software Interface](#software-interface) _23 projects_
- [Gas-Network Analysis](#gas-network-analysis) _3 projects_
- [Co-Simulation](#co-simulation) _6 projects_
- [Optimization Modeling Language](#optimization-modeling-language) _7 projects_
- [Optimization Solver](#optimization-solver) _16 projects_
- [Machine and Reinforcement Learning](#machine-and-reinforcement-learning) _5 projects_
- [Visualization](#visualization) _4 projects_
- [Messaging Environment](#messaging-environment) _1 projects_
- [Power-System Data](#power-system-data) _15 projects_
- [Power Electronics](#power-electronics) _1 projects_
- [Data Management](#data-management) _13 projects_
- [Educational Resources](#educational-resources) _11 projects_
- [Large-Language-Model Application](#large-language-model-application) _5 projects_

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
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13">&nbsp; Python substantially implements the maintained first-party core
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13">&nbsp; Julia substantially implements the maintained first-party core
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13">&nbsp; GNU Octave is a primary implementation or model-authoring language
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13">&nbsp; Java substantially implements the maintained first-party core
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13">&nbsp; C substantially implements the maintained first-party core
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13">&nbsp; C++ substantially implements the maintained first-party core
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/modelica.ico" style="display:inline;" width="13" height="13">&nbsp; Modelica is a primary implementation or model-authoring language
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/rust.ico" style="display:inline;" width="13" height="13">&nbsp; Rust substantially implements the maintained first-party core
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/r.ico" style="display:inline;" width="13" height="13">&nbsp; R is a primary implementation or model-authoring language
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13">&nbsp; The public repository contains a GitHub Actions workflow
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13">&nbsp; A university-based team is the current principal steward
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13">&nbsp; A national or government laboratory is the current principal steward
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13">&nbsp; Another non-profit organization is the current principal steward
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13">&nbsp; An independent contributor community is the current principal steward
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13">&nbsp; A commercial organization is the current principal steward

<br>

## Electro-mechanical Transient Simulation

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://ltb.curent.org/">LTB ANDES</a></b> (🥇31 ·  ⭐ 370) - Transient Stability Simulator; CURENT LTB. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CURENT/andes) (👨‍💻 29 · 🔀 160 · 📦 33 · 📋 85 - 15% open · ⏱️ 11.03.2026):

	```
	git clone https://github.com/CURENT/andes
	```
- [PyPi](https://pypi.org/project/andes) (📥 3.8K / month · 📦 4 · ⏱️ 12.03.2026):
	```
	pip install andes
	```
- [Conda](https://anaconda.org/conda-forge/andes) (📥 800K · ⏱️ 27.03.2026):
	```
	conda install -c conda-forge andes
	```
- [Docker Hub](https://hub.docker.com/r/CURENT/andes):
	```
	docker pull CURENT/andes
	```
- [Julia](https://juliahub.com/ui/Packages/General/Andes) (📥 6 / month):
	```
	import Pkg; Pkg.add("Andes")
	```
- Paper (📚 104 citations): [10.1109/TPWRS.2020.3017019](https://doi.org/10.1109/TPWRS.2020.3017019)
</details>
<details><summary><b><a href="https://www.nlr.gov/analysis/sienna">PowerSimulationsDynamics.jl</a></b> (🥇28 ·  ⭐ 220) - Dynamic Power System simulations; NREL Sienna. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Sienna-Platform/PowerSimulationsDynamics.jl) (👨‍💻 18 · 🔀 56 · 📋 150 - 35% open · ⏱️ 20.06.2026):

	```
	git clone https://github.com/Sienna-Platform/PowerSimulationsDynamics.jl
	```
- [Julia](https://juliahub.com/ui/Packages/General/PowerSimulationsDynamics) (📥 220 / month):
	```
	import Pkg; Pkg.add("PowerSimulationsDynamics")
	```
- Papers (📚 78 citations): [arXiv:2308.02921](https://arxiv.org/abs/2308.02921), [10.1109/TPWRS.2023.3303291](https://doi.org/10.1109/TPWRS.2023.3303291)
</details>
<details><summary><b><a href="https://dpsim.fein-aachen.org/">DPsim</a></b> (🥈27 ·  ⭐ 130) - Simulation for both EMT and phasor. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/sogno-platform/dpsim) (👨‍💻 43 · 🔀 83 · 📦 3 · 📋 200 - 38% open · ⏱️ 05.08.2026):

	```
	git clone https://github.com/sogno-platform/dpsim
	```
- [PyPi](https://pypi.org/project/dpsim) (⏱️ 10.12.2025):
	```
	pip install dpsim
	```
- Papers (📚 125 citations): [10.1016/j.softx.2019.100253](https://doi.org/10.1016/j.softx.2019.100253), [10.1109/OSMSES58477.2023.10089718](https://doi.org/10.1109/OSMSES58477.2023.10089718), [10.1049/tje2.12208](https://doi.org/10.1049/tje2.12208), [10.1109/OSMSES54027.2022.9769135](https://doi.org/10.1109/OSMSES54027.2022.9769135), [10.3390/en14237989](https://doi.org/10.3390/en14237989), [10.3390/en14071860](https://doi.org/10.3390/en14071860), [10.3390/en13153879](https://doi.org/10.3390/en13153879), [10.1109/ICCEP.2017.8004805](https://doi.org/10.1109/ICCEP.2017.8004805), [10.1109/EI2.2017.8245739](https://doi.org/10.1109/EI2.2017.8245739)
</details>
<details><summary><b><a href="http://dynawo.org">Dynaωo</a></b> (🥈22 ·  ⭐ 110) - C++/Modelica simulation tools for power systems. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/modelica.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dynawo/dynawo) (👨‍💻 63 · 🔀 32 · 📥 30K · 📋 1.8K - 13% open · ⏱️ 28.07.2026):

	```
	git clone https://github.com/dynawo/dynawo
	```
</details>
<details><summary><b><a href="https://github.com/changgang/steps">STEPS</a></b> (🥈20 ·  ⭐ 74) - Balanced large-scale AC-DC hybrid power system analysis. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/changgang/steps) (👨‍💻 9 · 🔀 23 · 📥 89 · 📦 7 · 📋 4 - 25% open · ⏱️ 02.02.2026):

	```
	git clone https://github.com/changgang/steps
	```
- [PyPi](https://pypi.org/project/stepspy) (📥 59 / month · ⏱️ 02.02.2026):
	```
	pip install stepspy
	```
- Papers (📚 54 citations): [10.1109/TPWRS.2020.3045102](https://doi.org/10.1109/TPWRS.2020.3045102), [10.1016/j.ijepes.2023.109509](https://doi.org/10.1016/j.ijepes.2023.109509), [10.1016/j.ijepes.2025.110651](https://doi.org/10.1016/j.ijepes.2025.110651)
</details>
<details><summary><b><a href="https://github.com/OpenIPSL/OpenIPSL">OpenIPSL</a></b> (🥉19 ·  ⭐ 110) - A Power System Library written in the Modelica. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/modelica.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/OpenIPSL/OpenIPSL) (👨‍💻 36 · 🔀 66 · 📥 520 · 📋 140 - 11% open · ⏱️ 13.04.2026):

	```
	git clone https://github.com/OpenIPSL/OpenIPSL
	```
- Paper (📚 21 citations): [10.1016/j.softx.2022.101277](https://doi.org/10.1016/j.softx.2022.101277)
</details>
<details><summary><b><a href="https://gridpack.pnnl.gov/wiki/index.php/Main_Page">GridPACK</a></b> (🥉19 ·  ⭐ 64) - High-Performance Electric Grid Simulation. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/GridOPTICS/GridPACK) (👨‍💻 58 · 🔀 24 · 📥 650 · 📋 140 - 13% open · ⏱️ 28.04.2026):

	```
	git clone https://github.com/GridOPTICS/GridPACK
	```
- Paper (📚 13 citations): [10.1177/1094342015607609](https://doi.org/10.1177/1094342015607609)
</details>
<details><summary><b><a href="https://www.epri.com/OpenDER">OpenDER</a></b> (🥉12 ·  ⭐ 73 · 💤) - Inverter-based DER simulation. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/epri-dev/OpenDER) (👨‍💻 2 · 🔀 29 · 📦 3 · ⏱️ 15.04.2025):

	```
	git clone https://github.com/epri-dev/OpenDER
	```
- [PyPi](https://pypi.org/project/opender) (📥 2.7K / month · ⏱️ 13.04.2025):
	```
	pip install opender
	```
</details>
<details><summary>Show 5 hidden projects...</summary>

- <b><a href="https://github.com/modelica-3rdparty/PowerSystems">PowerSystems</a></b> (🥉13 ·  ⭐ 79 · 🧊) - Modelica 3rd party library for electrical power.. <code><a href="https://tldrlegal.com/search?q=Modelica%20License%202">❗️Modelica License 2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/modelica.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://github.com/ANL-CEEESA/powersas.m">PowerSAS.m</a></b> (🥉9 ·  ⭐ 24 · 🧊) - Power grid analysis framework based on semi-.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="http://faraday1.ucd.ie/psat.html">PSAT</a></b> (🥉4 ·  ⭐ 17 · 🧊) - Unofficial repository of PSAT by Prof. Federico Milano. <code><a href="https://tldrlegal.com/search?q=GPL">❗️GPL</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://github.com/HuaizhiWang/matmtdc">matmtdc</a></b> (🥉4 ·  ⭐ 13 · 🧊) - Dynamic analysis of AC/DC hybrid power systems. <code><a href="https://tldrlegal.com/search?q=undefined">❗️undefined</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://sites.ecse.rpi.edu/~chowj/">PST</a></b> (🥉3 ·  ⭐ 5 · 🧊) - Unofficial repository of PST by Prof. Joe Chow. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code>
</details>
<br>

## Electro-magnetic Transient Simulation

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://eroots.tech/veragrid-gslv">VeraGrid</a></b> (🥇22 ·  ⭐ 580 · 📉) - Cross-platform power systems software, power flows,.. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/SanPen/VeraGrid) (👨‍💻 59 · 🔀 130 · 📥 62 · 📋 300 - 3% open · ⏱️ 31.07.2026):

	```
	git clone https://github.com/SanPen/VeraGrid
	```
- [PyPi](https://pypi.org/project/veragrid) (⏱️ 27.08.2025):
	```
	pip install veragrid
	```
</details>
<details><summary><b><a href="https://xyce.sandia.gov/">Xyce</a></b> (🥉14 ·  ⭐ 160) - The Xyce Parallel Electronic Simulator. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Xyce/Xyce) (👨‍💻 8 · 🔀 27 · 📥 1.2K · 📋 120 - 34% open · ⏱️ 01.06.2026):

	```
	git clone https://github.com/Xyce/Xyce
	```
- [PyPi](https://pypi.org/project/xyce) (📥 21 / month · ⏱️ 05.01.2022):
	```
	pip install xyce
	```
- [Conda](https://anaconda.org/vlsida-eda/xyce) (📥 5.1K · ⏱️ 25.03.2025):
	```
	conda install -c vlsida-eda xyce
	```
</details>
<details><summary><b><a href="https://github.com/NatLabRockies/ParaEMT_public">ParaEMT</a></b> (🥉14 ·  ⭐ 99) - Parallel EMT simulation. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NatLabRockies/ParaEMT_public) (👨‍💻 4 · 🔀 49 · 📋 6 - 83% open · ⏱️ 15.01.2026):

	```
	git clone https://github.com/NatLabRockies/ParaEMT_public
	```
- Papers (📚 33 citations): [10.1109/TPWRD.2023.3342715](https://doi.org/10.1109/TPWRD.2023.3342715), [10.1016/j.epsr.2024.110734](https://doi.org/10.1016/j.epsr.2024.110734)
</details>
<br>

## Steady-State Analysis and Optimization

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://www.pandapower.org/">pandapower</a></b> (🥇41 ·  ⭐ 1.2K · 📉) - Convenient Power System Modelling and Analysis. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/e2nIEE/pandapower) (👨‍💻 200 · 🔀 590 · 📦 590 · 📋 1.2K - 13% open · ⏱️ 06.08.2026):

	```
	git clone https://github.com/e2nIEE/pandapower
	```
- [PyPi](https://pypi.org/project/pandapower) (📦 110 · ⏱️ 08.07.2026):
	```
	pip install pandapower
	```
- [Conda](https://anaconda.org/conda-forge/pandapower) (📥 45K · ⏱️ 27.10.2025):
	```
	conda install -c conda-forge pandapower
	```
- [Docker Hub](https://hub.docker.com/r/pauldepraz/pandapowerapi) (📥 270 · ⏱️ 09.02.2021):
	```
	docker pull pauldepraz/pandapowerapi
	```
- Paper (📚 1114 citations): [10.1109/TPWRS.2018.2829021](https://doi.org/10.1109/TPWRS.2018.2829021)
</details>
<details><summary><b><a href="https://pypsa.org">PyPSA</a></b> (🥇40 ·  ⭐ 2.1K) - Python for Power System Analysis. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/PyPSA) (👨‍💻 120 · 🔀 670 · 📦 340 · 📋 630 - 23% open · ⏱️ 05.08.2026):

	```
	git clone https://github.com/PyPSA/PyPSA
	```
- [PyPi](https://pypi.org/project/pypsa) (📦 59 · ⏱️ 27.06.2026):
	```
	pip install pypsa
	```
- [Conda](https://anaconda.org/conda-forge/pypsa) (📥 270K · ⏱️ 10.07.2026):
	```
	conda install -c conda-forge pypsa
	```
- Paper (📚 529 citations): [10.5334/jors.188](https://doi.org/10.5334/jors.188)
</details>
<details><summary><b><a href="https://matpower.org/">MATPOWER</a></b> (🥇34 ·  ⭐ 580 · 📈) - Steady state power flow simulation. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/MATPOWER/matpower) (👨‍💻 23 · 🔀 180 · 📥 760K · 📋 240 - 9% open · ⏱️ 04.08.2026):

	```
	git clone https://github.com/MATPOWER/matpower
	```
- [Docker Hub](https://hub.docker.com/r/matpower/matpower) (📥 29K · ⏱️ 04.08.2026):
	```
	docker pull matpower/matpower
	```
- Paper (📚 6786 citations): [10.1109/TPWRS.2010.2051168](https://doi.org/10.1109/TPWRS.2010.2051168)
</details>
<details><summary><b><a href="rwl.github.io/PYPOWER/api/">PYPOWER</a></b> (🥇33 ·  ⭐ 410 · 📈) - Port of MATPOWER to Python. <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/rwl/PYPOWER) (👨‍💻 22 · 🔀 120 · 📦 170 · 📋 57 - 73% open · ⏱️ 01.08.2026):

	```
	git clone https://github.com/rwl/PYPOWER
	```
- [PyPi](https://pypi.org/project/PYPOWER) (📥 47K / month · 📦 23 · ⏱️ 01.08.2026):
	```
	pip install PYPOWER
	```
- [Conda](https://anaconda.org/invenia/pypower) (📥 3.2K · ⏱️ 25.03.2025):
	```
	conda install -c invenia pypower
	```
- [Docker Hub](https://hub.docker.com/r/hwanghust/pypower) (📥 50 · ⏱️ 19.05.2019):
	```
	docker pull hwanghust/pypower
	```
- Paper (📚 6786 citations): [10.1109/TPWRS.2010.2051168](https://doi.org/10.1109/TPWRS.2010.2051168)
</details>
<details><summary><b><a href="https://github.com/PowerGridModel/power-grid-model">Power Grid Model</a></b> (🥇32 ·  ⭐ 240 · 📉) - Steady-state distribution power system analysis. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PowerGridModel/power-grid-model) (👨‍💻 260 · 🔀 73 · 📥 2.1K · 📦 40 · 📋 330 - 35% open · ⏱️ 05.08.2026):

	```
	git clone https://github.com/PowerGridModel/power-grid-model
	```
- [PyPi](https://pypi.org/project/power-grid-model) (📦 15 · ⏱️ 05.08.2026):
	```
	pip install power-grid-model
	```
- [Conda](https://anaconda.org/conda-forge/power-grid-model):
	```
	conda install -c conda-forge power-grid-model
	```
- Paper (📚 8 citations): [10.1049/icp.2023.0633](https://doi.org/10.1049/icp.2023.0633)
</details>
<details><summary><b><a href="https://pypsa.org">PyPSA-Eur</a></b> (🥈29 ·  ⭐ 600) - Sector-Coupled Optimisation Model of the European Energy.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/pypsa-eur) (👨‍💻 110 · 🔀 410 · 📋 710 - 33% open · ⏱️ 03.08.2026):

	```
	git clone https://github.com/PyPSA/pypsa-eur
	```
- [Docker Hub](https://hub.docker.com/r/nimfetrisa/pypsa-eur):
	```
	docker pull nimfetrisa/pypsa-eur
	```
- Papers (📚 787 citations): [10.1016/j.esr.2018.08.012](https://doi.org/10.1016/j.esr.2018.08.012), [10.1016/j.joule.2023.06.016](https://doi.org/10.1016/j.joule.2023.06.016), [10.1016/j.joule.2022.04.016](https://doi.org/10.1016/j.joule.2022.04.016)
</details>
<details><summary><b><a href="https://www.nlr.gov/analysis/sienna">PowerSimulations.jl</a></b> (🥈29 ·  ⭐ 320) - Power Systems optimization simulation and modeling;.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Sienna-Platform/PowerSimulations.jl) (👨‍💻 57 · 🔀 86 · 📋 480 - 7% open · ⏱️ 05.08.2026):

	```
	git clone https://github.com/Sienna-Platform/PowerSimulations.jl
	```
- [Julia](https://juliahub.com/ui/Packages/General/PowerSimulations) (📥 620 / month):
	```
	import Pkg; Pkg.add("PowerSimulations")
	```
</details>
<details><summary><b><a href="https://github.com/lanl-ansi/PowerModels.jl">PowerModels.jl</a></b> (🥈28 ·  ⭐ 470) - Power Network Optimization. <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/lanl-ansi/PowerModels.jl) (👨‍💻 32 · 🔀 160 · 📋 520 - 18% open · ⏱️ 01.07.2026):

	```
	git clone https://github.com/lanl-ansi/PowerModels.jl
	```
- [Julia](https://juliahub.com/ui/Packages/General/PowerModels) (📥 2.1K / month):
	```
	import Pkg; Pkg.add("PowerModels")
	```
- Paper (📚 14 citations): [10.23919/PSCC.2018.8442948](https://doi.org/10.23919/PSCC.2018.8442948)
</details>
<details><summary><b><a href="https://pypsa-meets-earth.github.io/">PyPSA-Earth</a></b> (🥈27 ·  ⭐ 350) - Open optimisation model for study energy system.. <code><a href="http://bit.ly/3pwmjO5">❗️AGPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/pypsa-meets-earth/pypsa-earth) (👨‍💻 98 · 🔀 340 · 📋 720 - 40% open · ⏱️ 06.08.2026):

	```
	git clone https://github.com/pypsa-meets-earth/pypsa-earth
	```
- Paper (📚 74 citations): [10.1016/j.apenergy.2023.121096](https://doi.org/10.1016/j.apenergy.2023.121096)
</details>
<details><summary><b><a href="https://www.powsybl.org">PowSyBl Core</a></b> (🥈25 ·  ⭐ 180) - Framework to build power system software. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/powsybl/powsybl-core) (👨‍💻 130 · 🔀 66 · 📦 97 · 📋 820 - 32% open · ⏱️ 04.08.2026):

	```
	git clone https://github.com/powsybl/powsybl-core
	```
</details>
<details><summary><b><a href="https://github.com/IIT-EnergySystemModels/openTEPES">openTEPES</a></b> (🥈24 ·  ⭐ 56) - Open Generation, Storage, and Transmission Operation.. <code><a href="http://bit.ly/3pwmjO5">❗️AGPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/IIT-EnergySystemModels/openTEPES) (👨‍💻 10 · 🔀 28 · 📥 120 · 📋 20 - 20% open · ⏱️ 05.08.2026):

	```
	git clone https://github.com/IIT-EnergySystemModels/openTEPES
	```
- [PyPi](https://pypi.org/project/openTEPES) (📥 190 / month · ⏱️ 05.08.2026):
	```
	pip install openTEPES
	```
- Paper (📚 26 citations): [10.1016/j.softx.2022.101070](https://doi.org/10.1016/j.softx.2022.101070)
</details>
<details><summary><b><a href="https://www.nlr.gov/analysis/sienna">PowerFlows.jl</a></b> (🥈24 ·  ⭐ 30) - Collection of Power Flow solution; NREL Sienna. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Sienna-Platform/PowerFlows.jl) (👨‍💻 18 · 🔀 23 · 📋 170 - 15% open · ⏱️ 30.07.2026):

	```
	git clone https://github.com/Sienna-Platform/PowerFlows.jl
	```
- [Julia](https://juliahub.com/ui/Packages/General/PowerFlows) (📥 700 / month):
	```
	import Pkg; Pkg.add("PowerFlows")
	```
</details>
<details><summary><b><a href="https://www.nlr.gov/analysis/sienna">PowerNetworkMatrices.jl</a></b> (🥈24 ·  ⭐ 30) - Power systems matrices; NREL Sienna. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Sienna-Platform/PowerNetworkMatrices.jl) (👨‍💻 16 · 🔀 21 · 📋 130 - 25% open · ⏱️ 03.08.2026):

	```
	git clone https://github.com/Sienna-Platform/PowerNetworkMatrices.jl
	```
- [Julia](https://juliahub.com/ui/Packages/General/PowerNetworkMatrices) (📥 910 / month):
	```
	import Pkg; Pkg.add("PowerNetworkMatrices")
	```
</details>
<details><summary><b><a href="https://github.com/grid-parity-exchange/Egret">EGRET</a></b> (🥈23 ·  ⭐ 170) - Tools for Power Systems Optimization Modeling. <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/grid-parity-exchange/Egret) (👨‍💻 42 · 🔀 67 · 📋 90 - 57% open · ⏱️ 29.05.2026):

	```
	git clone https://github.com/grid-parity-exchange/Egret
	```
- Paper (📚 151 citations): [10.1287/ijoc.2019.0944](https://doi.org/10.1287/ijoc.2019.0944)
</details>
<details><summary><b><a href="https://www.gridpath.io/">GridPath</a></b> (🥈22 ·  ⭐ 140) - Power system planning and operations. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/sylvan-energy/gridpath) (👨‍💻 16 · 🔀 66 · 📥 1.4K · 📦 5 · 📋 350 - 16% open · ⏱️ 03.08.2026):

	```
	git clone https://github.com/sylvan-energy/gridpath
	```
- [PyPi](https://pypi.org/project/GridPath) (📥 890 / month · ⏱️ 03.08.2026):
	```
	pip install GridPath
	```
</details>
<details><summary><b><a href="https://matpower.org/">MOST</a></b> (🥈22 ·  ⭐ 39 · 📈) - MATPOWER Optimal Scheduling Tool. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/MATPOWER/most) (👨‍💻 2 · 🔀 14 · 📋 45 - 17% open · ⏱️ 04.08.2026):

	```
	git clone https://github.com/MATPOWER/most
	```
- Papers (📚 6998 citations): [10.1109/TPWRS.2010.2051168](https://doi.org/10.1109/TPWRS.2010.2051168), [10.1109/TSG.2013.2281001](https://doi.org/10.1109/TSG.2013.2281001)
</details>
<details><summary><b><a href="https://energy.mit.edu/genx/">GenX</a></b> (🥈21 ·  ⭐ 360) - Configurable capacity expansion model. <code><a href="http://bit.ly/2KucAZR">❗️GPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/GenXProject/GenX.jl) (👨‍💻 37 · 🔀 140 · 📋 330 - 21% open · ⏱️ 09.01.2026):

	```
	git clone https://github.com/GenXProject/GenX.jl
	```
- [Julia](https://juliahub.com/ui/Packages/General/GenX) (📥 75 / month):
	```
	import Pkg; Pkg.add("GenX")
	```
</details>
<details><summary><b><a href="https://www.gridlabd.org/">GridLAB-D</a></b> (🥈21 ·  ⭐ 220 · 💤) - Distribution power system simulator. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/gridlab-d/gridlab-d) (👨‍💻 77 · 🔀 130 · 📥 9.3K · 📋 1.6K - 26% open · ⏱️ 28.05.2025):

	```
	git clone https://github.com/gridlab-d/gridlab-d
	```
</details>
<details><summary><b><a href="https://l2rpn.chalearn.org/">LightSim2Grid</a></b> (🥈21 ·  ⭐ 71) - A fast backend for the Grid2Op. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Grid2op/lightsim2grid) (👨‍💻 9 · 🔀 15 · 📥 300 · 📦 89 · 📋 63 - 25% open · ⏱️ 21.04.2026):

	```
	git clone https://github.com/Grid2op/lightsim2grid
	```
- [PyPi](https://pypi.org/project/LightSim2Grid) (📥 21K / month · 📦 13 · ⏱️ 04.08.2026):
	```
	pip install LightSim2Grid
	```
- [Docker Hub](https://hub.docker.com/r/bdonnot/lightsim2grid) (📥 1.4K · ⏱️ 01.02.2022):
	```
	docker pull bdonnot/lightsim2grid
	```
</details>
<details><summary><b><a href="https://www.nlr.gov/reopt/">REopt</a></b> (🥉19 ·  ⭐ 120) - Renewable Energy Integration & Optimization. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NatLabRockies/REopt_API) (👨‍💻 26 · 🔀 67 · 📥 580 · 📋 86 - 51% open · ⏱️ 30.07.2026):

	```
	git clone https://github.com/NatLabRockies/REopt_API
	```
</details>
<details><summary><b><a href="https://ltb.curent.org/">LTB AMS</a></b> (🥉19 ·  ⭐ 25) - Scheduling Modeling and Simulation; CURENT LTB. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CURENT/ams) (👨‍💻 7 · 🔀 9 · 📥 160 · 📦 3 · 📋 24 - 37% open · ⏱️ 03.05.2026):

	```
	git clone https://github.com/CURENT/ams
	```
- [PyPi](https://pypi.org/project/ltbams) (📥 170 / month · ⏱️ 03.05.2026):
	```
	pip install ltbams
	```
- [Conda](https://anaconda.org/conda-forge/ltbams) (📥 38K · ⏱️ 03.05.2026):
	```
	conda install -c conda-forge ltbams
	```
- Paper (📚 9 citations): [10.1109/TSTE.2025.3528027](https://doi.org/10.1109/TSTE.2025.3528027)
</details>
<details><summary><b><a href="https://github.com/NLR-Distribution-Suite/erad">ERAD</a></b> (🥉19 ·  ⭐ 24) - Toolkit for computing resilience metrics for power.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NLR-Distribution-Suite/erad) (👨‍💻 8 · 🔀 13 · 📦 3 · ⏱️ 04.08.2026):

	```
	git clone https://github.com/NLR-Distribution-Suite/erad
	```
- [PyPi](https://pypi.org/project/NREL-erad) (📥 450 / month · ⏱️ 16.07.2026):
	```
	pip install NREL-erad
	```
- Paper: [10.21105/joss.08782](https://doi.org/10.21105/joss.08782)
</details>
<details><summary><b><a href="https://github.com/ANL-CEEESA/UnitCommitment.jl">UnitCommitment.jl</a></b> (🥉17 ·  ⭐ 150) - Optimization package for the Security-Constrained.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ANL-CEEESA/UnitCommitment.jl) (👨‍💻 7 · 🔀 36 · 📋 12 - 25% open · ⏱️ 17.07.2026):

	```
	git clone https://github.com/ANL-CEEESA/UnitCommitment.jl
	```
- [Julia](https://juliahub.com/ui/Packages/General/UnitCommitment) (📥 66 / month):
	```
	import Pkg; Pkg.add("UnitCommitment")
	```
</details>
<details><summary><b><a href="https://www.powsybl.org">Open RAO</a></b> (🥉17 ·  ⭐ 32) - Power systems coordinated capacity calculation and.. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/powsybl/powsybl-open-rao) (👨‍💻 44 · 🔀 10 · 📥 55 · 📋 280 - 26% open · ⏱️ 05.08.2026):

	```
	git clone https://github.com/powsybl/powsybl-open-rao
	```
</details>
<details><summary><b><a href="https://pypsa.org">PyPSA-USA</a></b> (🥉16 ·  ⭐ 140) - Power System Model for the United States. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/pypsa-usa) (👨‍💻 16 · 🔀 51 · 📋 400 - 26% open · ⏱️ 11.05.2026):

	```
	git clone https://github.com/PyPSA/pypsa-usa
	```
</details>
<details><summary><b><a href="https://github.com/bukhsh/oats">OATS</a></b> (🥉16 ·  ⭐ 29 · 💤) - Optimisation and Analysis Toolbox for Power Systems. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/bukhsh/oats) (👨‍💻 4 · 🔀 9 · 📦 3 · 📋 79 - 29% open · ⏱️ 11.12.2024):

	```
	git clone https://github.com/bukhsh/oats
	```
- [PyPi](https://pypi.org/project/oatspower) (📥 40 / month · 📦 1 · ⏱️ 28.01.2020):
	```
	pip install oatspower
	```
- Paper (📚 26 citations): [10.1109/TPWRS.2020.2986081](https://doi.org/10.1109/TPWRS.2020.2986081)
</details>
<details><summary><b><a href="https://github.com/NatLabRockies/dgen">dGen</a></b> (🥉15 ·  ⭐ 78) - The Distributed Generation Market Demand (dGen) model. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NatLabRockies/dgen) (👨‍💻 14 · 🔀 170 · 📋 45 - 53% open · ⏱️ 17.02.2026):

	```
	git clone https://github.com/NatLabRockies/dgen
	```
</details>
<details><summary><b><a href="https://github.com/grid-parity-exchange/Prescient">Prescient</a></b> (🥉15 ·  ⭐ 40 · 📉) - Production cost modeling for power generation and.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/grid-parity-exchange/Prescient) (👨‍💻 11 · 🔀 18 · 📦 11 · 📋 67 - 29% open · ⏱️ 29.05.2026):

	```
	git clone https://github.com/grid-parity-exchange/Prescient
	```
- [PyPi](https://pypi.org/project/gridx-prescient) (📦 5 · ⏱️ 29.05.2026):
	```
	pip install gridx-prescient
	```
</details>
<details><summary><b><a href="https://www.nlr.gov/analysis/reeds/">ReEDS</a></b> (🥉14 ·  ⭐ 34 · 🐣) - Capacity planning and dispatch model. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ReEDS-Model/ReEDS) (👨‍💻 23 · 🔀 14 · 📋 70 - 74% open · ⏱️ 06.08.2026):

	```
	git clone https://github.com/ReEDS-Model/ReEDS
	```
</details>
<details><summary><b><a href="https://github.com/LBNL-ETA/DOPER">DOPER</a></b> (🥉14 ·  ⭐ 25) - Distributed Optimal and Predictive Energy Resources. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/LBNL-ETA/DOPER) (👨‍💻 3 · 🔀 12 · ⏱️ 06.08.2026):

	```
	git clone https://github.com/LBNL-ETA/DOPER
	```
</details>
<details><summary><b><a href="https://www.gridpath.io/">ExaGO</a></b> (🥉12 ·  ⭐ 15) - Large-scale power grid optimization. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ORNL/ExaGO) (👨‍💻 35 · 🔀 7 · 📋 16 - 62% open · ⏱️ 28.05.2026):

	```
	git clone https://github.com/ORNL/ExaGO
	```
</details>
<details><summary><b><a href="https://github.com/pypsa-meets-earth/pypsa-distribution">PyPSA-Distribution</a></b> (🥉11 ·  ⭐ 31) - Multi-energy model for small scale applications in.. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/pypsa-meets-earth/pypsa-distribution) (👨‍💻 7 · 🔀 13 · 📋 35 - 71% open · ⏱️ 29.06.2026):

	```
	git clone https://github.com/pypsa-meets-earth/pypsa-distribution
	```
</details>
<details><summary><b><a href="https://www.nlr.gov/analysis/sienna">PowerSystemsInvestments.jl</a></b> (🥉10 ·  ⭐ 21) - Power Systems investment models; NREL Sienna. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Sienna-Platform/PowerSystemsInvestments.jl) (👨‍💻 4 · 🔀 12 · 📋 34 - 85% open · ⏱️ 20.06.2026):

	```
	git clone https://github.com/Sienna-Platform/PowerSystemsInvestments.jl
	```
- [Julia](https://juliahub.com/ui/Packages/General/PowerSystemsInvestments):
	```
	import Pkg; Pkg.add("PowerSystemsInvestments")
	```
</details>
<details><summary><b><a href="https://www2.econ.iastate.edu/tesfatsi/AMESMarketHome.htm">AMES - Version 5.0</a></b> (🥉7 ·  ⭐ 35) - Wholesale Power Market Test Bed. <code><a href="https://github.com/ames-market/AMES-V5.0/blob/master/LICENSE.rst">❗️Custom</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ames-market/AMES-V5.0) (👨‍💻 3 · 🔀 10 · ⏱️ 03.02.2026):

	```
	git clone https://github.com/ames-market/AMES-V5.0
	```
</details>
<details><summary><b><a href="https://github.com/ANL-CEEESA/EGRIP.jl">EGRIP.jl</a></b> (🥉7 ·  ⭐ 11 · 💤) - Julia/MATALB package for power system restoration.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ANL-CEEESA/EGRIP.jl) (👨‍💻 5 · ⏱️ 06.05.2025):

	```
	git clone https://github.com/ANL-CEEESA/EGRIP.jl
	```
- [Julia](https://juliahub.com/ui/Packages/General/EGRIP):
	```
	import Pkg; Pkg.add("EGRIP")
	```
</details>
<details><summary><b><a href="https://esca.epri.com/usregen">US-REGEN</a></b> (🥉6 ·  ⭐ 24 · 💤) - U.S. regional economy, greenhouse gas, and energy model. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/epri-dev/US-REGEN) (👨‍💻 2 · 🔀 4 · ⏱️ 27.05.2025):

	```
	git clone https://github.com/epri-dev/US-REGEN
	```
</details>
<details><summary><b><a href="https://github.com/NatLabRockies/ASSET">ASSET</a></b> (🥉6 ·  ⭐ 20 · 💤) - Assess and analyze grid strength. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NatLabRockies/ASSET) (👨‍💻 2 · 🔀 7 · ⏱️ 05.05.2025):

	```
	git clone https://github.com/NatLabRockies/ASSET
	```
- Paper: [10.1109/PESGM52009.2025.11225841](https://doi.org/10.1109/PESGM52009.2025.11225841)
</details>
<details><summary><b><a href="https://github.com/PPGS-Tools/PyPSA-stochUC">PyPSA-stochUC</a></b> (🥉5 ·  ⭐ 20 · 💤) - Stochastic unit commitment extension for PyPSA with market.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PPGS-Tools/PyPSA-stochUC) (👨‍💻 2 · 🔀 4 · ⏱️ 09.12.2024):

	```
	git clone https://github.com/PPGS-Tools/PyPSA-stochUC
	```
</details>
<details><summary><b><a href="https://github.com/ANL-CEEESA/gensas">GenSAS</a></b> (🥉4 ·  ⭐ 1) - A C++ based generalized simulation tool based on semi-.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/modelica.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ANL-CEEESA/gensas) (👨‍💻 3 · 🔀 1 · ⏱️ 05.04.2026):

	```
	git clone https://github.com/ANL-CEEESA/gensas
	```
</details>
<details><summary><b><a href="https://www.epri.com/pages/sa/opendss">OpenDSS</a></b> (🥉2) - Distribution system simulator. <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- _No project information available._</details>
<details><summary>Show 4 hidden projects...</summary>

- <b><a href="https://dss-extensions.org/">AltDSS/DSS C-API</a></b> (🥉16 ·  ⭐ 38 · 🧊) - a plain C interface to OpenDSS. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://github.com/ames-market/psst">PSST</a></b> (🥉12 ·  ⭐ 45 · 🧊) - Power System Simulation Toolbox for SCUC and SCED in.. <code><a href="https://tldrlegal.com/search?q=AMES%20License">❗️AMES License</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="http://www.msv.ei.tum.de/">hynet</a></b> (🥉11 ·  ⭐ 4 · 🧊) - Optimal power flow framework for hybrid AC/DC power systems. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://www2.econ.iastate.edu/tesfatsi/AMESMarketHome.htm">AMES (V4.0)</a></b> (🥉3 ·  ⭐ 14 · 🧊) - Agent based Modeling of Electricity Systems. <code><a href="http://bit.ly/2KucAZR">❗️GPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
</details>
<br>

## Software Interface

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://www.scipopt.org/">PySCIPOpt</a></b> (🥇37 ·  ⭐ 990) - Python interface for SCIP. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/scipopt/PySCIPOpt) (👨‍💻 91 · 🔀 280 · 📦 490 · 📋 650 - 3% open · ⏱️ 21.07.2026):

	```
	git clone https://github.com/scipopt/PySCIPOpt
	```
- [PyPi](https://pypi.org/project/PySCIPOpt) (📥 410K / month · 📦 110 · ⏱️ 16.05.2026):
	```
	pip install PySCIPOpt
	```
- [Conda](https://anaconda.org/conda-forge/pyscipopt) (📥 820K · ⏱️ 16.05.2026):
	```
	conda install -c conda-forge pyscipopt
	```
- Paper (📚 67 citations): [10.1007/978-3-319-42432-3_37](https://doi.org/10.1007/978-3-319-42432-3_37)
</details>
<details><summary><b><a href="https://www.powsybl.org">PyPowSyBl</a></b> (🥇21 ·  ⭐ 100 · 📉) - A PowSyBl and Python integration. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/powsybl/pypowsybl) (👨‍💻 48 · 🔀 26 · 📥 610 · 📋 310 - 29% open · ⏱️ 22.07.2026):

	```
	git clone https://github.com/powsybl/pypowsybl
	```
- [PyPi](https://pypi.org/project/pypowsybl) (📦 15 · ⏱️ 22.07.2026):
	```
	pip install pypowsybl
	```
</details>
<details><summary><b><a href="https://ampl.com/">AMPLPY</a></b> (🥇21 ·  ⭐ 86) - Python API for AMPL. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ampl/amplpy) (👨‍💻 9 · 🔀 20 · 📦 140 · ⏱️ 21.07.2026):

	```
	git clone https://github.com/ampl/amplpy
	```
- [PyPi](https://pypi.org/project/amplpy) (📥 32K / month · 📦 14 · ⏱️ 21.07.2026):
	```
	pip install amplpy
	```
- [Conda](https://anaconda.org/conda-forge/amplpy) (📥 570K · ⏱️ 05.09.2025):
	```
	conda install -c conda-forge amplpy
	```
</details>
<details><summary><b><a href="https://github.com/mzy2240/ESA">Easy SimAuto</a></b> (🥈20 ·  ⭐ 53) - Python interface to PowerWorld. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/mzy2240/ESA) (👨‍💻 13 · 🔀 16 · 📦 10 · 📋 100 - 18% open · ⏱️ 31.12.2025):

	```
	git clone https://github.com/mzy2240/ESA
	```
- [PyPi](https://pypi.org/project/esa) (📥 500 / month · 📦 1 · ⏱️ 05.06.2023):
	```
	pip install esa
	```
- Paper (📚 25 citations): [10.21105/joss.02289](https://doi.org/10.21105/joss.02289)
</details>
<details><summary><b><a href="https://github.com/ieeh-tu-dresden/powerfactory-tools">powerfactory-tools</a></b> (🥈19 ·  ⭐ 57) - Python toolbox for control of DIgSILENT PowerFactory. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ieeh-tu-dresden/powerfactory-tools) (👨‍💻 4 · 🔀 9 · 📥 390 · 📦 2 · 📋 200 - 7% open · ⏱️ 07.07.2026):

	```
	git clone https://github.com/ieeh-tu-dresden/powerfactory-tools
	```
- [PyPi](https://pypi.org/project/ieeh-powerfactory-tools) (📥 300 / month · ⏱️ 07.07.2026):
	```
	pip install ieeh-powerfactory-tools
	```
- Paper (📚 1 citation): [10.21105/joss.09281](https://doi.org/10.21105/joss.09281)
</details>
<details><summary><b><a href="https://github.com/PauloRadatz/py_dss_interface">py-dss-interface</a></b> (🥈19 ·  ⭐ 45) - A package for access to direct dll version of OpenDSS. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PauloRadatz/py_dss_interface) (👨‍💻 7 · 🔀 13 · 📥 43 · 📦 41 · 📋 57 - 1% open · ⏱️ 15.04.2026):

	```
	git clone https://github.com/PauloRadatz/py_dss_interface
	```
- [PyPi](https://pypi.org/project/py-dss-interface) (📥 5.2K / month · 📦 13 · ⏱️ 16.02.2026):
	```
	pip install py-dss-interface
	```
</details>
<details><summary><b><a href="https://github.com/UGM-EPSLab/matpowercaseframes">matpowercaseframes</a></b> (🥈18 ·  ⭐ 6) - Parse MATPOWER case into pandas DataFrame. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/UGM-EPSLab/matpowercaseframes) (👨‍💻 9 · 🔀 3 · 📦 43 · 📋 14 - 35% open · ⏱️ 29.06.2026):

	```
	git clone https://github.com/UGM-EPSLab/matpowercaseframes
	```
- [PyPi](https://pypi.org/project/matpowercaseframes) (📥 20K / month · 📦 11 · ⏱️ 29.06.2026):
	```
	pip install matpowercaseframes
	```
</details>
<details><summary><b><a href="https://www.nlr.gov/grid/pydss">PyDSS</a></b> (🥈17 ·  ⭐ 42) - A Python wrapper for OpenDSS. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NatLabRockies/PyDSS) (👨‍💻 24 · 🔀 29 · 📦 3 · 📋 31 - 48% open · ⏱️ 16.06.2026):

	```
	git clone https://github.com/NatLabRockies/PyDSS
	```
- [PyPi](https://pypi.org/project/pydss) (⏱️ 17.08.2011):
	```
	pip install pydss
	```
</details>
<details><summary><b><a href="https://github.com/cimug-org/CIMTool">CIMTool</a></b> (🥉16 ·  ⭐ 77) - CIMugs CIMTool for the CIM. <code><a href="https://tldrlegal.com/search?q=LGPL-2.1">❗️LGPL-2.1</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cimug-org/CIMTool) (👨‍💻 17 · 🔀 12 · 📥 3.1K · 📋 140 - 30% open · ⏱️ 22.07.2026):

	```
	git clone https://github.com/CIMug-org/CIMTool
	```
</details>
<details><summary><b><a href="https://dss-extensions.org/">OpenDSSDirect.jl</a></b> (🥉15 ·  ⭐ 30) - Cross-platform Julia interface to OpenDSS. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dss-extensions/OpenDSSDirect.jl) (👨‍💻 9 · 🔀 6 · 📋 48 - 25% open · ⏱️ 17.02.2026):

	```
	git clone https://github.com/dss-extensions/OpenDSSDirect.jl
	```
- [Julia](https://juliahub.com/ui/Packages/General/OpenDSSDirect) (📥 34 / month):
	```
	import Pkg; Pkg.add("OpenDSSDirect")
	```
</details>
<details><summary><b><a href="https://github.com/FraunhIEE-UniKassel-PowSysStability/powfacpy">powfacpy</a></b> (🥉15 ·  ⭐ 12) - Python wrapper around the DIgSILENT PowerFactory API. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/FraunhIEE-UniKassel-PowSysStability/powfacpy) (👨‍💻 2 · 🔀 6 · 📦 5 · 📋 41 - 17% open · ⏱️ 03.07.2026):

	```
	git clone https://github.com/FraunhIEE-UniKassel-PowSysStability/powfacpy
	```
- [PyPi](https://pypi.org/project/powfacpy) (📥 250 / month · ⏱️ 22.07.2026):
	```
	pip install powfacpy
	```
</details>
<details><summary><b><a href="https://github.com/yasirroni/matpower-pip">matpower-pip</a></b> (🥉13 ·  ⭐ 26) - Easy Python Access to MATPOWER. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/yasirroni/matpower-pip) (👨‍💻 2 · 🔀 3 · 📦 14 · 📋 22 - 31% open · ⏱️ 03.06.2026):

	```
	git clone https://github.com/yasirroni/matpower-pip
	```
- [PyPi](https://pypi.org/project/matpower) (📥 840 / month · 📦 2 · ⏱️ 25.02.2026):
	```
	pip install matpower
	```
</details>
<details><summary><b><a href="https://www.pscad.com/">mhi-pscad</a></b> (🥉9) - PSCAD Automation library. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [PyPi](https://pypi.org/project/mhi-pscad) (📥 7.4K / month · 📦 2 · ⏱️ 14.05.2026):
	```
	pip install mhi-pscad
	```
</details>
<details><summary><b><a href="https://github.com/cimug-org/CIMTool-Builders-Library">CIMTool-Builders-Library</a></b> (🥉8 ·  ⭐ 10) - Publically available XSLT builders. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cimug-org/CIMTool-Builders-Library) (👨‍💻 7 · 🔀 3 · ⏱️ 14.05.2026):

	```
	git clone https://github.com/CIMug-org/CIMTool-Builders-Library
	```
</details>
<details><summary><b><a href="https://dss-extensions.org/">DSS MATLAB</a></b> (🥉7 ·  ⭐ 12 · 💤) - MATLAB interface to OpenDSS. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dss-extensions/dss_matlab) (🔀 2 · 📥 1.4K · 📋 21 - 33% open · ⏱️ 30.10.2024):

	```
	git clone https://github.com/dss-extensions/dss_matlab
	```
</details>
<details><summary><b><a href="https://github.com/epri-dev/OpenDER_interface">OpenDER interface</a></b> (🥉5 ·  ⭐ 6 · 💤) - Interface for OpenDER. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/epri-dev/OpenDER_interface) (👨‍💻 2 · 🔀 2 · ⏱️ 10.02.2025):

	```
	git clone https://github.com/epri-dev/OpenDER_interface
	```
</details>
<details><summary>Show 7 hidden projects...</summary>

- <b><a href="https://dss-extensions.org/">OpenDSSDirect.py</a></b> (🥈20 ·  ⭐ 110 · 🧊) - A direct library interface to OpenDSS. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://dss-extensions.org/">AltDSS-Python</a></b> (🥉13 ·  ⭐ 18 · 🧊) - Modern Python bindings for an alternative.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://github.com/felipemarkson/dssdata">DSSData</a></b> (🥉9 ·  ⭐ 17 · 🧊) - A micro-framework for simulation and data analysis of.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://dss-extensions.org/">DSS Sharp</a></b> (🥉7 ·  ⭐ 12 · 🧊) - C#/.NET wrapper library for DSS C-API. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://ltb.curent.org">Andes.jl</a></b> (🥉6 ·  ⭐ 9 · 🧊) - Julia interface for ANDES. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://github.com/yasirroni/mypower">mypower</a></b> (🥉5 ·  ⭐ 8 · 🧊) - Supplementary function of MATPOWER in Python. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://github.com/mzy2240/EasySimauto.jl">EasySimauto.jl</a></b> (🥉4 ·  ⭐ 7 · 🧊) - Julia interface for EasySimAuto and PowerWorld. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
</details>
<br>

## Gas-Network Analysis

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://www.pandapipes.org/">pandapipes</a></b> (🥇32 ·  ⭐ 230) - Pipeflow Calculation Tool. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/e2nIEE/pandapipes) (👨‍💻 29 · 🔀 83 · 📦 42 · 📋 180 - 51% open · ⏱️ 26.05.2026):

	```
	git clone https://github.com/e2nIEE/pandapipes
	```
- [PyPi](https://pypi.org/project/pandapipes) (📥 52K / month · 📦 16 · ⏱️ 26.05.2026):
	```
	pip install pandapipes
	```
- Paper (📚 76 citations): [10.3390/su12239899](https://doi.org/10.3390/su12239899)
</details>
<details><summary><b><a href="https://github.com/lanl-ansi/GasModels.jl">GasModels.jl</a></b> (🥉21 ·  ⭐ 80) - Gas Network Optimization. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/lanl-ansi/GasModels.jl) (👨‍💻 19 · 🔀 24 · 📋 190 - 24% open · ⏱️ 30.07.2026):

	```
	git clone https://github.com/lanl-ansi/GasModels.jl
	```
- [Julia](https://juliahub.com/ui/Packages/General/GasModels) (📥 52 / month):
	```
	import Pkg; Pkg.add("GasModels")
	```
</details>
<details><summary>Show 1 hidden projects...</summary>

- <b><a href="https://matpower.org/">MPNG</a></b> (🥉11 ·  ⭐ 11 · 🧊) - Simulator for Optimal Power and Natural Gas Flow. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
</details>
<br>

## Co-Simulation

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://openmodelica.org">OpenModelica</a></b> (🥇37 ·  ⭐ 1.4K) - Modelica-based environment for modeling and simulation. <code><a href="https://tldrlegal.com/search?q=Modelica%20License%202">❗️Modelica License 2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/modelica.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/OpenModelica/OpenModelica) (👨‍💻 210 · 🔀 390 · 📥 1.8K · 📋 8.9K - 24% open · ⏱️ 06.08.2026):

	```
	git clone https://github.com/OpenModelica/OpenModelica
	```
- [Docker Hub](https://hub.docker.com/r/openmodelica/openmodelica) (📥 84K · ⭐ 6 · ⏱️ 03.07.2026):
	```
	docker pull openmodelica/openmodelica
	```
- Paper (📚 184 citations): [10.4173/mic.2020.4.1](https://doi.org/10.4173/mic.2020.4.1)
</details>
<details><summary><b><a href="https://helics.org/tools/">HELICS</a></b> (🥈33 ·  ⭐ 170) - Co-simulation framework. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/GMLC-TDC/HELICS) (👨‍💻 39 · 🔀 53 · 📥 33K · 📋 690 - 14% open · ⏱️ 06.08.2026):

	```
	git clone https://github.com/GMLC-TDC/HELICS
	```
- [PyPi](https://pypi.org/project/helics) (📥 4K / month · 📦 13 · ⏱️ 28.02.2025):
	```
	pip install helics
	```
- [Conda](https://anaconda.org/conda-forge/helics) (📥 22K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge helics
	```
- [Julia](https://juliahub.com/ui/Packages/General/HELICS) (📥 23 / month):
	```
	import Pkg; Pkg.add("HELICS")
	```
- Paper (📚 65 citations): [10.1109/ACCESS.2024.3363615](https://doi.org/10.1109/ACCESS.2024.3363615)
</details>
<details><summary><b><a href="https://precice.org/">precice</a></b> (🥈32 ·  ⭐ 960) - Precise Code Interaction Coupling Environment. <code><a href="http://bit.ly/37RvQcA">❗️LGPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/precice/precice) (👨‍💻 79 · 🔀 280 · 📥 47K · 📋 1K - 24% open · ⏱️ 22.07.2026):

	```
	git clone https://github.com/precice/precice
	```
- [PyPi](https://pypi.org/project/pyprecice) (📥 2.5K / month · 📦 10 · ⏱️ 08.04.2026):
	```
	pip install pyprecice
	```
- [Conda](https://anaconda.org/conda-forge/pyprecice) (📥 180K · ⏱️ 08.04.2026):
	```
	conda install -c conda-forge pyprecice
	```
- [Docker Hub](https://hub.docker.com/r/precice/precice) (📥 47K · ⏱️ 06.08.2026):
	```
	docker pull precice/precice
	```
- Paper (📚 46 citations): [10.12688/openreseurope.14445.2](https://doi.org/10.12688/openreseurope.14445.2)
</details>
<details><summary><b><a href="https://github.com/pnnl/tesp">TESP</a></b> (🥉16 ·  ⭐ 49) - Transactive Energy Simulation Platform. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/pnnl/tesp) (👨‍💻 31 · 🔀 42 · 📥 530 · 📦 2 · 📋 130 - 27% open · ⏱️ 05.02.2026):

	```
	git clone https://github.com/pnnl/tesp
	```
- [PyPi](https://pypi.org/project/tesp_support) (⏱️ 05.02.2026):
	```
	pip install tesp_support
	```
</details>
<details><summary>Show 2 hidden projects...</summary>

- <b><a href="https://github.com/ebalogun01/EV-EcoSim">EV-EcoSim</a></b> (🥉14 ·  ⭐ 26 · 🧊) - A grid-aware co-simulation platform for the design.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://github.com/OpenHybridSim/OpenHybridSim-code">OpenHybridSim</a></b> (🥉12 ·  ⭐ 8 · 🧊) - EMT-TS hybrid simulation. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
</details>
<br>

## Optimization Modeling Language

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://www.pyomo.org">Pyomo</a></b> (🥇49 ·  ⭐ 2.5K) - Python-based Optimization Modeling Language. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Pyomo/pyomo) (👨‍💻 200 · 🔀 580 · 📥 6.9K · 📦 4.9K · 📋 1.5K - 22% open · ⏱️ 13.07.2026):

	```
	git clone https://github.com/Pyomo/pyomo
	```
- [PyPi](https://pypi.org/project/Pyomo) (📥 1.4M / month · 📦 230 · ⏱️ 04.06.2026):
	```
	pip install Pyomo
	```
- [Conda](https://anaconda.org/conda-forge/pyomo) (📥 2.5M · ⏱️ 05.06.2026):
	```
	conda install -c conda-forge pyomo
	```
- Paper (📚 793 citations): [10.1007/978-3-030-68928-5](https://doi.org/10.1007/978-3-030-68928-5)
</details>
<details><summary><b><a href="https://github.com/cvxpy/cvxpy">CVXPY</a></b> (🥈46 ·  ⭐ 6.3K) - Convex optimization modeling language. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cvxpy/cvxpy) (👨‍💻 260 · 🔀 1.2K · 📥 830 · 📦 19K · 📋 1.7K - 11% open · ⏱️ 04.08.2026):

	```
	git clone https://github.com/cvxpy/cvxpy
	```
- [PyPi](https://pypi.org/project/cvxpy) (📥 5.3M / month · 📦 1K · ⏱️ 22.06.2026):
	```
	pip install cvxpy
	```
- [Conda](https://anaconda.org/conda-forge/cvxpy) (📥 2.2M · ⏱️ 10.07.2026):
	```
	conda install -c conda-forge cvxpy
	```
- Paper (📚 38 citations): [10.1080/23307706.2017.1397554](https://doi.org/10.1080/23307706.2017.1397554)
</details>
<details><summary><b><a href="https://jump.dev">JuMP</a></b> (🥈41 ·  ⭐ 2.5K) - Julia-based Optimization Modeling Language. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/jump-dev/JuMP.jl) (👨‍💻 170 · 🔀 420 · 📋 1.5K - 1% open · ⏱️ 29.07.2026):

	```
	git clone https://github.com/jump-dev/JuMP.jl
	```
- [Julia](https://juliahub.com/ui/Packages/General/JuMP) (📥 30K / month):
	```
	import Pkg; Pkg.add("JuMP")
	```
- Paper (📚 334 citations): [10.1007/s12532-023-00239-3](https://doi.org/10.1007/s12532-023-00239-3)
</details>
<details><summary><b><a href="https://github.com/exanauts/ExaModels.jl">ExaModels</a></b> (🥉26 ·  ⭐ 80 · 📈) - An algebraic modeling and automatic differentiation.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/exanauts/ExaModels.jl) (👨‍💻 14 · 🔀 12 · 📋 55 - 18% open · ⏱️ 03.08.2026):

	```
	git clone https://github.com/exanauts/ExaModels.jl
	```
- [Julia](https://juliahub.com/ui/Packages/General/ExaModels) (📥 480 / month):
	```
	import Pkg; Pkg.add("ExaModels")
	```
- Paper (📚 29 citations): [10.1016/j.epsr.2024.110651](https://doi.org/10.1016/j.epsr.2024.110651)
</details>
<details><summary><b><a href="https://github.com/XiongPengNUS/rsome">RSOME</a></b> (🥉24 ·  ⭐ 350 · 💤) - Robust Stochastic Optimization Made Easy. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/XiongPengNUS/rsome) (👨‍💻 3 · 🔀 62 · 📋 45 - 15% open · ⏱️ 15.11.2024):

	```
	git clone https://github.com/XiongPengNUS/rsome
	```
- [PyPi](https://pypi.org/project/rsome) (📥 600 / month · 📦 4 · ⏱️ 29.10.2024):
	```
	pip install rsome
	```
- Papers (📚 261 citations): [10.1287/ijoc.2023.1291](https://doi.org/10.1287/ijoc.2023.1291), [10.1287/mnsc.2020.3603](https://doi.org/10.1287/mnsc.2020.3603)
</details>
<details><summary><b><a href="https://github.com/metab0t/PyOptInterface">PyOptInterface</a></b> (🥉24 ·  ⭐ 310) - Efficient modeling interface for optimization in.. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/metab0t/PyOptInterface) (👨‍💻 8 · 🔀 28 · 📦 23 · 📋 48 - 22% open · ⏱️ 22.07.2026):

	```
	git clone https://github.com/metab0t/PyOptInterface
	```
- [PyPi](https://pypi.org/project/pyoptinterface) (📥 12K / month · 📦 8 · ⏱️ 27.03.2026):
	```
	pip install pyoptinterface
	```
- Paper (📚 4 citations): [10.1109/TPWRS.2024.3483489](https://doi.org/10.1109/TPWRS.2024.3483489)
</details>
<details><summary><b><a href="https://www.gurobi.com/features/gurobi-optimods/">Gurobi OptiMods</a></b> (🥉19 ·  ⭐ 180) - Implemented optimization use cases using Gurobi. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Gurobi/gurobi-optimods) (👨‍💻 17 · 🔀 38 · 📦 10 · 📋 87 - 28% open · ⏱️ 09.04.2026):

	```
	git clone https://github.com/Gurobi/gurobi-optimods
	```
- [PyPi](https://pypi.org/project/gurobi-optimods) (📥 370 / month · 📦 2 · ⏱️ 09.04.2026):
	```
	pip install gurobi-optimods
	```
</details>
<br>

## Optimization Solver

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://highs.dev/">HiGHS</a></b> (🥇52 ·  ⭐ 1.8K) - Large-scale Sparse Linear Problem Optimizer. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ERGO-Code/HiGHS) (👨‍💻 120 · 🔀 330 · 📥 79K · 📋 1.2K - 13% open · ⏱️ 06.08.2026):

	```
	git clone https://github.com/ERGO-Code/HiGHS
	```
- [PyPi](https://pypi.org/project/highspy) (📥 3.7M / month · 📦 210 · ⏱️ 02.07.2026):
	```
	pip install highspy
	```
- [Conda](https://anaconda.org/conda-forge/highs) (📥 100K · ⏱️ 10.07.2026):
	```
	conda install -c conda-forge highs
	```
- [Julia](https://juliahub.com/ui/Packages/General/HiGHS) (📥 15K / month):
	```
	import Pkg; Pkg.add("HiGHS")
	```
- Paper (📚 364 citations): [10.1007/s12532-017-0130-5](https://doi.org/10.1007/s12532-017-0130-5)
</details>
<details><summary><b><a href="https://osqp.org">OSQP</a></b> (🥇48 ·  ⭐ 2.2K) - Operator Splitting QP Solver. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/osqp/osqp) (👨‍💻 36 · 🔀 410 · 📥 220K · 📋 400 - 30% open · ⏱️ 10.11.2025):

	```
	git clone https://github.com/osqp/osqp
	```
- [PyPi](https://pypi.org/project/osqp) (📥 5.5M / month · 📦 170 · ⏱️ 12.06.2026):
	```
	pip install osqp
	```
- [Conda](https://anaconda.org/conda-forge/osqp) (📥 1.6M · ⏱️ 13.06.2026):
	```
	conda install -c conda-forge osqp
	```
- [Julia](https://juliahub.com/ui/Packages/General/OSQP) (📥 960 / month):
	```
	import Pkg; Pkg.add("OSQP")
	```
- Paper (📚 1165 citations): [10.1007/s12532-020-00179-2](https://doi.org/10.1007/s12532-020-00179-2)
</details>
<details><summary><b><a href="https://github.com/cvxgrp/scs">SCS</a></b> (🥈45 ·  ⭐ 630) - Splitting Conic Solver. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cvxgrp/scs) (👨‍💻 32 · 🔀 140 · 📋 190 - 22% open · ⏱️ 28.06.2026):

	```
	git clone https://github.com/cvxgrp/scs
	```
- [PyPi](https://pypi.org/project/scs) (📥 4.2M / month · 📦 72 · ⏱️ 09.01.2026):
	```
	pip install scs
	```
- [Conda](https://anaconda.org/conda-forge/scs) (📥 1.9M · ⏱️ 12.05.2026):
	```
	conda install -c conda-forge scs
	```
- [Julia](https://juliahub.com/ui/Packages/General/SCS) (📥 6.4K / month):
	```
	import Pkg; Pkg.add("SCS")
	```
- Paper (📚 608 citations): [10.1007/s10957-016-0892-3](https://doi.org/10.1007/s10957-016-0892-3)
</details>
<details><summary><b><a href="https://developers.google.com/optimization/">OR-Tools</a></b> (🥈37 ·  ⭐ 14K) - Google Optimization Tools. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/google/or-tools) (👨‍💻 200 · 🔀 2.5K · 📥 460K · 📦 370 · 📋 3.2K - 3% open · ⏱️ 09.06.2026):

	```
	git clone https://github.com/google/or-tools
	```
- [PyPi](https://pypi.org/project/ortools) (📥 6.6M / month · 📦 390 · ⏱️ 14.01.2026):
	```
	pip install ortools
	```
- [Conda](https://anaconda.org/conda-forge/ortools-python) (📥 170K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge ortools-python
	```
</details>
<details><summary><b><a href="https://www.coin-or.org/">Ipopt</a></b> (🥈34 ·  ⭐ 1.8K) - COIN-OR Interior Point Optimizer. <code><a href="http://bit.ly/2M0xmjV">EPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/coin-or/Ipopt) (👨‍💻 38 · 🔀 320 · 📥 35K · 📋 630 - 2% open · ⏱️ 25.05.2026):

	```
	git clone https://github.com/coin-or/Ipopt
	```
- [PyPi](https://pypi.org/project/ipopt) (📥 2.3K / month · 📦 10 · ⏱️ 07.04.2021):
	```
	pip install ipopt
	```
- [Conda](https://anaconda.org/conda-forge/ipopt) (📥 2.8M · ⏱️ 17.02.2026):
	```
	conda install -c conda-forge ipopt
	```
- Paper (📚 9539 citations): [10.1007/s10107-004-0559-y](https://doi.org/10.1007/s10107-004-0559-y)
</details>
<details><summary><b><a href="https://cvxopt.org/">CVXOPT</a></b> (🥈28 ·  ⭐ 1K) - Python Software for Convex Optimization. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cvxopt/cvxopt) (👨‍💻 10 · 🔀 220 · 📦 15K · 📋 200 - 21% open · ⏱️ 02.03.2026):

	```
	git clone https://github.com/cvxopt/cvxopt
	```
- [PyPi](https://pypi.org/project/cvxopt) (📥 1.2M / month · 📦 480 · ⏱️ 09.02.2026):
	```
	pip install cvxopt
	```
- [Conda](https://anaconda.org/conda-forge/cvxopt) (📥 2.2M · ⏱️ 01.08.2026):
	```
	conda install -c conda-forge cvxopt
	```
</details>
<details><summary><b><a href="https://github.com/xopt-org/Xopt">Xopt</a></b> (🥈28 ·  ⭐ 94 · 📈) - Flexible high-level optimization in Python. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/xopt-org/Xopt) (👨‍💻 28 · 🔀 39 · 📦 28 · 📋 100 - 19% open · ⏱️ 31.07.2026):

	```
	git clone https://github.com/xopt-org/Xopt
	```
- [PyPi](https://pypi.org/project/xopt) (📥 5.7K / month · 📦 12 · ⏱️ 31.07.2026):
	```
	pip install xopt
	```
- [Conda](https://anaconda.org/conda-forge/xopt) (📥 92K · ⏱️ 01.08.2026):
	```
	conda install -c conda-forge xopt
	```
- Paper (📚 9 citations): [10.18429/JACoW-IPAC2023-THPL164](https://doi.org/10.18429/JACoW-IPAC2023-THPL164)
</details>
<details><summary><b><a href="https://www.coin-or.org/">CBC</a></b> (🥉25 ·  ⭐ 1K) - COIN-OR Branch-and-Cut solver. <code><a href="http://bit.ly/2M0xmjV">EPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/coin-or/Cbc) (👨‍💻 35 · 🔀 140 · 📥 370K · 📋 560 - 29% open · ⏱️ 25.06.2026):

	```
	git clone https://github.com/coin-or/Cbc
	```
- [Conda](https://anaconda.org/conda-forge/coincbc) (📥 1.7M · ⏱️ 12.05.2026):
	```
	conda install -c conda-forge coincbc
	```
</details>
<details><summary><b><a href="https://github.com/oxfordcontrol/Clarabel.rs">Clarabel.rs</a></b> (🥉25 ·  ⭐ 580) - Interior-point solver for convex conic optimisation.. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/rust.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/oxfordcontrol/Clarabel.rs) (👨‍💻 11 · 🔀 48 · 📦 92 · 📋 75 - 32% open · ⏱️ 13.04.2026):

	```
	git clone https://github.com/oxfordcontrol/Clarabel.rs
	```
- [PyPi](https://pypi.org/project/clarabel) (📥 4.2M / month · 📦 43 · ⏱️ 11.06.2025):
	```
	pip install clarabel
	```
- [Conda](https://anaconda.org/conda-forge/clarabel) (📥 440K · ⏱️ 17.12.2025):
	```
	conda install -c conda-forge clarabel
	```
- Paper: [arXiv:2405.12762](https://arxiv.org/abs/2405.12762)
</details>
<details><summary><b><a href="https://github.com/PREDICT-EPFL/piqp">PIQP</a></b> (🥉25 ·  ⭐ 140) - Proximal Interior Point Quadratic Programming solver. <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PREDICT-EPFL/piqp) (👨‍💻 6 · 🔀 22 · 📥 1.4K · 📦 53 · 📋 21 - 23% open · ⏱️ 16.05.2026):

	```
	git clone https://github.com/PREDICT-EPFL/piqp
	```
- [PyPi](https://pypi.org/project/piqp) (📥 94K / month · 📦 13 · ⏱️ 11.05.2026):
	```
	pip install piqp
	```
- [Conda](https://anaconda.org/conda-forge/piqp) (📥 350K · ⏱️ 14.05.2026):
	```
	conda install -c conda-forge piqp
	```
- Paper (📚 18 citations): [10.1109/CDC49753.2023.10383915](https://doi.org/10.1109/CDC49753.2023.10383915)
</details>
<details><summary><b><a href="https://github.com/MadNLP/MadNLP.jl">MadNLP</a></b> (🥉24 ·  ⭐ 250) - A solver for nonlinear programming with GPU support. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/MadNLP/MadNLP.jl) (👨‍💻 20 · 🔀 29 · 📋 140 - 24% open · ⏱️ 31.07.2026):

	```
	git clone https://github.com/MadNLP/MadNLP.jl
	```
- [Julia](https://juliahub.com/ui/Packages/General/MadNLP) (📥 800 / month):
	```
	import Pkg; Pkg.add("MadNLP")
	```
- Papers: [arXiv:2307.16830](https://arxiv.org/abs/2307.16830), [arXiv:2010.02404](https://arxiv.org/abs/2010.02404)
</details>
<details><summary><b><a href="https://www.coin-or.org/">Clp</a></b> (🥉23 ·  ⭐ 490) - COIN-OR Linear Programming Solver. <code><a href="http://bit.ly/2M0xmjV">EPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/coin-or/Clp) (👨‍💻 28 · 🔀 96 · 📥 16K · 📋 210 - 20% open · ⏱️ 15.07.2026):

	```
	git clone https://github.com/coin-or/Clp
	```
- [Conda](https://anaconda.org/conda-forge/coin-or-clp) (📥 1.7M · ⏱️ 11.05.2026):
	```
	conda install -c conda-forge coin-or-clp
	```
</details>
<details><summary><b><a href="https://github.com/oxfordcontrol/Clarabel.jl">Clarabel.jl</a></b> (🥉23 ·  ⭐ 280) - Interior-point solver for convex conic optimisation.. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/oxfordcontrol/Clarabel.jl) (👨‍💻 13 · 🔀 28 · 📋 76 - 17% open · ⏱️ 14.04.2026):

	```
	git clone https://github.com/oxfordcontrol/Clarabel.jl
	```
- [Julia](https://juliahub.com/ui/Packages/General/Clarabel) (📥 4.8K / month):
	```
	import Pkg; Pkg.add("Clarabel")
	```
- Paper: [arXiv:2405.12762](https://arxiv.org/abs/2405.12762)
</details>
<details><summary><b><a href="https://github.com/ds4dm/Tulip.jl">Tulip</a></b> (🥉22 ·  ⭐ 160) - Interior-point solver in pure Julia. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ds4dm/Tulip.jl) (👨‍💻 12 · 🔀 24 · 📋 47 - 38% open · ⏱️ 19.04.2026):

	```
	git clone https://github.com/ds4dm/Tulip.jl
	```
- [Julia](https://juliahub.com/ui/Packages/General/Tulip) (📥 370 / month):
	```
	import Pkg; Pkg.add("Tulip")
	```
- Paper (📚 13 citations): [10.1007/s12532-020-00200-8](https://doi.org/10.1007/s12532-020-00200-8)
</details>
<details><summary><b><a href="https://github.com/kvxopt/kvxopt">KVXOPT</a></b> (🥉13 ·  ⭐ 13) - CVXOPT with additional SuiteSparse wrappers. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/kvxopt/kvxopt) (👨‍💻 16 · 🔀 1 · 📥 8 · 📦 34 · ⏱️ 22.02.2026):

	```
	git clone https://github.com/kvxopt/kvxopt
	```
- [PyPi](https://pypi.org/project/kvxopt) (📥 7K / month · 📦 14 · ⏱️ 22.02.2026):
	```
	pip install kvxopt
	```
- [Conda](https://anaconda.org/conda-forge/kvxopt) (📥 480K · ⏱️ 23.02.2026):
	```
	conda install -c conda-forge kvxopt
	```
</details>
<details><summary>Show 1 hidden projects...</summary>

- <b><a href="https://github.com/embotech/ecos">ECOS</a></b> (🥈39 ·  ⭐ 550 · 🧊) - Conic solver for second-order cone programming. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code>
</details>
<br>

## Machine and Reinforcement Learning

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://l2rpn.chalearn.org/">Grid2Op</a></b> (🥇25 ·  ⭐ 460) - Modeling sequential decision making in power systems. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Grid2op/grid2op) (👨‍💻 32 · 🔀 150 · 📥 1 · 📋 410 - 15% open · ⏱️ 18.06.2026):

	```
	git clone https://github.com/Grid2op/grid2op
	```
- [PyPi](https://pypi.org/project/Grid2Op) (📥 17K / month · 📦 9 · ⏱️ 18.06.2026):
	```
	pip install Grid2Op
	```
- [Docker Hub](https://hub.docker.com/r/bdonnot/grid2op) (📥 12K · ⭐ 1 · ⏱️ 05.07.2022):
	```
	docker pull bdonnot/grid2op
	```
</details>
<details><summary><b><a href="https://github.com/JarvisETHZ/Daline">Daline</a></b> (🥉7 ·  ⭐ 25) - A Data-driven Power Flow Linearization Toolbox. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/JarvisETHZ/Daline) (👨‍💻 1 · 📥 9 · ⏱️ 29.01.2026):

	```
	git clone https://github.com/JarvisETHZ/Daline
	```
- Paper: [10.3929/ethz-b-000681867](https://doi.org/10.3929/ethz-b-000681867)
</details>
<details><summary>Show 3 hidden projects...</summary>

- <b><a href="https://github.com/RLGC-Project/RLGC">RLGC</a></b> (🥈17 ·  ⭐ 140 · 🧊) - RL for Grid Control (RLGC). <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://deepsolar.web.app">DeepSolar</a></b> (🥉9 ·  ⭐ 270 · 🧊) - Houseshold-level solar panel identification with deep.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://github.com/cuihantao/andes_gym">andes_gym</a></b> (🥉4 ·  ⭐ 14 · 🧊) - ANDES RL Environment for OpenAI Gym. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
</details>
<br>

## Visualization

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://www.powsybl.org">PowSyBl Diagram</a></b> (🥇19 ·  ⭐ 120) - single-line substation diagrams and network graph.. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/powsybl/powsybl-diagram) (👨‍💻 37 · 🔀 29 · 📦 35 · 📋 210 - 34% open · ⏱️ 06.07.2026):

	```
	git clone https://github.com/powsybl/powsybl-diagram
	```
</details>
<details><summary><b><a href="https://www.nlr.gov/analysis/sienna">PowerGraphics.jl</a></b> (🥈18 ·  ⭐ 33) - Visualization for PowerSimulations; NREL Sienna. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Sienna-Platform/PowerGraphics.jl) (👨‍💻 14 · 🔀 18 · 📋 44 - 27% open · ⏱️ 20.06.2026):

	```
	git clone https://github.com/Sienna-Platform/PowerGraphics.jl
	```
- [Julia](https://juliahub.com/ui/Packages/General/PowerGraphics) (📥 100 / month):
	```
	import Pkg; Pkg.add("PowerGraphics")
	```
</details>
<details><summary><b><a href="https://ltb.curent.org/">LTB AGVis</a></b> (🥉12 ·  ⭐ 10) - Geographical Visualization for Power Grid; CURENT LTB. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CURENT/agvis) (👨‍💻 14 · 🔀 6 · 📥 20 · 📦 3 · 📋 25 - 36% open · ⏱️ 09.03.2026):

	```
	git clone https://github.com/CURENT/agvis
	```
- [PyPi](https://pypi.org/project/agvis) (📥 36 / month · ⏱️ 07.06.2024):
	```
	pip install agvis
	```
- Paper (📚 5 citations): [10.1109/NAPS58826.2023.10318583](https://doi.org/10.1109/NAPS58826.2023.10318583)
</details>
<details><summary>Show 1 hidden projects...</summary>

- <b><a href="https://github.com/power-flow-analyzer/PowerFlowAnalyzer">PowerFlowAnalyzer</a></b> (🥉7 ·  ⭐ 7 · 🧊) - Toolbox for power system analysis. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
</details>
<br>

## Messaging Environment

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary>Show 1 hidden projects...</summary>

- <b><a href="https://ltb.curent.org/">LTB DiME</a></b> (🥇14 ·  ⭐ 4 · 🧊) - Distributed Messaging Environment; CURENT LTB. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
</details>
<br>

## Power-System Data

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

🔗&nbsp;<b><a href="https://github.com/Team-Nando/MV-LV-Networks">Australian MV-LV Networks</a></b> ( ⭐ 31 · 🧊)  - Large-scale three-phase Australian MV distribution.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://power-grid-lib.github.io">Power Grid Lib - Optimal Power Flow</a></b> ( ⭐ 410 · 🧊)  - Benchmarks for OPF. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://power-grid-lib.github.io">Power Grid Lib - Unit Commitment</a></b> ( ⭐ 130)  - Benchmarks for UC. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://power-grid-lib.github.io">Power Grid Lib - Optimal Power Flow with HVDC Lines</a></b> ( ⭐ 26 · 🧊)  - Benchmarks for OPF with HVDC. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/enliten/ENLITEN-Grid-Econ-Data">WECC-and-NPCC-Electricity-Economic-Data</a></b> ( ⭐ 14 · 🧊)  - Economic data on WECC and NPCC. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://opendata.elia.be/pages/home/">OpenDataElia</a></b>  - Data by opendatasoft. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/owid/energy-data">Data on Energy</a></b> ( ⭐ 420)  - Data on energy by Our World in Data. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/tamu-engineering-research/COVID-EMDA">COVID-EMDA</a></b> ( ⭐ 60 · 🧊)  - Cross-Domain Data Hub with Data in USA. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/rte-france/digital-fault-recording-database">Electrical Signals Databases</a></b> ( ⭐ 35)  - Voltage and current samples from Digital Fault Recorder. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/lbl-hub/CSEE-Benchmark">A new power system benchmark</a></b> ( ⭐ 48)  - A new type of power system calculation example by the.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/NanpengYu/pmuBAGE">pmuBAGE</a></b> ( ⭐ 8 · 🧊)  - Synthetic phasor measurement unit dataset. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

<details><summary><b><a href="https://simbench.de/en/">SimBench</a></b> (🥇20 ·  ⭐ 140) - Benchmark dataset of German LV/MV/HV grids including.. <code><a href="https://tldrlegal.com/search?q=odbl-1.0">❗️odbl-1.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/e2nIEE/simbench) (👨‍💻 6 · 🔀 38 · 📦 51 · 📋 39 - 15% open · ⏱️ 02.04.2026):

	```
	git clone https://github.com/e2nIEE/simbench
	```
- [PyPi](https://pypi.org/project/simbench) (📥 12K / month · 📦 15 · ⏱️ 02.04.2026):
	```
	pip install simbench
	```
- [Conda](https://anaconda.org/conda-forge/simbench):
	```
	conda install -c conda-forge simbench
	```
</details>
<details><summary><b><a href="https://github.com/GridMod/RTS-GMLC">RTS-GMLC</a></b> (🥈15 ·  ⭐ 250) - Reliability Test System dataset for Grid.. <code><a href="https://tldrlegal.com/search?q=DOE/NREL/ALLIANCE%20data%20use%20disclaimer%20agreement">❗️DOE/NREL/ALLIANCE data use disclaimer agreement</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/GridMod/RTS-GMLC) (👨‍💻 31 · 🔀 97 · 📋 130 - 22% open · ⏱️ 23.10.2025):

	```
	git clone https://github.com/GridMod/RTS-GMLC
	```
</details>
<details><summary><b><a href="https://colib.net/">COLIB</a></b> (🥉7 ·  ⭐ 14 · 💤) - Collaborative dynamic library. <code><a href="https://tldrlegal.com/search?q=CC-BY-4.0">❗️CC-BY-4.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CRESYM/colib0.github.io) (👨‍💻 12 · 🔀 4 · 📋 130 - 9% open · ⏱️ 12.05.2025):

	```
	git clone https://github.com/CRESYM/colib0.github.io
	```
</details>
<details><summary><b><a href="https://github.com/LSU-RAISE-LAB/DPLib">DPLib</a></b> (🥉7 ·  ⭐ 11) - MATLAB-based distributed benchmark library and.. <code><a href="https://tldrlegal.com/search?q=Academic%20and%20Research%20Use%20Only">❗️Academic and Research Use Only</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/LSU-RAISE-LAB/DPLib) (👨‍💻 2 · 🔀 4 · ⏱️ 15.06.2026):

	```
	git clone https://github.com/LSU-RAISE-LAB/DPLib
	```
- Paper: [arXiv:2506.20819](https://arxiv.org/abs/2506.20819)
</details>
<br>

## Power Electronics

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary>Show 1 hidden projects...</summary>

- <b><a href="https://github.com/vrnthakore/gseim">GSEIM</a></b> (🥇6 · 🧊) - Simulation of electrical circuits. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code>
</details>
<br>

## Data Management

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://pypsa.org">Atlite</a></b> (🥇31 ·  ⭐ 390) - Calculating Renewable Power Potentials. <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/atlite) (👨‍💻 46 · 🔀 130 · 📦 120 · 📋 170 - 32% open · ⏱️ 17.07.2026):

	```
	git clone https://github.com/PyPSA/atlite
	```
- [PyPi](https://pypi.org/project/atlite) (📥 5.9K / month · 📦 2 · ⏱️ 21.04.2026):
	```
	pip install atlite
	```
- [Conda](https://anaconda.org/conda-forge/atlite) (📥 170K · ⏱️ 21.04.2026):
	```
	conda install -c conda-forge atlite
	```
- Paper (📚 159 citations): [10.21105/joss.03294](https://doi.org/10.21105/joss.03294)
</details>
<details><summary><b><a href="https://www.gridstatus.io">GridStatus</a></b> (🥇26 ·  ⭐ 440) - Extract data from ISOs and other sources. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/gridstatus/gridstatus) (👨‍💻 47 · 🔀 83 · 📦 31 · 📋 160 - 32% open · ⏱️ 03.08.2026):

	```
	git clone https://github.com/gridstatus/gridstatus
	```
- [PyPi](https://pypi.org/project/gridstatus) (📥 83K / month · 📦 2 · ⏱️ 21.04.2026):
	```
	pip install gridstatus
	```
- [Conda](https://anaconda.org/services/gridstatus) (📥 51 · ⏱️ 25.03.2025):
	```
	conda install -c services gridstatus
	```
</details>
<details><summary><b><a href="https://pypsa.org">powerplantmatching</a></b> (🥈23 ·  ⭐ 230) - Tools to combine multiple power plant databases. <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/powerplantmatching) (👨‍💻 37 · 🔀 73 · 📥 87 · 📦 88 · 📋 120 - 23% open · ⏱️ 23.06.2026):

	```
	git clone https://github.com/PyPSA/powerplantmatching
	```
- [PyPi](https://pypi.org/project/powerplantmatching) (📥 4.6K / month · ⏱️ 11.02.2026):
	```
	pip install powerplantmatching
	```
- [Conda](https://anaconda.org/conda-forge/powerplantmatching) (📥 160K · ⏱️ 11.02.2026):
	```
	conda install -c conda-forge powerplantmatching
	```
- Paper (📚 2 citations): [10.1016/j.esr.2018.11.004](https://doi.org/10.1016/j.esr.2018.11.004)
</details>
<details><summary><b><a href="https://groups.io/g/powergenome">PowerGenome</a></b> (🥈17 ·  ⭐ 230) - Create inputs for power systems models. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PowerGenome/PowerGenome) (👨‍💻 18 · 🔀 77 · 📋 230 - 54% open · ⏱️ 13.02.2026):

	```
	git clone https://github.com/PowerGenome/PowerGenome
	```
- [PyPi](https://pypi.org/project/PowerGenome) (📥 88 / month · ⏱️ 21.03.2025):
	```
	pip install PowerGenome
	```
- [Conda](https://anaconda.org/conda-forge/powergenome) (📥 1.8K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge powergenome
	```
</details>
<details><summary><b><a href="https://www.energydatamodel.org/">EnergyDataModel</a></b> (🥈17 ·  ⭐ 92) - Represent energy systems as Python data classes. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/rebase-energy/energydatamodel) (👨‍💻 5 · 🔀 9 · ⏱️ 31.07.2026):

	```
	git clone https://github.com/rebase-energy/EnergyDataModel
	```
- [PyPi](https://pypi.org/project/energydatamodel) (📥 1.8K / month · 📦 6 · ⏱️ 31.07.2026):
	```
	pip install energydatamodel
	```
</details>
<details><summary><b><a href="https://github.com/sogno-platform/cimpy">CIMpy</a></b> (🥈17 ·  ⭐ 78 · 💤) - CIM files to the XML/RDF format. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/sogno-platform/cimpy) (👨‍💻 11 · 🔀 25 · 📦 17 · 📋 17 - 29% open · ⏱️ 23.02.2025):

	```
	git clone https://github.com/sogno-platform/cimpy
	```
- [PyPi](https://pypi.org/project/cimpy) (📥 870 / month · 📦 1 · ⏱️ 20.06.2024):
	```
	pip install cimpy
	```
- Paper (📚 1 citation): [10.1049/tje2.12208](https://doi.org/10.1049/tje2.12208)
</details>
<details><summary><b><a href="https://github.com/dsgrid/dsgrid">dsgrid</a></b> (🥉15 ·  ⭐ 33) - Demand-side grid projects, datasets and queries. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/rust.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dsgrid/dsgrid) (👨‍💻 7 · 🔀 6 · 📦 1 · 📋 150 - 43% open · ⏱️ 31.03.2026):

	```
	git clone https://github.com/dsgrid/dsgrid
	```
</details>
<details><summary><b><a href="https://www.nlr.gov/analysis/sienna">PowerSystemsInvestmentsPortfolios.jl</a></b> (🥉12 ·  ⭐ 13) - Data models for Power Systems investment models; NREL.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Sienna-Platform/PowerSystemsInvestmentsPortfolios.jl) (👨‍💻 8 · 🔀 9 · 📋 72 - 26% open · ⏱️ 06.08.2026):

	```
	git clone https://github.com/Sienna-Platform/PowerSystemsInvestmentsPortfolios.jl
	```
- [Julia](https://juliahub.com/ui/Packages/General/PowerSystemsInvestmentsPortfolios) (📥 12 / month):
	```
	import Pkg; Pkg.add("PowerSystemsInvestmentsPortfolios")
	```
</details>
<details><summary><b><a href="https://github.com/cuihantao/PowerfulCases">PowerfulCases</a></b> (🥉9 ·  ⭐ 5) - Test case data management for power systems simulation. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cuihantao/PowerfulCases) (⏱️ 19.01.2026):

	```
	git clone https://github.com/cuihantao/PowerfulCases
	```
- [PyPi](https://pypi.org/project/powerfulcases) (📥 37 / month · ⏱️ 29.12.2025):
	```
	pip install powerfulcases
	```
</details>
<details><summary><b><a href="https://github.com/cuihantao/PowerDynData.jl">PowerDynData.jl</a></b> (🥉7 ·  ⭐ 2) - Julia package for parsing PSS/E DYR dynamic data files. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cuihantao/PowerDynData.jl) (👨‍💻 4 · 🔀 1 · ⏱️ 04.01.2026):

	```
	git clone https://github.com/cuihantao/PowerDynData.jl
	```
- [Julia](https://juliahub.com/ui/Packages/General/PowerDynData) (📥 9 / month):
	```
	import Pkg; Pkg.add("PowerDynData")
	```
</details>
<details><summary>Show 3 hidden projects...</summary>

- <b><a href="https://github.com/lanl-ansi/grg-pssedata">grg-pssedata</a></b> (🥉13 ·  ⭐ 35 · 🧊) - Python tools for working with PSSE v33 data files. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://github.com/RWTH-IAEW/cimpyorm">cimpyorm</a></b> (🥉9 ·  ⭐ 12 · 🧊) - Python ORM middleware for IEC CIM and CGMES datasets. <code><a href="https://tldrlegal.com/search?q=BSD-3.0">❗️BSD-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="https://github.com/anderson-optimization/em-psse">PSSE RAW</a></b> (🥉5 ·  ⭐ 39 · 🧊) - PSSE RAW parser. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code>
</details>
<br>

## Educational Resources

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

🔗&nbsp;<b><a href="https://powercybertraining.github.io">PowerCyber Training</a></b> ( ⭐ 11)  - PowerCyber Training modules source. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/Power-Systems-Textbook/TextbookSimulations">TextbookSimulations</a></b> ( ⭐ 12 · 🧊)  - Examples and problems accompanying Daniel Kirschens.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/CURENT/ece522">UTK ECE 522 - Power System Analysis II</a></b> ( ⭐ 6)  - Hands-on Project for Power System Analysis II (UTK.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/bcornelusse/ELEC0447-analysis-power-systems">ELEC0447 Analysis of Electric Power and Energy Systems</a></b> ( ⭐ 24)  - Masters course of power systems analysis at ULige. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/Team-Nando/Tutorial-DERHostingCapacity-0-dss_python">Tutorial on DER Hosting Capacity Part 0</a></b> ( ⭐ 6 · 💤)  - Using dss_python. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/Team-Nando/Tutorial-DERHostingCapacity-1-AdvancedTools_LV">Tutorial on DER Hosting Capacity Part 1</a></b> ( ⭐ 5)  - Advanced Tools for the Analysis of Three-Phase.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/Team-Nando/Tutorial-DERHostingCapacity-2-TimeSeries_LV">Tutorial on DER Hosting Capacity Part 2</a></b> ( ⭐ 2)  - Time-Series Analysis and PV Hosting Capacity of LV.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/Team-Nando/Tutorial-DERHostingCapacity-3-VoltWatt_LV">Tutorial on DER Hosting Capacity Part 3</a></b> ( ⭐ 1)  - Volt-Watt Control and PV Hosting Capacity of LV.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/Team-Nando/Tutorial-DERHostingCapacity-4-MonteCarlo_MV-LV">Tutorial on DER Hosting Capacity Part 4</a></b> ( ⭐ 3 · 💤)  - Monte Carlo Assessment of PV Hosting Capacity of an.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://ltb.curent.org">LTB Demo</a></b> ( ⭐ 4)  - Ready-to-use LTB usage examples. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

<details><summary><b><a href="https://www.opti-verse.org/">OptiVerse</a></b> (🥇7 ·  ⭐ 12 · 💤) - A library with innovative optimization solutions. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/feyntech-opt/OptiVerse) (👨‍💻 5 · 🔀 12 · ⏱️ 15.02.2025):

	```
	git clone https://github.com/feyntech-opt/OptiVerse
	```
</details>
<br>

## Large-Language-Model Application

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="http://poweragent.seas.harvard.edu/">PowerMCP</a></b> (🥇16 ·  ⭐ 190) - Collection of MCP servers for power system software. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Power-Agent/PowerMCP) (👨‍💻 16 · 🔀 55 · 📋 7 - 42% open · ⏱️ 02.07.2026):

	```
	git clone https://github.com/Power-Agent/PowerMCP
	```
</details>
<details><summary><b><a href="https://github.com/open-energy-transition/pypsa-mcp">PyPSA MCP</a></b> (🥈10 ·  ⭐ 70) - PyPSA Energy Modeling for LLMs. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/open-energy-transition/pypsa-mcp) (👨‍💻 2 · 🔀 8 · 📥 11 · ⏱️ 20.03.2026):

	```
	git clone https://github.com/open-energy-transition/pypsa-mcp
	```
- [PyPi](https://pypi.org/project/pypsamcp) (📥 41 / month · ⏱️ 20.03.2026):
	```
	pip install pypsamcp
	```
</details>
<details><summary><b><a href="http://poweragent.seas.harvard.edu/">PowerFM</a></b> (🥉6 ·  ⭐ 48) - Foundation models in the power and energy domain. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Power-Agent/PowerFM) (👨‍💻 1 · 🔀 4 · ⏱️ 14.05.2026):

	```
	git clone https://github.com/Power-Agent/PowerFM
	```
</details>
<details><summary><b><a href="http://poweragent.seas.harvard.edu/">PowerWorkflow</a></b> (🥉6 ·  ⭐ 39 · 💤) - Collection of agentic workflows for power system.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Power-Agent/PowerWF) (👨‍💻 1 · 🔀 2 · ⏱️ 19.07.2025):

	```
	git clone https://github.com/Power-Agent/PowerWF
	```
</details>
<details><summary><b><a href="https://ltb.curent.org/">P-V Curve LLM</a></b> (🥉5 ·  ⭐ 4) - Using LLMs in Power-Voltage Curves for Voltage Stability.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CURENT/pv-curve-llm) (👨‍💻 6 · 🔀 2 · ⏱️ 11.05.2026):

	```
	git clone https://github.com/CURENT/pv-curve-llm
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
