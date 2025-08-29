[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/ps-wiki-best-of-ps-badge.png)](https://mseep.ai/app/ps-wiki-best-of-ps)

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
    <a href="#Contents" title="Project Count"><img src="https://img.shields.io/badge/projects-160-blue.svg?color=5ac4bf"></a>
    <a href="#Contribution" title="Contributions are welcome"><img src="https://img.shields.io/badge/contributions-welcome-green.svg"></a>
    <img alt="GitHub Created At" src="https://img.shields.io/github/created-at/ps-wiki/best-of-ps">
    <a href="https://github.com/ps-wiki/best-of-ps/releases" title="Best-of Updates"><img src="https://img.shields.io/github/release-date/ps-wiki/best-of-ps?color=green&label=updated"></a>
    <a href="https://www.repostatus.org/#active"><img src="https://www.repostatus.org/badges/latest/active.svg" alt="Project Status: Active – The project has reached a stable, usable state and is being actively developed." /></a>
    <img alt="GitHub License" src="https://img.shields.io/github/license/ps-wiki/best-of-ps">
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/ps-wiki/best-of-ps">
    <a href="https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fps-wiki%2Fbest-of-ps"><img src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fps-wiki%2Fbest-of-ps&labelColor=%23697689&countColor=%23dce775&style=plastic&labelStyle=lower" /></a>
</p>

This curated list contains 160 open-source projects with a total of 75K stars grouped into 16 categories. All projects are ranked by a project-popularity score, which is calculated based on various metrics automatically collected from GitHub and different package managers. If you like to add or update projects, feel free to open an [issue](https://github.com/ps-wiki/best-of-ps/issues/new/choose), submit a [pull request](https://github.com/ps-wiki/best-of-ps/pulls), or directly edit the [projects.yaml](https://github.com/ps-wiki/best-of-ps/edit/main/projects.yaml). Contributions are very welcome!

## Contents

- [Phasor Simulation](#phasor-simulation) _16 projects_
- [EMT Simulation](#emt-simulation) _2 projects_
- [Steady State Simulation](#steady-state-simulation) _42 projects_
- [Interface](#interface) _22 projects_
- [Gas Simulation](#gas-simulation) _3 projects_
- [Co-Simulation Environment](#co-simulation-environment) _2 projects_
- [Optimization Modeling Language](#optimization-modeling-language) _8 projects_
- [Optimizer](#optimizer) _17 projects_
- [Machine/Reinforcement Learning for Power Grid](#machinereinforcement-learning-for-power-grid) _4 projects_
- [Visualization](#visualization) _3 projects_
- [Messaging Environment](#messaging-environment) _2 projects_
- [Power System Data](#power-system-data) _18 projects_
- [Power Electronics](#power-electronics) _1 projects_
- [Database Management](#database-management) _2 projects_
- [Textbook](#textbook) _11 projects_
- [Large Language Model](#large-language-model) _5 projects_

## Explanation
- 🥇🥈🥉&nbsp; Combined project-quality score
- ⭐️&nbsp; Star count from GitHub
- 🐣&nbsp; New project _(less than 6 months old)_
- 💤&nbsp; Inactive project _(12 months no activity)_
- 💀&nbsp; Dead project _(1200 months no activity)_
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
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13">&nbsp; CI via GitHub Actions
- <img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/azure.ico" style="display:inline;" width="13" height="13">&nbsp; CI via Azure Pipelines
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

<details><summary><b><a href="http://dynawo.org">Dynaωo</a></b> (🥇23 ·  ⭐ 86) - C++/Modelica simulation tools for power systems. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/modelica.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dynawo/dynawo) (👨‍💻 60 · 🔀 27 · 📥 18K · 📋 1.6K - 11% open · ⏱️ 26.08.2025):

	```
	git clone https://github.com/dynawo/dynawo
	```
</details>
<details><summary><b><a href="https://ltb.curent.org/">LTB ANDES</a></b> (🥇21 ·  ⭐ 290) - Transient Stability Simulator; CURENT LTB. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/azure.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CURENT/andes) (👨‍💻 26 · 🔀 120 · 📦 28 · 📋 79 - 18% open · ⏱️ 02.05.2025):

	```
	git clone https://github.com/CURENT/andes
	```
- [PyPi](https://pypi.org/project/andes) (📥 2.1K / month · 📦 4 · ⏱️ 05.01.2025):
	```
	pip install andes
	```
- [Conda](https://anaconda.org/conda-forge/andes) (📥 660K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge andes
	```
- [Docker Hub](https://hub.docker.com/r/CURENT/andes):
	```
	docker pull CURENT/andes
	```
</details>
<details><summary><b><a href="https://www.gridlabd.org/">GridLAB-D</a></b> (🥈19 ·  ⭐ 180) - Distribution power system simulator. <code><a href="https://github.com/gridlab-d/gridlab-d/blob/master/LICENSE">❗️Custom</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/gridlab-d/gridlab-d) (👨‍💻 76 · 🔀 120 · 📥 7.1K · 📋 1.3K - 24% open · ⏱️ 28.05.2025):

	```
	git clone https://github.com/gridlab-d/gridlab-d
	```
</details>
<details><summary><b><a href="https://github.com/OpenIPSL/OpenIPSL">OpenIPSL</a></b> (🥈17 ·  ⭐ 93) - A Power System Library written in the Modelica. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/modelica.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/OpenIPSL/OpenIPSL) (👨‍💻 35 · 🔀 59 · 📥 500 · 📋 120 - 12% open · ⏱️ 27.08.2025):

	```
	git clone https://github.com/OpenIPSL/OpenIPSL
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/analysis/sienna.html">PowerSimulationsDynamics.jl</a></b> (🥈16 ·  ⭐ 200) - Dynamic Power System simulations; NREL Sienna. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL-Sienna/PowerSimulationsDynamics.jl) (👨‍💻 15 · 🔀 51 · 📋 140 - 32% open · ⏱️ 09.07.2025):

	```
	git clone https://github.com/NREL-Sienna/PowerSimulationsDynamics.jl
	```
</details>
<details><summary><b><a href="https://xyce.sandia.gov/">Xyce</a></b> (🥈16 ·  ⭐ 190) - The Xyce Parallel Electronic Simulator. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Xyce/Xyce) (👨‍💻 8 · 🔀 31 · 📥 1K · 📋 110 - 34% open · ⏱️ 25.08.2025):

	```
	git clone https://github.com/Xyce/Xyce
	```
- [PyPi](https://pypi.org/project/xyce) (📥 7 / month · ⏱️ 05.01.2022):
	```
	pip install xyce
	```
- [Conda](https://anaconda.org/vlsida-eda/xyce) (📥 3.5K · ⏱️ 25.03.2025):
	```
	conda install -c vlsida-eda xyce
	```
</details>
<details><summary><b><a href="https://gridpack.pnnl.gov/wiki/index.php/Main_Page">GridPACK</a></b> (🥈15 ·  ⭐ 53) - High-Performance Electric Grid Simulation. <code><a href="https://github.com/GridOPTICS/GridPACK/blob/develop/docs/markdown/LICENSE.md">❗️Custom</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/GridOPTICS/GridPACK) (👨‍💻 54 · 🔀 22 · 📥 620 · 📋 140 - 22% open · ⏱️ 30.07.2025):

	```
	git clone https://github.com/GridOPTICS/GridPACK
	```
</details>
<details><summary><b><a href="https://www.epri.com/OpenDER">OpenDER</a></b> (🥉14 ·  ⭐ 66) - Inverter-based DER simulation. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/epri-dev/OpenDER) (👨‍💻 2 · 🔀 27 · 📦 3 · ⏱️ 15.04.2025):

	```
	git clone https://github.com/epri-dev/OpenDER
	```
- [PyPi](https://pypi.org/project/opender) (📥 3.7K / month · ⏱️ 13.04.2025):
	```
	pip install opender
	```
</details>
<details><summary><b><a href="https://github.com/modelica-3rdparty/PowerSystems">PowerSystems</a></b> (🥉13 ·  ⭐ 73 · 💤) - Modelica 3rd party library for electrical power.. <code><a href="https://modelica.org/licenses/ModelicaLicense2/">❗️Custom</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/modelica.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/modelica-3rdparty/PowerSystems) (👨‍💻 10 · 🔀 37 · 📋 41 - 34% open · ⏱️ 07.05.2024):

	```
	git clone https://github.com/modelica-3rdparty/PowerSystems
	```
</details>
<details><summary><b><a href="https://github.com/changgang/steps">STEPS</a></b> (🥉12 ·  ⭐ 57 · 💤) - Balanced large-scale AC-DC hybrid power system analysis. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/changgang/steps) (👨‍💻 4 · 🔀 19 · 📥 50 · 📦 7 · 📋 3 - 33% open · ⏱️ 24.03.2024):

	```
	git clone https://github.com/changgang/steps
	```
- [PyPi](https://pypi.org/project/stepspy) (📥 51 / month · ⏱️ 22.09.2024):
	```
	pip install stepspy
	```
</details>
<details><summary><b><a href="https://github.com/ANL-CEEESA/powersas.m">PowerSAS.m</a></b> (🥉7 ·  ⭐ 20 · 💤) - Power grid analysis framework based on semi-analytical.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ANL-CEEESA/powersas.m) (👨‍💻 4 · 🔀 5 · ⏱️ 05.01.2024):

	```
	git clone https://github.com/ANL-CEEESA/powersas.m
	```
</details>
<details><summary><b><a href="https://github.com/OpenHybridSim/OpenHybridSim-code">OpenHybridSim</a></b> (🥉6 ·  ⭐ 8 · 💤) - EMT-TS hybrid simulation. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/OpenHybridSim/OpenHybridSim-code) (🔀 4 · ⏱️ 05.05.2020):

	```
	git clone https://github.com/OpenHybridSim/OpenHybridSim-code
	```
</details>
<details><summary><b><a href="https://github.com/ANL-CEEESA/gensas">GenSAS</a></b> (🥉5 ·  ⭐ 1) - A C++ based generalized simulation tool based on semi-.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ANL-CEEESA/gensas) (👨‍💻 3 · 🔀 1 · ⏱️ 04.03.2025):

	```
	git clone https://github.com/ANL-CEEESA/gensas
	```
</details>
<details><summary><b><a href="http://faraday1.ucd.ie/psat.html">PSAT</a></b> (🥉4 ·  ⭐ 13 · 💤) - Unofficial repository of PSAT by Prof. Federico Milano. <code><a href="https://tldrlegal.com/search?q=GPL">❗️GPL</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Sinan81/PSAT) (👨‍💻 2 · 🔀 8 · 📥 140 · ⏱️ 23.06.2020):

	```
	git clone https://github.com/Sinan81/PSAT
	```
</details>
<details><summary><b><a href="https://github.com/HuaizhiWang/matmtdc">matmtdc</a></b> (🥉4 ·  ⭐ 11 · 💤) - Dynamic analysis of AC/DC hybrid power systems. <code><a href="https://tldrlegal.com/search?q=undefined">❗️undefined</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/HuaizhiWang/matmtdc) (🔀 6 · ⏱️ 04.05.2021):

	```
	git clone https://github.com/HuaizhiWang/matmtdc
	```
</details>
<details><summary><b><a href="https://sites.ecse.rpi.edu/~chowj/">PST</a></b> (🥉3 ·  ⭐ 5 · 💤) - Unofficial repository of PST by Prof. Joe Chow. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cuihantao/pst) (🔀 1 · ⏱️ 11.04.2020):

	```
	git clone https://github.com/cuihantao/pst
	```
</details>
<br>

## EMT Simulation

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://dpsim.fein-aachen.org/">DPsim</a></b> (🥇20 ·  ⭐ 88) - Simulation for both EMT and phasor. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/sogno-platform/dpsim) (👨‍💻 37 · 🔀 62 · 📦 11 · 📋 160 - 52% open · ⏱️ 07.07.2025):

	```
	git clone https://github.com/sogno-platform/dpsim
	```
- [PyPi](https://pypi.org/project/dpsim) (📥 73 / month · ⏱️ 10.12.2022):
	```
	pip install dpsim
	```
</details>
<details><summary><b><a href="https://github.com/NREL/ParaEMT_public">ParaEMT</a></b> (🥉9 ·  ⭐ 71) - Parallel EMT simulation. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL/ParaEMT_public) (👨‍💻 4 · 🔀 30 · ⏱️ 24.05.2025):

	```
	git clone https://github.com/NREL/ParaEMT_public
	```
</details>
<br>

## Steady State Simulation

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://www.pandapower.org/">pandapower</a></b> (🥇35 ·  ⭐ 1K · 📈) - Convenient Power System Modelling and Analysis. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/e2nIEE/pandapower) (👨‍💻 160 · 🔀 510 · 📦 500 · 📋 1.1K - 18% open · ⏱️ 28.08.2025):

	```
	git clone https://github.com/e2nIEE/pandapower
	```
- [PyPi](https://pypi.org/project/pandapower) (📥 87K / month · 📦 68 · ⏱️ 16.06.2025):
	```
	pip install pandapower
	```
- [Conda](https://anaconda.org/conda-forge/pandapower) (📥 30K · ⏱️ 16.06.2025):
	```
	conda install -c conda-forge pandapower
	```
- [Docker Hub](https://hub.docker.com/r/pauldepraz/pandapowerapi) (📥 110 · ⏱️ 09.02.2021):
	```
	docker pull pauldepraz/pandapowerapi
	```
</details>
<details><summary><b><a href="https://pypsa.org">PyPSA</a></b> (🥇32 ·  ⭐ 1.6K) - Python for Power System Analysis. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/PyPSA) (👨‍💻 100 · 🔀 540 · 📦 300 · 📋 450 - 26% open · ⏱️ 15.08.2025):

	```
	git clone https://github.com/PyPSA/PyPSA
	```
- [PyPi](https://pypi.org/project/pypsa) (📥 11K / month · 📦 31 · ⏱️ 15.08.2025):
	```
	pip install pypsa
	```
- [Conda](https://anaconda.org/conda-forge/pypsa) (📥 160K · ⏱️ 16.08.2025):
	```
	conda install -c conda-forge pypsa
	```
</details>
<details><summary><b><a href="https://github.com/PowerGridModel/power-grid-model">Power Grid Model</a></b> (🥇31 ·  ⭐ 180) - Steady-state distribution power system analysis. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PowerGridModel/power-grid-model) (👨‍💻 28 · 🔀 43 · 📥 820 · 📦 33 · 📋 250 - 32% open · ⏱️ 26.08.2025):

	```
	git clone https://github.com/PowerGridModel/power-grid-model
	```
- [PyPi](https://pypi.org/project/power-grid-model) (📥 50K / month · 📦 10 · ⏱️ 26.08.2025):
	```
	pip install power-grid-model
	```
- [Conda](https://anaconda.org/conda-forge/power-grid-model) (📥 3.7M · ⏱️ 26.08.2025):
	```
	conda install -c conda-forge power-grid-model
	```
</details>
<details><summary><b><a href="https://matpower.org/">MATPOWER</a></b> (🥇25 ·  ⭐ 490) - Steady state power flow simulation. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/MATPOWER/matpower) (👨‍💻 22 · 🔀 160 · 📥 620K · 📋 230 - 10% open · ⏱️ 25.08.2025):

	```
	git clone https://github.com/MATPOWER/matpower
	```
- [Docker Hub](https://hub.docker.com/r/matpower/matpower) (📥 3.1K · ⏱️ 25.08.2025):
	```
	docker pull matpower/matpower
	```
</details>
<details><summary><b><a href="https://www.eroots.tech/software">GridCal</a></b> (🥇25 ·  ⭐ 460) - Cross-platform power systems software. <code><a href="http://bit.ly/37RvQcA">❗️LGPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/SanPen/VeraGrid) (👨‍💻 58 · 🔀 110 · 📥 49 · 📋 260 - 9% open · ⏱️ 27.08.2025):

	```
	git clone https://github.com/SanPen/GridCal
	```
- [PyPi](https://pypi.org/project/GridCal) (📥 1.6K / month · ⏱️ 27.08.2025):
	```
	pip install GridCal
	```
</details>
<details><summary><b><a href="https://www.powsybl.org">PowSyBl Core</a></b> (🥈24 ·  ⭐ 140) - Framework to build power system software. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/powsybl/powsybl-core) (👨‍💻 120 · 🔀 49 · 📦 91 · 📋 690 - 43% open · ⏱️ 19.08.2025):

	```
	git clone https://github.com/powsybl/powsybl-core
	```
</details>
<details><summary><b><a href="rwl.github.io/PYPOWER/api/">PYPOWER</a></b> (🥈22 ·  ⭐ 370) - Port of MATPOWER to Python. <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/rwl/PYPOWER) (👨‍💻 22 · 🔀 120 · 📦 150 · 📋 48 - 72% open · ⏱️ 10.07.2025):

	```
	git clone https://github.com/rwl/PYPOWER
	```
- [PyPi](https://pypi.org/project/PYPOWER) (📥 26K / month · 📦 19 · ⏱️ 10.07.2025):
	```
	pip install PYPOWER
	```
- [Conda](https://anaconda.org/invenia/pypower) (📥 3.2K · ⏱️ 25.03.2025):
	```
	conda install -c invenia pypower
	```
- [Docker Hub](https://hub.docker.com/r/hwanghust/pypower) (📥 27 · ⏱️ 19.05.2019):
	```
	docker pull hwanghust/pypower
	```
</details>
<details><summary><b><a href="https://pypsa.org">PyPSA-Eur</a></b> (🥈21 ·  ⭐ 470) - Sector-Coupled Optimisation Model of the European Energy.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/pypsa-eur) (👨‍💻 100 · 🔀 290 · 📋 570 - 28% open · ⏱️ 26.08.2025):

	```
	git clone https://github.com/PyPSA/pypsa-eur
	```
- [Docker Hub](https://hub.docker.com/r/nimfetrisa/pypsa-eur):
	```
	docker pull nimfetrisa/pypsa-eur
	```
</details>
<details><summary><b><a href="https://pypsa-meets-earth.github.io/">PyPSA-Earth</a></b> (🥈21 ·  ⭐ 280) - Open optimisation model for study energy system.. <code><a href="http://bit.ly/3pwmjO5">❗️AGPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/pypsa-meets-earth/pypsa-earth) (👨‍💻 80 · 🔀 250 · 📋 550 - 37% open · ⏱️ 22.08.2025):

	```
	git clone https://github.com/pypsa-meets-earth/pypsa-earth
	```
</details>
<details><summary><b><a href="https://www.gridpath.io/">GridPath</a></b> (🥈21 ·  ⭐ 120) - Power system planning and operations. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/blue-marble/gridpath) (👨‍💻 13 · 🔀 58 · 📥 1.3K · 📦 4 · 📋 340 - 23% open · ⏱️ 11.08.2025):

	```
	git clone https://github.com/blue-marble/gridpath
	```
- [PyPi](https://pypi.org/project/GridPath) (📥 190 / month · ⏱️ 03.07.2025):
	```
	pip install GridPath
	```
</details>
<details><summary><b><a href="https://www.powsybl.org">PyPowSyBl</a></b> (🥈21 ·  ⭐ 68) - A PowSyBl and Python integration. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/powsybl/pypowsybl) (👨‍💻 35 · 🔀 14 · 📥 350 · 📋 270 - 34% open · ⏱️ 27.08.2025):

	```
	git clone https://github.com/powsybl/pypowsybl
	```
- [PyPi](https://pypi.org/project/pypowsybl) (📥 5.9K / month · 📦 8 · ⏱️ 24.07.2025):
	```
	pip install pypowsybl
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/analysis/sienna.html">PowerSimulations.jl</a></b> (🥈20 ·  ⭐ 300) - Power Systems optimization simulation and modeling;.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL-Sienna/PowerSimulations.jl) (👨‍💻 41 · 🔀 74 · 📋 440 - 21% open · ⏱️ 16.06.2025):

	```
	git clone https://github.com/NREL-Sienna/PowerSimulations.jl
	```
</details>
<details><summary><b><a href="https://github.com/lanl-ansi/PowerModels.jl">PowerModels.jl</a></b> (🥈19 ·  ⭐ 430) - Power Network Optimization. <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/lanl-ansi/PowerModels.jl) (👨‍💻 32 · 🔀 160 · 📋 510 - 18% open · ⏱️ 12.08.2025):

	```
	git clone https://github.com/lanl-ansi/PowerModels.jl
	```
</details>
<details><summary><b><a href="https://energy.mit.edu/genx/">GenX</a></b> (🥈19 ·  ⭐ 320) - Configurable capacity expansion model. <code><a href="http://bit.ly/2KucAZR">❗️GPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/GenXProject/GenX.jl) (👨‍💻 36 · 🔀 130 · 📋 310 - 17% open · ⏱️ 11.07.2025):

	```
	git clone https://github.com/GenXProject/GenX
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/reopt/">REopt</a></b> (🥈19 ·  ⭐ 110) - Renewable Energy Integration & Optimization. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL/REopt_API) (👨‍💻 23 · 🔀 59 · 📥 570 · 📋 97 - 57% open · ⏱️ 20.08.2025):

	```
	git clone https://github.com/NREL/REopt_API
	```
</details>
<details><summary><b><a href="https://l2rpn.chalearn.org/">LightSim2Grid</a></b> (🥈19 ·  ⭐ 57 · 📈) - A fast backend for the Grid2Op. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Grid2op/lightsim2grid) (👨‍💻 6 · 🔀 12 · 📥 300 · 📦 69 · 📋 55 - 30% open · ⏱️ 28.04.2025):

	```
	git clone https://github.com/BDonnot/lightsim2grid
	```
- [PyPi](https://pypi.org/project/LightSim2Grid) (📥 12K / month · 📦 23 · ⏱️ 28.04.2025):
	```
	pip install LightSim2Grid
	```
- [Docker Hub](https://hub.docker.com/r/bdonnot/lightsim2grid) (📥 400 · ⏱️ 01.02.2022):
	```
	docker pull bdonnot/lightsim2grid
	```
</details>
<details><summary><b><a href="https://www.gurobi.com/features/gurobi-optimods/">Gurobi OptiMods</a></b> (🥈18 ·  ⭐ 160) - Implemented optimization use cases using Gurobi. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Gurobi/gurobi-optimods) (👨‍💻 15 · 🔀 34 · 📦 9 · 📋 84 - 29% open · ⏱️ 12.03.2025):

	```
	git clone https://github.com/Gurobi/gurobi-optimods
	```
- [PyPi](https://pypi.org/project/gurobi-optimods) (📥 380 / month · ⏱️ 12.03.2025):
	```
	pip install gurobi-optimods
	```
</details>
<details><summary><b><a href="https://github.com/IIT-EnergySystemModels/openTEPES">openTEPES</a></b> (🥈18 ·  ⭐ 46) - Open Generation, Storage, and Transmission Operation.. <code><a href="http://bit.ly/3pwmjO5">❗️AGPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/IIT-EnergySystemModels/openTEPES) (👨‍💻 9 · 🔀 23 · 📥 120 · 📋 13 - 23% open · ⏱️ 27.08.2025):

	```
	git clone https://github.com/IIT-EnergySystemModels/openTEPES
	```
- [PyPi](https://pypi.org/project/openTEPES) (📥 330 / month · ⏱️ 24.06.2025):
	```
	pip install openTEPES
	```
</details>
<details><summary><b><a href="https://pypsa.org">PyPSA-USA</a></b> (🥉17 ·  ⭐ 92) - Power System Model for the United States. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/pypsa-usa) (👨‍💻 12 · 🔀 31 · 📋 360 - 25% open · ⏱️ 20.08.2025):

	```
	git clone https://github.com/PyPSA/pypsa-usa
	```
</details>
<details><summary><b><a href="https://github.com/pnnl/tesp">TESP</a></b> (🥉17 ·  ⭐ 45) - Transactive Energy Simulation Platform. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/pnnl/tesp) (👨‍💻 26 · 🔀 40 · 📥 500 · 📦 2 · 📋 130 - 25% open · ⏱️ 15.12.2024):

	```
	git clone https://github.com/pnnl/tesp
	```
- [PyPi](https://pypi.org/project/tesp_support) (📥 76 / month · ⏱️ 15.12.2024):
	```
	pip install tesp_support
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/analysis/reeds/">ReEDS-2.0</a></b> (🥉16 ·  ⭐ 160) - Capacity planning and dispatch model. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL/ReEDS-2.0) (👨‍💻 14 · 🔀 71 · 📋 25 - 12% open · ⏱️ 25.08.2025):

	```
	git clone https://github.com/NREL/ReEDS-2.0
	```
</details>
<details><summary><b><a href="https://ltb.curent.org/">LTB AMS</a></b> (🥉16 ·  ⭐ 18) - Scheduling Modeling and Simulation; CURENT LTB. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/azure.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CURENT/ams) (👨‍💻 4 · 🔀 8 · 📥 32 · 📦 3 · 📋 21 - 66% open · ⏱️ 18.08.2025):

	```
	git clone https://github.com/CURENT/ams
	```
- [PyPi](https://pypi.org/project/ltbams) (📥 300 / month · ⏱️ 18.08.2025):
	```
	pip install ltbams
	```
- [Conda](https://anaconda.org/conda-forge/ltbams) (📥 18K · ⏱️ 19.08.2025):
	```
	conda install -c conda-forge ltbams
	```
</details>
<details><summary><b><a href="https://github.com/grid-parity-exchange/Egret">EGRET</a></b> (🥉15 ·  ⭐ 140) - Tools for Power Systems Optimization Modeling. <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/grid-parity-exchange/Egret) (👨‍💻 39 · 🔀 54 · 📋 87 - 56% open · ⏱️ 20.06.2025):

	```
	git clone https://github.com/grid-parity-exchange/Egret
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/analysis/sienna.html">PowerNetworkMatrices.jl</a></b> (🥉15 ·  ⭐ 25) - Power systems matrices; NREL Sienna. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL-Sienna/PowerNetworkMatrices.jl) (👨‍💻 8 · 🔀 21 · 📋 85 - 47% open · ⏱️ 11.04.2025):

	```
	git clone https://github.com/NREL-Sienna/PowerNetworkMatrices.jl
	```
</details>
<details><summary><b><a href="https://www.powsybl.org">Open RAO</a></b> (🥉15 ·  ⭐ 24) - Power systems coordinated capacity calculation and.. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/powsybl/powsybl-open-rao) (👨‍💻 37 · 🔀 8 · 📥 52 · 📋 190 - 36% open · ⏱️ 28.08.2025):

	```
	git clone https://github.com/powsybl/powsybl-open-rao
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/analysis/sienna.html">PowerFlows.jl</a></b> (🥉15 ·  ⭐ 22) - Collection of Power Flow solution; NREL Sienna. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL-Sienna/PowerFlows.jl) (👨‍💻 11 · 🔀 22 · 📋 120 - 43% open · ⏱️ 05.05.2025):

	```
	git clone https://github.com/NREL-Sienna/PowerFlows.jl
	```
</details>
<details><summary><b><a href="https://github.com/ANL-CEEESA/UnitCommitment.jl">UnitCommitment.jl</a></b> (🥉14 ·  ⭐ 120) - Optimization package for the Security-Constrained.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ANL-CEEESA/UnitCommitment.jl) (👨‍💻 6 · 🔀 33 · 📋 8 - 12% open · ⏱️ 27.06.2025):

	```
	git clone https://github.com/ANL-CEEESA/UnitCommitment.jl
	```
</details>
<details><summary><b><a href="https://matpower.org/">MOST</a></b> (🥉14 ·  ⭐ 34) - MATPOWER Optimal Scheduling Tool. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/MATPOWER/most) (🔀 13 · 📋 45 - 17% open · ⏱️ 12.07.2025):

	```
	git clone https://github.com/MATPOWER/most
	```
</details>
<details><summary><b><a href="https://www.gridpath.io/">ExaGO</a></b> (🥉13 ·  ⭐ 86) - Large-scale power grid optimization. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/pnnl/ExaGO) (👨‍💻 32 · 🔀 14 · 📋 96 - 54% open · ⏱️ 24.07.2025):

	```
	git clone https://github.com/pnnl/ExaGO
	```
</details>
<details><summary><b><a href="https://github.com/felipemarkson/dssdata">DSSData</a></b> (🥉10 ·  ⭐ 16 · 💤) - A micro-framework for simulation and data analysis of.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/felipemarkson/dssdata) (👨‍💻 2 · 🔀 3 · 📥 56 · 📦 2 · 📋 36 - 13% open · ⏱️ 10.04.2023):

	```
	git clone https://github.com/felipemarkson/dssdata
	```
- [PyPi](https://pypi.org/project/dssdata) (📥 24 / month · ⏱️ 24.01.2023):
	```
	pip install dssdata
	```
</details>
<details><summary><b><a href="https://github.com/ebalogun01/EV-EcoSim">EV-EcoSim</a></b> (🥉9 ·  ⭐ 26 · 💤) - A grid-aware co-simulation platform for the design and.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ebalogun01/EV-EcoSim) (🔀 5 · 📋 72 - 12% open · ⏱️ 19.04.2024):

	```
	git clone https://github.com/ebalogun01/EV-EcoSim/
	```
</details>
<details><summary><b><a href="https://pypsa-meets-earth.github.io/">PyPSA-Distribution</a></b> (🥉9 ·  ⭐ 24) - Multi-energy model for small scale applications in.. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/pypsa-meets-earth/pypsa-distribution) (👨‍💻 7 · 🔀 11 · 📋 25 - 64% open · ⏱️ 31.05.2025):

	```
	git clone https://github.com/pypsa-meets-earth/pypsa-distribution
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/analysis/sienna.html">PowerSystemsInvestmentsPortfolios.jl</a></b> (🥉8 ·  ⭐ 12) - Data models for Power Systems investment models; NREL.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL-Sienna/PowerSystemsInvestmentsPortfolios.jl) (👨‍💻 5 · 🔀 8 · 📋 51 - 43% open · ⏱️ 04.08.2025):

	```
	git clone https://github.com/NREL-Sienna/PowerSystemsInvestmentsPortfolios.jl
	```
</details>
<details><summary><b><a href="https://www2.econ.iastate.edu/tesfatsi/AMESMarketHome.htm">AMES - Version 5.0</a></b> (🥉7 ·  ⭐ 27) - Wholesale Power Market Test Bed. <code><a href="https://github.com/ames-market/AMES-V5.0/blob/master/LICENSE.rst">❗️Custom</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ames-market/AMES-V5.0) (👨‍💻 3 · 🔀 6 · ⏱️ 16.05.2025):

	```
	git clone https://github.com/ames-market/AMES-V5.0
	```
</details>
<details><summary><b><a href="https://github.com/LBNL-ETA/DOPER">DOPER</a></b> (🥉7 ·  ⭐ 21) - Distributed Optimal and Predictive Energy Resources. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/LBNL-ETA/DOPER) (👨‍💻 3 · 🔀 11 · ⏱️ 30.01.2025):

	```
	git clone https://github.com/LBNL-ETA/DOPER
	```
</details>
<details><summary><b><a href="https://github.com/power-flow-analyzer/PowerFlowAnalyzer">PowerFlowAnalyzer</a></b> (🥉7 ·  ⭐ 6 · 💤) - Toolbox for power system analysis. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/power-flow-analyzer/PowerFlowAnalyzer) (👨‍💻 3 · 🔀 1 · 📥 180 · ⏱️ 16.05.2019):

	```
	git clone https://github.com/power-flow-analyzer/PowerFlowAnalyzer
	```
</details>
<details><summary><b><a href="https://github.com/ANL-CEEESA/EGRIP.jl">EGRIP.jl</a></b> (🥉6 ·  ⭐ 8) - Julia/MATALB package for power system restoration.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ANL-CEEESA/EGRIP.jl) (👨‍💻 5 · ⏱️ 06.05.2025):

	```
	git clone https://github.com/ANL-CEEESA/EGRIP.jl
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/analysis/sienna.html">PowerSystemsInvestments.jl</a></b> (🥉5 ·  ⭐ 20) - Power Systems investment models; NREL Sienna. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL-Sienna/PowerSystemsInvestments.jl) (👨‍💻 4 · 🔀 12 · 📋 29 - 93% open · ⏱️ 21.07.2025):

	```
	git clone https://github.com/NREL-Sienna/PowerSystemsInvestments.jl
	```
</details>
<details><summary><b><a href="https://github.com/yasirroni/mypower">mypower</a></b> (🥉5 ·  ⭐ 8 · 💤) - Supplementary function of MATPOWER in Python. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code>intf</code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/yasirroni/mypower) (🔀 1 · ⏱️ 26.11.2022):

	```
	git clone https://github.com/yasirroni/mypower
	```
</details>
<details><summary><b><a href="https://github.com/NREL/ASSET">ASSET</a></b> (🥉4 ·  ⭐ 14 · 🐣) - Assess and analyze grid strength. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL/ASSET) (👨‍💻 2 · 🔀 5 · ⏱️ 05.05.2025):

	```
	git clone https://github.com/NREL/ASSET
	```
</details>
<details><summary><b><a href="https://www2.econ.iastate.edu/tesfatsi/AMESMarketHome.htm">AMES (V4.0)</a></b> (🥉2 ·  ⭐ 13 · 💤) - Agent based Modeling of Electricity Systems. <code><a href="http://bit.ly/2KucAZR">❗️GPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ames-market/AMES-v4.0) (👨‍💻 2 · 🔀 7 · 📋 5 - 60% open · ⏱️ 28.08.2020):

	```
	git clone https://github.com/ames-market/AMES-v4.0
	```
</details>
<details><summary><b><a href="https://www.epri.com/pages/sa/opendss">OpenDSS</a></b> (🥉2) - Distribution system simulator. <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- _No project information available._</details>
<br>

## Interface

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/PauloRadatz/py_dss_interface">py-dss-interface</a></b> (🥇21 ·  ⭐ 33 · 📈) - A package for access to direct dll version of OpenDSS. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PauloRadatz/py_dss_interface) (👨‍💻 7 · 🔀 10 · 📥 15 · 📦 37 · ⏱️ 21.08.2025):

	```
	git clone https://github.com/PauloRadatz/py_dss_interface
	```
- [PyPi](https://pypi.org/project/py-dss-interface) (📥 2.8K / month · 📦 9 · ⏱️ 19.08.2025):
	```
	pip install py-dss-interface
	```
</details>
<details><summary><b><a href="https://dss-extensions.org/">OpenDSSDirect.py</a></b> (🥇19 ·  ⭐ 98 · 💤) - A direct library interface to OpenDSS. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dss-extensions/OpenDSSDirect.py) (👨‍💻 3 · 🔀 25 · 📦 76 · 📋 110 - 17% open · ⏱️ 29.03.2024):

	```
	git clone https://github.com/dss-extensions/OpenDSSDirect.py
	```
- [PyPi](https://pypi.org/project/OpenDSSDirect.py) (📥 4.6K / month · 📦 16 · ⏱️ 11.03.2021):
	```
	pip install OpenDSSDirect.py
	```
</details>
<details><summary><b><a href="https://github.com/sogno-platform/cimpy">CIMpy</a></b> (🥇18 ·  ⭐ 62) - CIM files to the XML/RDF format. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/sogno-platform/cimpy) (👨‍💻 11 · 🔀 23 · 📦 12 · 📋 24 - 50% open · ⏱️ 23.02.2025):

	```
	git clone https://github.com/sogno-platform/cimpy
	```
- [PyPi](https://pypi.org/project/cimpy) (📥 1.6K / month · 📦 1 · ⏱️ 20.06.2024):
	```
	pip install cimpy
	```
</details>
<details><summary><b><a href="https://github.com/mzy2240/ESA">Easy SimAuto</a></b> (🥈15 ·  ⭐ 47) - Python interface to PowerWorld. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/mzy2240/ESA) (👨‍💻 12 · 🔀 13 · 📦 7 · 📋 100 - 15% open · ⏱️ 16.01.2025):

	```
	git clone https://github.com/mzy2240/ESA
	```
- [PyPi](https://pypi.org/project/esa) (📥 830 / month · 📦 1 · ⏱️ 21.05.2022):
	```
	pip install esa
	```
</details>
<details><summary><b><a href="https://dss-extensions.org/">AltDSS/DSS C-API</a></b> (🥈15 ·  ⭐ 35 · 💤) - a plain C interface to OpenDSS. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dss-extensions/dss_capi) (👨‍💻 8 · 🔀 14 · 📥 29K · 📋 120 - 13% open · ⏱️ 11.07.2024):

	```
	git clone https://github.com/dss-extensions/dss_capi
	```
</details>
<details><summary><b><a href="https://github.com/ieeh-tu-dresden/powerfactory-tools">powerfactory-tools</a></b> (🥈15 ·  ⭐ 32) - Python toolbox for control of DIgSILENT PowerFactory. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ieeh-tu-dresden/powerfactory-tools) (👨‍💻 4 · 🔀 6 · 📥 360 · 📦 2 · 📋 180 - 9% open · ⏱️ 26.08.2025):

	```
	git clone https://github.com/ieeh-tu-dresden/powerfactory-tools
	```
- [PyPi](https://pypi.org/project/ieeh-powerfactory-tools) (📥 420 / month · ⏱️ 26.08.2025):
	```
	pip install ieeh-powerfactory-tools
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/grid/pydss.html">PyDSS</a></b> (🥈14 ·  ⭐ 39) - A Python wrapper for OpenDSS. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL/PyDSS) (👨‍💻 23 · 🔀 25 · 📦 2 · 📋 30 - 46% open · ⏱️ 30.09.2024):

	```
	git clone https://github.com/NREL/PyDSS
	```
- [PyPi](https://pypi.org/project/pydss) (📥 24 / month · ⏱️ 17.08.2011):
	```
	pip install pydss
	```
</details>
<details><summary><b><a href="https://github.com/UGM-EPSLab/matpowercaseframes">matpowercaseframes</a></b> (🥈14 ·  ⭐ 5) - Parse MATPOWER case into pandas DataFrame. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/UGM-EPSLab/matpowercaseframes) (👨‍💻 7 · 🔀 2 · 📋 5 - 40% open · ⏱️ 31.05.2025):

	```
	git clone https://github.com/UGM-EPSLab/matpowercaseframes
	```
- [PyPi](https://pypi.org/project/matpowercaseframes) (📥 9.5K / month · 📦 6 · ⏱️ 31.05.2025):
	```
	pip install matpowercaseframes
	```
</details>
<details><summary><b><a href="https://github.com/cimug-org/CIMTool">CIMTool</a></b> (🥈13 ·  ⭐ 57) - CIMugs CIMTool for the CIM. <code><a href="https://tldrlegal.com/search?q=LGPL-2.1">❗️LGPL-2.1</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cimug-org/CIMTool) (👨‍💻 17 · 🔀 7 · 📥 2.5K · 📋 98 - 35% open · ⏱️ 05.05.2025):

	```
	git clone https://github.com/CIMug-org/CIMTool
	```
</details>
<details><summary><b><a href="https://github.com/yasirroni/matpower-pip">matpower-pip</a></b> (🥈13 ·  ⭐ 25) - Easy Python Access to MATPOWER. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/yasirroni/matpower-pip) (👨‍💻 1 · 🔀 2 · 📦 9 · 📋 19 - 26% open · ⏱️ 15.08.2025):

	```
	git clone https://github.com/yasirroni/matpower-pip
	```
- [PyPi](https://pypi.org/project/matpower) (📥 370 / month · 📦 2 · ⏱️ 15.08.2025):
	```
	pip install matpower
	```
</details>
<details><summary><b><a href="https://github.com/lanl-ansi/grg-pssedata">grg-pssedata</a></b> (🥉12 ·  ⭐ 32 · 💤) - Python tools for working with PSSE v33 data files. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/lanl-ansi/grg-pssedata) (👨‍💻 3 · 🔀 14 · 📦 7 · 📋 13 - 23% open · ⏱️ 14.12.2020):

	```
	git clone https://github.com/lanl-ansi/grg-pssedata
	```
- [PyPi](https://pypi.org/project/grg-pssedata) (📥 78 / month · 📦 1 · ⏱️ 15.12.2020):
	```
	pip install grg-pssedata
	```
</details>
<details><summary><b><a href="https://dss-extensions.org/">OpenDSSDirect.jl</a></b> (🥉12 ·  ⭐ 29) - Cross-platform Julia interface to OpenDSS. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dss-extensions/OpenDSSDirect.jl) (👨‍💻 8 · 🔀 6 · 📋 47 - 25% open · ⏱️ 30.10.2024):

	```
	git clone https://github.com/dss-extensions/OpenDSSDirect.jl
	```
</details>
<details><summary><b><a href="https://dss-extensions.org/">AltDSS-Python</a></b> (🥉12 ·  ⭐ 17 · 💤) - Modern Python bindings for an alternative.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dss-extensions/AltDSS-Python) (🔀 1 · 📦 12 · 📋 9 - 77% open · ⏱️ 29.03.2024):

	```
	git clone https://github.com/dss-extensions/AltDSS-Python
	```
- [PyPi](https://pypi.org/project/altdss) (📥 760 / month · 📦 2 · ⏱️ 29.03.2024):
	```
	pip install altdss
	```
</details>
<details><summary><b><a href="https://github.com/RWTH-IAEW/cimpyorm">cimpyorm</a></b> (🥉11 ·  ⭐ 12 · 💤) - Python ORM middleware for IEC CIM and CGMES datasets. <code><a href="https://tldrlegal.com/search?q=BSD-3.0">❗️BSD-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/RWTH-IAEW/cimpyorm) (👨‍💻 5 · 🔀 5 · 📦 4 · 📋 3 - 33% open · ⏱️ 19.10.2023):

	```
	git clone https://github.com/RWTH-IAEW/cimpyorm
	```
- [PyPi](https://pypi.org/project/cimpyorm) (📥 5.5K / month · ⏱️ 19.10.2023):
	```
	pip install cimpyorm
	```
</details>
<details><summary><b><a href="https://www.pscad.com/">mhi-pscad</a></b> (🥉10) - PSCAD Automation library. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [PyPi](https://pypi.org/project/mhi-pscad) (📥 2.9K / month · 📦 1 · ⏱️ 07.08.2025):
	```
	pip install mhi-pscad
	```
</details>
<details><summary><b><a href="https://dss-extensions.org/">DSS MATLAB</a></b> (🥉8 ·  ⭐ 11) - MATLAB interface to OpenDSS. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dss-extensions/dss_matlab) (🔀 2 · 📥 1.2K · 📋 21 - 33% open · ⏱️ 30.10.2024):

	```
	git clone https://github.com/dss-extensions/dss_matlab
	```
</details>
<details><summary><b><a href="https://dss-extensions.org/">DSS Sharp</a></b> (🥉8 ·  ⭐ 10 · 💤) - C#/.NET wrapper library for DSS C-API. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dss-extensions/dss_sharp) (📥 55 · 📦 3 · 📋 15 - 20% open · ⏱️ 15.03.2024):

	```
	git clone https://github.com/dss-extensions/dss_sharp
	```
</details>
<details><summary><b><a href="https://github.com/cimug-org/CIMTool-Builders-Library">CIMTool-Builders-Library</a></b> (🥉8 ·  ⭐ 9) - Publically available XSLT builders. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cimug-org/CIMTool-Builders-Library) (👨‍💻 5 · 🔀 3 · ⏱️ 05.05.2025):

	```
	git clone https://github.com/CIMug-org/CIMTool-Builders-Library
	```
</details>
<details><summary><b><a href="https://github.com/anderson-optimization/em-psse">PSSE RAW</a></b> (🥉5 ·  ⭐ 35 · 💤) - PSSE RAW parser. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/anderson-optimization/em-psse) (👨‍💻 2 · 🔀 15 · ⏱️ 07.01.2020):

	```
	git clone https://github.com/anderson-optimization/em-psse
	```
</details>
<details><summary><b><a href="https://www.epri.com/OpenDER">OpenDER interface</a></b> (🥉5 ·  ⭐ 6) - Interface for OpenDER. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/epri-dev/OpenDER_interface) (👨‍💻 2 · 🔀 1 · ⏱️ 10.02.2025):

	```
	git clone https://github.com/epri-dev/OpenDER_interface
	```
</details>
<details><summary><b><a href="https://ltb.curent.org">Andes.jl</a></b> (🥉4 ·  ⭐ 8 · 💤) - Julia interface for ANDES. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cuihantao/Andes.jl) (🔀 1 · ⏱️ 05.02.2024):

	```
	git clone https://github.com/cuihantao/Andes.jl
	```
</details>
<details><summary><b><a href="https://github.com/mzy2240/EasySimauto.jl">EasySimauto.jl</a></b> (🥉3 ·  ⭐ 6 · 💤) - Julia interface for EasySimAuto and PowerWorld. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/mzy2240/EasySimauto.jl) (👨‍💻 2 · ⏱️ 31.07.2023):

	```
	git clone https://github.com/mzy2240/EasySimauto.jl
	```
</details>
<br>

## Gas Simulation

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://www.pandapipes.org/">pandapipes</a></b> (🥇27 ·  ⭐ 180 · 📈) - Pipeflow Calculation Tool. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/e2nIEE/pandapipes) (👨‍💻 28 · 🔀 71 · 📦 33 · 📋 170 - 49% open · ⏱️ 17.07.2025):

	```
	git clone https://github.com/e2nIEE/pandapipes
	```
- [PyPi](https://pypi.org/project/pandapipes) (📥 8.2K / month · 📦 10 · ⏱️ 27.06.2025):
	```
	pip install pandapipes
	```
</details>
<details><summary><b><a href="https://github.com/lanl-ansi/GasModels.jl">GasModels.jl</a></b> (🥉13 ·  ⭐ 72) - Gas Network Optimization. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/lanl-ansi/GasModels.jl) (👨‍💻 14 · 🔀 18 · 📋 150 - 35% open · ⏱️ 29.04.2025):

	```
	git clone https://github.com/lanl-ansi/GasModels.jl
	```
</details>
<details><summary><b><a href="https://matpower.org/">MPNG</a></b> (🥉7 ·  ⭐ 11 · 💤) - Simulator for Optimal Power and Natural Gas Flow. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/MATPOWER/mpng) (👨‍💻 3 · 🔀 5 · ⏱️ 13.09.2023):

	```
	git clone https://github.com/MATPOWER/mpng
	```
</details>
<br>

## Co-Simulation Environment

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://openmodelica.org">OpenModelica</a></b> (🥇27 ·  ⭐ 1K) - Modelica-based environment for modeling and simulation. <code><a href="https://modelica.org/licenses/ModelicaLicense2/">❗️Custom</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/modelica.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/OpenModelica/OpenModelica) (👨‍💻 200 · 🔀 320 · 📥 490 · 📋 8.4K - 24% open · ⏱️ 28.08.2025):

	```
	git clone https://github.com/OpenModelica/OpenModelica
	```
- [Docker Hub](https://hub.docker.com/r/openmodelica/openmodelica) (📥 54K · ⭐ 6 · ⏱️ 23.08.2025):
	```
	docker pull openmodelica/openmodelica
	```
</details>
<details><summary><b><a href="https://precice.org/">precice</a></b> (🥉26 ·  ⭐ 820) - Precise Code Interaction Coupling Environment. <code><a href="http://bit.ly/37RvQcA">❗️LGPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/precice/precice) (👨‍💻 59 · 🔀 190 · 📥 37K · 📋 930 - 21% open · ⏱️ 28.08.2025):

	```
	git clone https://github.com/precice/precice
	```
- [PyPi](https://pypi.org/project/pyprecice) (📥 1.1K / month · 📦 8 · ⏱️ 18.06.2025):
	```
	pip install pyprecice
	```
- [Conda](https://anaconda.org/conda-forge/pyprecice) (📥 120K · ⏱️ 18.06.2025):
	```
	conda install -c conda-forge pyprecice
	```
- [Docker Hub](https://hub.docker.com/r/precice/precice) (📥 29K · ⏱️ 28.08.2025):
	```
	docker pull precice/precice
	```
</details>
<br>

## Optimization Modeling Language

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/cvxpy/cvxpy">CVXPY</a></b> (🥇40 ·  ⭐ 5.9K) - Convex optimization modeling language. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cvxpy/cvxpy) (👨‍💻 230 · 🔀 1.1K · 📥 630 · 📦 18K · 📋 1.6K - 17% open · ⏱️ 27.08.2025):

	```
	git clone https://github.com/cvxpy/cvxpy
	```
- [PyPi](https://pypi.org/project/cvxpy) (📥 2.4M / month · 📦 740 · ⏱️ 24.08.2025):
	```
	pip install cvxpy
	```
- [Conda](https://anaconda.org/conda-forge/cvxpy) (📥 1.8M · ⏱️ 24.08.2025):
	```
	conda install -c conda-forge cvxpy
	```
</details>
<details><summary><b><a href="https://www.pyomo.org">Pyomo</a></b> (🥇40 ·  ⭐ 2.3K) - Python-based Optimization Modeling Language. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Pyomo/pyomo) (👨‍💻 180 · 🔀 550 · 📥 4.9K · 📦 4.6K · 📋 1.5K - 21% open · ⏱️ 28.08.2025):

	```
	git clone https://github.com/Pyomo/pyomo
	```
- [PyPi](https://pypi.org/project/Pyomo) (📥 630K / month · 📦 280 · ⏱️ 21.02.2025):
	```
	pip install Pyomo
	```
- [Conda](https://anaconda.org/conda-forge/pyomo) (📥 1.6M · ⏱️ 28.08.2025):
	```
	conda install -c conda-forge pyomo
	```
</details>
<details><summary><b><a href="https://cvxopt.org/">CVXOPT</a></b> (🥈27 ·  ⭐ 1K) - Python Software for Convex Optimization. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cvxopt/cvxopt) (👨‍💻 10 · 🔀 210 · 📦 15K · 📋 200 - 23% open · ⏱️ 16.06.2025):

	```
	git clone https://github.com/cvxopt/cvxopt
	```
- [PyPi](https://pypi.org/project/cvxopt) (📥 650K / month · 📦 450 · ⏱️ 09.08.2023):
	```
	pip install cvxopt
	```
- [Conda](https://anaconda.org/conda-forge/cvxopt) (📥 1.6M · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge cvxopt
	```
</details>
<details><summary><b><a href="https://jump.dev">JuMP</a></b> (🥉25 ·  ⭐ 2.3K) - Julia-based Optimization Modeling Language. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/jump-dev/JuMP.jl) (👨‍💻 160 · 🔀 410 · 📋 1.5K - 0% open · ⏱️ 28.08.2025):

	```
	git clone https://github.com/jump-dev/JuMP.jl
	```
</details>
<details><summary><b><a href="https://github.com/metab0t/PyOptInterface">PyOptInterface</a></b> (🥉20 ·  ⭐ 280) - Efficient modeling interface for optimization in.. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/metab0t/PyOptInterface) (👨‍💻 2 · 🔀 17 · 📦 20 · 📋 35 - 22% open · ⏱️ 12.08.2025):

	```
	git clone https://github.com/metab0t/PyOptInterface
	```
- [PyPi](https://pypi.org/project/pyoptinterface) (📥 3K / month · 📦 6 · ⏱️ 08.08.2025):
	```
	pip install pyoptinterface
	```
</details>
<details><summary><b><a href="https://github.com/XiongPengNUS/rsome">RSOME</a></b> (🥉16 ·  ⭐ 330) - Robust Stochastic Optimization Made Easy. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/XiongPengNUS/rsome) (👨‍💻 3 · 🔀 59 · 📋 45 - 15% open · ⏱️ 15.11.2024):

	```
	git clone https://github.com/XiongPengNUS/rsome
	```
- [PyPi](https://pypi.org/project/rsome) (📥 640 / month · 📦 4 · ⏱️ 29.10.2024):
	```
	pip install rsome
	```
</details>
<details><summary><b><a href="https://github.com/sanurielf/kvxopt">KVXOPT</a></b> (🥉16 ·  ⭐ 12) - CVXOPT with more wrappers suite-sparse. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/sanurielf/kvxopt) (👨‍💻 16 · 🔀 1 · 📦 31 · ⏱️ 20.06.2025):

	```
	git clone https://github.com/sanurielf/kvxopt
	```
- [PyPi](https://pypi.org/project/kvxopt) (📥 4.1K / month · 📦 14 · ⏱️ 20.06.2025):
	```
	pip install kvxopt
	```
- [Conda](https://anaconda.org/conda-forge/kvxopt) (📥 340K · ⏱️ 20.06.2025):
	```
	conda install -c conda-forge kvxopt
	```
</details>
<details><summary><b><a href="https://github.com/exanauts/ExaModels.jl">ExaModels</a></b> (🥉15 ·  ⭐ 63) - An algebraic modeling and automatic differentiation tool.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/exanauts/ExaModels.jl) (👨‍💻 9 · 🔀 8 · 📋 38 - 31% open · ⏱️ 25.08.2025):

	```
	git clone https://github.com/exanauts/ExaModels.jl
	```
</details>
<br>

## Optimizer

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://developers.google.com/optimization/">OR-Tools</a></b> (🥇40 ·  ⭐ 12K) - Google Optimization Tools. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/google/or-tools) (👨‍💻 190 · 🔀 2.3K · 📥 950K · 📦 350 · 📋 3.1K - 1% open · ⏱️ 12.08.2025):

	```
	git clone https://github.com/google/or-tools
	```
- [PyPi](https://pypi.org/project/ortools) (📥 2.4M / month · 📦 310 · ⏱️ 19.06.2025):
	```
	pip install ortools
	```
- [Conda](https://anaconda.org/conda-forge/ortools-python) (📥 120K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge ortools-python
	```
</details>
<details><summary><b><a href="https://github.com/google/or-tools">Xopt</a></b> (🥇38 ·  ⭐ 12K) - Flexible high-level optimization in Python. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/google/or-tools) (👨‍💻 190 · 🔀 2.3K · 📥 950K · 📦 350 · 📋 3.1K - 1% open · ⏱️ 12.08.2025):

	```
	git clone https://github.com/google/or-tools
	```
- [PyPi](https://pypi.org/project/xopt) (📥 540 / month · 📦 3 · ⏱️ 27.08.2025):
	```
	pip install xopt
	```
- [Conda](https://anaconda.org/conda-forge/xopt) (📥 58K · ⏱️ 28.08.2025):
	```
	conda install -c conda-forge xopt
	```
</details>
<details><summary><b><a href="https://github.com/google/or-tools">Tulip</a></b> (🥈36 ·  ⭐ 12K) - Interior-point solver in pure Julia. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/google/or-tools) (👨‍💻 190 · 🔀 2.3K · 📥 950K · 📦 350 · 📋 3.1K - 1% open · ⏱️ 12.08.2025):

	```
	git clone https://github.com/google/or-tools
	```
</details>
<details><summary><b><a href="https://highs.dev/">HiGHS</a></b> (🥈34 ·  ⭐ 1.3K) - Large-scale Sparse Linear Problem Optimizer. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/rust.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/r.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/cpp.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ERGO-Code/HiGHS) (👨‍💻 91 · 🔀 240 · 📥 8.3K · 📋 930 - 12% open · ⏱️ 17.07.2025):

	```
	git clone https://github.com/ERGO-Code/HiGHS
	```
- [PyPi](https://pypi.org/project/highspy) (📥 450K / month · 📦 79 · ⏱️ 06.06.2025):
	```
	pip install highspy
	```
- [Conda](https://anaconda.org/conda-forge/highs) (📥 31K · ⏱️ 06.06.2025):
	```
	conda install -c conda-forge highs
	```
</details>
<details><summary><b><a href="https://osqp.org">OSQP</a></b> (🥈31 ·  ⭐ 1.9K) - Operator Splitting QP Solver. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/r.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/osqp/osqp) (👨‍💻 36 · 🔀 370 · 📥 130K · 📋 380 - 26% open · ⏱️ 25.08.2025):

	```
	git clone https://github.com/osqp/osqp
	```
- [PyPi](https://pypi.org/project/osqp) (📥 2.4M / month · 📦 110 · ⏱️ 08.05.2025):
	```
	pip install osqp
	```
- [Conda](https://anaconda.org/conda-forge/osqp) (📥 1.3M · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge osqp
	```
</details>
<details><summary><b><a href="https://www.scipopt.org/">PySCIPOpt</a></b> (🥈31 ·  ⭐ 920) - Python interface for SCIP. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/scipopt/PySCIPOpt) (👨‍💻 83 · 🔀 270 · 📦 390 · 📋 600 - 6% open · ⏱️ 19.08.2025):

	```
	git clone https://github.com/scipopt/PySCIPOpt
	```
- [PyPi](https://pypi.org/project/PySCIPOpt) (📥 110K / month · 📦 70 · ⏱️ 25.08.2025):
	```
	pip install PySCIPOpt
	```
- [Conda](https://anaconda.org/conda-forge/pyscipopt) (📥 550K · ⏱️ 27.08.2025):
	```
	conda install -c conda-forge pyscipopt
	```
</details>
<details><summary><b><a href="https://github.com/cvxgrp/scs">SCS</a></b> (🥈29 ·  ⭐ 580) - Splitting Conic Solver. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/r.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cvxgrp/scs) (👨‍💻 33 · 🔀 140 · 📋 190 - 22% open · ⏱️ 12.08.2025):

	```
	git clone https://github.com/cvxgrp/scs
	```
- [PyPi](https://pypi.org/project/scs) (📥 2.1M / month · 📦 59 · ⏱️ 10.08.2025):
	```
	pip install scs
	```
- [Conda](https://anaconda.org/conda-forge/scs) (📥 1.4M · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge scs
	```
</details>
<details><summary><b><a href="https://www.coin-or.org/">Ipopt</a></b> (🥉28 ·  ⭐ 1.6K) - COIN-OR Interior Point Optimizer. <code><a href="http://bit.ly/2M0xmjV">EPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/coin-or/Ipopt) (👨‍💻 36 · 🔀 300 · 📥 23K · 📋 620 - 1% open · ⏱️ 21.08.2025):

	```
	git clone https://github.com/coin-or/Ipopt
	```
- [PyPi](https://pypi.org/project/ipopt) (📥 1.2K / month · 📦 10 · ⏱️ 07.04.2021):
	```
	pip install ipopt
	```
- [Conda](https://anaconda.org/conda-forge/ipopt) (📥 1.8M · ⏱️ 18.08.2025):
	```
	conda install -c conda-forge ipopt
	```
</details>
<details><summary><b><a href="https://github.com/oxfordcontrol/Clarabel.rs">Clarabel.rs</a></b> (🥉25 ·  ⭐ 460) - Interior-point solver for convex conic optimisation.. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/rust.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/oxfordcontrol/Clarabel.rs) (👨‍💻 11 · 🔀 35 · 📦 42 · 📋 60 - 21% open · ⏱️ 11.06.2025):

	```
	git clone https://github.com/oxfordcontrol/Clarabel.rs
	```
- [PyPi](https://pypi.org/project/clarabel) (📥 1.8M / month · 📦 43 · ⏱️ 11.06.2025):
	```
	pip install clarabel
	```
- [Conda](https://anaconda.org/conda-forge/clarabel) (📥 250K · ⏱️ 12.06.2025):
	```
	conda install -c conda-forge clarabel
	```
</details>
<details><summary><b><a href="https://github.com/embotech/ecos">ECOS</a></b> (🥉24 ·  ⭐ 520 · 💤) - Conic solver for second-order cone programming. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/r.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/embotech/ecos) (👨‍💻 40 · 🔀 120 · 📋 160 - 40% open · ⏱️ 04.01.2022):

	```
	git clone https://github.com/embotech/ecos
	```
- [PyPi](https://pypi.org/project/ecos) (📥 770K / month · 📦 49 · ⏱️ 18.06.2024):
	```
	pip install ecos
	```
- [Conda](https://anaconda.org/conda-forge/ecos) (📥 1.1M · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge ecos
	```
</details>
<details><summary><b><a href="https://www.coin-or.org/">CBC</a></b> (🥉23 ·  ⭐ 930) - COIN-OR Branch-and-Cut solver. <code><a href="http://bit.ly/2M0xmjV">EPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/coin-or/Cbc) (👨‍💻 35 · 🔀 120 · 📥 160K · 📋 530 - 28% open · ⏱️ 22.08.2025):

	```
	git clone https://github.com/coin-or/Cbc
	```
- [Conda](https://anaconda.org/conda-forge/coincbc) (📥 1.4M · ⏱️ 02.08.2025):
	```
	conda install -c conda-forge coincbc
	```
</details>
<details><summary><b><a href="https://www.coin-or.org/">Clp</a></b> (🥉23 ·  ⭐ 930) - COIN-OR Linear Programming Solver. <code><a href="http://bit.ly/2M0xmjV">EPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/coin-or/Cbc) (👨‍💻 35 · 🔀 120 · 📥 160K · 📋 530 - 28% open · ⏱️ 22.08.2025):

	```
	git clone https://github.com/coin-or/Cbc
	```
- [Conda](https://anaconda.org/conda-forge/coin-or-clp) (📥 1.1M · ⏱️ 02.08.2025):
	```
	conda install -c conda-forge coin-or-clp
	```
</details>
<details><summary><b><a href="https://ampl.com/">AMPLPY</a></b> (🥉22 ·  ⭐ 81) - Python API for AMPL. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ampl/amplpy) (👨‍💻 9 · 🔀 20 · 📦 130 · ⏱️ 09.07.2025):

	```
	git clone https://github.com/ampl/amplpy
	```
- [PyPi](https://pypi.org/project/amplpy) (📥 33K / month · 📦 8 · ⏱️ 09.07.2025):
	```
	pip install amplpy
	```
- [Conda](https://anaconda.org/conda-forge/amplpy) (📥 460K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge amplpy
	```
</details>
<details><summary><b><a href="https://github.com/PREDICT-EPFL/piqp">PIQP</a></b> (🥉21 ·  ⭐ 120) - Proximal Interior Point Quadratic Programming solver. <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/r.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PREDICT-EPFL/piqp) (👨‍💻 5 · 🔀 17 · 📥 820 · 📦 47 · 📋 17 - 17% open · ⏱️ 22.08.2025):

	```
	git clone https://github.com/PREDICT-EPFL/piqp
	```
- [PyPi](https://pypi.org/project/piqp) (📥 13K / month · 📦 9 · ⏱️ 22.08.2025):
	```
	pip install piqp
	```
- [Conda](https://anaconda.org/conda-forge/piqp) (📥 240K · ⏱️ 22.08.2025):
	```
	conda install -c conda-forge piqp
	```
</details>
<details><summary><b><a href="https://github.com/MadNLP/MadNLP.jl">MadNLP</a></b> (🥉16 ·  ⭐ 210) - A solver for nonlinear programming with GPU support. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/MadNLP/MadNLP.jl) (👨‍💻 16 · 🔀 19 · 📋 100 - 33% open · ⏱️ 24.08.2025):

	```
	git clone https://github.com/MadNLP/MadNLP.jl
	```
</details>
<details><summary><b><a href="https://github.com/oxfordcontrol/Clarabel.jl">Clarabel.jl</a></b> (🥉15 ·  ⭐ 220 · 📉) - Interior-point solver for convex conic optimisation.. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/oxfordcontrol/Clarabel.jl) (👨‍💻 12 · 🔀 21 · 📋 63 - 14% open · ⏱️ 25.08.2025):

	```
	git clone https://github.com/oxfordcontrol/Clarabel.jl
	```
</details>
<details><summary><b><a href="https://www.opti-verse.org/">OptiVerse</a></b> (🥉7 ·  ⭐ 12) - A library with innovative optimization solutions. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/feyntech-opt/OptiVerse) (👨‍💻 5 · 🔀 12 · ⏱️ 15.02.2025):

	```
	git clone https://github.com/feyntech-opt/OptiVerse
	```
</details>
<br>

## Machine/Reinforcement Learning for Power Grid

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://l2rpn.chalearn.org/">Grid2Op</a></b> (🥇26 ·  ⭐ 370) - Modeling sequential decision making in power systems. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Grid2op/grid2op) (👨‍💻 32 · 🔀 130 · 📋 380 - 14% open · ⏱️ 28.08.2025):

	```
	git clone https://github.com/rte-france/Grid2Op
	```
- [PyPi](https://pypi.org/project/Grid2Op) (📥 4.7K / month · 📦 23 · ⏱️ 24.07.2025):
	```
	pip install Grid2Op
	```
- [Docker Hub](https://hub.docker.com/r/bdonnot/grid2op) (📥 10K · ⭐ 1 · ⏱️ 05.07.2022):
	```
	docker pull bdonnot/grid2op
	```
</details>
<details><summary><b><a href="https://github.com/RLGC-Project/RLGC">RLGC</a></b> (🥈9 ·  ⭐ 130 · 💤) - RL for Grid Control (RLGC). <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/RLGC-Project/RLGC) (👨‍💻 4 · 🔀 31 · 📋 15 - 33% open · ⏱️ 08.04.2022):

	```
	git clone https://github.com/RLGC-Project/RLGC
	```
</details>
<details><summary><b><a href="https://github.com/JarvisETHZ/Daline">Daline</a></b> (🥉7 ·  ⭐ 21) - A Data-driven Power Flow Linearization Toolbox. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/JarvisETHZ/Daline) (👨‍💻 1 · 📥 6 · ⏱️ 26.04.2025):

	```
	git clone https://github.com/JarvisETHZ/Daline
	```
</details>
<details><summary><b><a href="https://github.com/cuihantao/andes_gym">andes_gym</a></b> (🥉4 ·  ⭐ 10 · 💤) - ANDES RL Environment for OpenAI Gym. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cuihantao/andes_gym) (👨‍💻 2 · 🔀 5 · ⏱️ 28.01.2022):

	```
	git clone https://github.com/cuihantao/andes_gym
	```
</details>
<br>

## Visualization

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://www.powsybl.org">PowSyBl Diagram</a></b> (🥇18 ·  ⭐ 94) - single-line substation diagrams and network graph.. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/powsybl/powsybl-diagram) (👨‍💻 29 · 🔀 16 · 📦 32 · 📋 190 - 37% open · ⏱️ 22.07.2025):

	```
	git clone https://github.com/powsybl/powsybl-diagram
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/analysis/sienna.html">PowerGraphics.jl</a></b> (🥉13 ·  ⭐ 31) - Visualization for PowerSimulations; NREL Sienna. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL-Sienna/PowerGraphics.jl) (👨‍💻 11 · 🔀 18 · 📋 39 - 38% open · ⏱️ 19.03.2025):

	```
	git clone https://github.com/NREL-Sienna/powergraphics.jl
	```
</details>
<details><summary><b><a href="https://ltb.curent.org/">LTB AGVis</a></b> (🥉11 ·  ⭐ 8 · 💤) - Geographical Visualization for Power Grid; CURENT LTB. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CURENT/agvis) (👨‍💻 10 · 🔀 5 · 📥 18 · 📦 3 · 📋 25 - 36% open · ⏱️ 07.06.2024):

	```
	git clone https://github.com/CURENT/agvis
	```
- [PyPi](https://pypi.org/project/agvis) (📥 53 / month · ⏱️ 07.06.2024):
	```
	pip install agvis
	```
</details>
<br>

## Messaging Environment

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://helics.org/tools/">HELICS</a></b> (🥇21 ·  ⭐ 140) - Co-simulation framework. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/java.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/GMLC-TDC/HELICS) (👨‍💻 39 · 🔀 46 · 📥 28K · 📋 680 - 13% open · ⏱️ 16.08.2025):

	```
	git clone https://github.com/GMLC-TDC/HELICS
	```
- [PyPi](https://pypi.org/project/helics) (📥 3.8K / month · 📦 13 · ⏱️ 28.02.2025):
	```
	pip install helics
	```
- [Conda](https://anaconda.org/conda-forge/helics) (📥 21K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge helics
	```
</details>
<details><summary><b><a href="https://ltb.curent.org/">LTB DiME</a></b> (🥉7 ·  ⭐ 3 · 💤) - Distributed Messaging Environment; CURENT LTB. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/c.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/octave.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CURENT/dime) (👨‍💻 4 · 🔀 2 · 📋 48 - 27% open · ⏱️ 31.07.2023):

	```
	git clone https://github.com/CURENT/dime
	```
</details>
<br>

## Power System Data

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

🔗&nbsp;<b><a href="https://github.com/Team-Nando/MV-LV-Networks">Australian MV-LV Networks</a></b> ( ⭐ 28 · 💤)  - Large-scale three-phase Australian MV distribution.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://power-grid-lib.github.io">Power Grid Lib - Optimal Power Flow</a></b> ( ⭐ 350 · 💤)  - Benchmarks for OPF. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://power-grid-lib.github.io">Power Grid Lib - Unit Commitment</a></b> ( ⭐ 99 · 💤)  - Benchmarks for UC. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://power-grid-lib.github.io">Power Grid Lib - Optimal Power Flow with HVDC Lines</a></b> ( ⭐ 24 · 💤)  - Benchmarks for OPF with HVDC. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/enliten/ENLITEN-Grid-Econ-Data">WECC-and-NPCC-Electricity-Economic-Data</a></b> ( ⭐ 9 · 💤)  - Economic data on WECC and NPCC. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://opendata.elia.be/pages/home/">OpenDataElia</a></b>  - Data by opendatasoft. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/owid/energy-data">Data on Energy</a></b> ( ⭐ 340)  - Data on energy by Our World in Data. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/non-profit2.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/tamu-engineering-research/COVID-EMDA">COVID-EMDA</a></b> ( ⭐ 61 · 💤)  - Cross-Domain Data Hub with Data in USA. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/rte-france/digital-fault-recording-database">Electrical Signals Databases</a></b> ( ⭐ 29)  - Voltage and current samples from Digital Fault Recorder. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/lbl-hub/CSEE-Benchmark">A new power system benchmark</a></b> ( ⭐ 31)  - A new type of power system calculation example by the.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/NanpengYu/pmuBAGE">pmuBAGE</a></b> ( ⭐ 9 · 💤)  - Synthetic phasor measurement unit dataset. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

<details><summary><b><a href="https://www.gridstatus.io">GridStatus</a></b> (🥇25 ·  ⭐ 350 · 📈) - Extract data from ISOs and other sources. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/gridstatus/gridstatus) (👨‍💻 33 · 🔀 68 · 📦 24 · 📋 120 - 32% open · ⏱️ 28.08.2025):

	```
	git clone https://github.com/kmax12/gridstatus
	```
- [PyPi](https://pypi.org/project/gridstatus) (📥 34K / month · 📦 2 · ⏱️ 12.08.2025):
	```
	pip install gridstatus
	```
- [Conda](https://anaconda.org/services/gridstatus) (📥 31 · ⏱️ 25.03.2025):
	```
	conda install -c services gridstatus
	```
</details>
<details><summary><b><a href="https://pypsa.org">Atlite</a></b> (🥈23 ·  ⭐ 330) - Calculating Renewable Power Potentials. <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/atlite) (👨‍💻 42 · 🔀 110 · 📦 110 · 📋 150 - 28% open · ⏱️ 24.07.2025):

	```
	git clone https://github.com/PyPSA/atlite
	```
- [PyPi](https://pypi.org/project/atlite) (📥 2.3K / month · ⏱️ 12.05.2025):
	```
	pip install atlite
	```
- [Conda](https://anaconda.org/conda-forge/atlite) (📥 95K · ⏱️ 11.08.2025):
	```
	conda install -c conda-forge atlite
	```
</details>
<details><summary><b><a href="https://pypsa.org">powerplantmatching</a></b> (🥈23 ·  ⭐ 190) - Tools to combine multiple power plant databases. <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/powerplantmatching) (👨‍💻 34 · 🔀 68 · 📥 87 · 📦 85 · 📋 110 - 29% open · ⏱️ 27.08.2025):

	```
	git clone https://github.com/PyPSA/powerplantmatching
	```
- [PyPi](https://pypi.org/project/powerplantmatching) (📥 1.1K / month · ⏱️ 01.02.2025):
	```
	pip install powerplantmatching
	```
- [Conda](https://anaconda.org/conda-forge/powerplantmatching) (📥 86K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge powerplantmatching
	```
</details>
<details><summary><b><a href="https://simbench.de/en/">SimBench</a></b> (🥉19 ·  ⭐ 120) - Benchmark dataset of German LV/MV/HV grids including.. <code><a href="https://tldrlegal.com/search?q=odbl-1.0">❗️odbl-1.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code>juptyer</code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/e2nIEE/simbench) (👨‍💻 4 · 🔀 30 · 📦 47 · 📋 35 - 8% open · ⏱️ 13.04.2025):

	```
	git clone https://github.com/e2nIEE/simbench
	```
- [PyPi](https://pypi.org/project/simbench) (📥 4.1K / month · 📦 10 · ⏱️ 13.04.2025):
	```
	pip install simbench
	```
- [Conda](https://anaconda.org/conda-forge/simbench):
	```
	conda install -c conda-forge simbench
	```
</details>
<details><summary><b><a href="https://groups.io/g/powergenome">PowerGenome</a></b> (🥉18 ·  ⭐ 220) - Create inputs for power systems models. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/anaconda.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PowerGenome/PowerGenome) (👨‍💻 18 · 🔀 72 · 📋 190 - 51% open · ⏱️ 21.03.2025):

	```
	git clone https://github.com/PowerGenome/PowerGenome
	```
- [PyPi](https://pypi.org/project/PowerGenome) (📥 39 / month · ⏱️ 21.03.2025):
	```
	pip install PowerGenome
	```
- [Conda](https://anaconda.org/conda-forge/powergenome) (📥 1.2K · ⏱️ 22.04.2025):
	```
	conda install -c conda-forge powergenome
	```
</details>
<details><summary><b><a href="https://www.energydatamodel.org/">EnergyDataModel</a></b> (🥉12 ·  ⭐ 67) - Represent energy systems as Python data classes. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/for-profit.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/rebase-energy/EnergyDataModel) (👨‍💻 3 · 🔀 5 · ⏱️ 07.04.2025):

	```
	git clone https://github.com/rebase-energy/EnergyDataModel
	```
- [PyPi](https://pypi.org/project/energydatamodel) (📥 37 / month · 📦 2 · ⏱️ 23.03.2025):
	```
	pip install energydatamodel
	```
</details>
<details><summary><b><a href="https://deepsolar.web.app">DeepSolar</a></b> (🥉9 ·  ⭐ 260 · 💤) - Houseshold-level solar panel identification with deep.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/wangzhecheng/DeepSolar) (👨‍💻 2 · 🔀 71 · 📋 17 - 76% open · ⏱️ 26.03.2019):

	```
	git clone https://github.com/wangzhecheng/DeepSolar
	```
</details>
<br>

## Power Electronics

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/gseim/gseim">GSEIM</a></b> (🥇6 ·  ⭐ 2 · 💤) - Simulation of electrical circuits. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/gseim/gseim) (👨‍💻 1):

	```
	git clone https://github.com/gseim/gseim
	```
- [PyPi](https://pypi.org/project/GSEIM) (📥 5 / month · ⏱️ 16.07.2022):
	```
	pip install GSEIM
	```
</details>
<br>

## Database Management

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/dsgrid/dsgrid">dsgrid</a></b> (🥇17 ·  ⭐ 100) - Demand-side grid projects, datasets and queries. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dsgrid/dsgrid) (👨‍💻 6 · 🔀 29 · 📋 130 - 40% open · ⏱️ 15.08.2025):

	```
	git clone https://github.com/dsgrid/dsgrid
	```
- [PyPi](https://pypi.org/project/dsgrid) (📥 13 / month · ⏱️ 18.12.2014):
	```
	pip install dsgrid
	```
</details>
<details><summary><b><a href="https://github.com/NREL/dgen">dGen</a></b> (🥉16 ·  ⭐ 69) - The Distributed Generation Market Demand (dGen) model. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/lab.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL/dgen) (👨‍💻 12 · 🔀 160 · 📋 51 - 58% open · ⏱️ 22.07.2025):

	```
	git clone https://github.com/NREL/dgen
	```
</details>
<br>

## Textbook

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

🔗&nbsp;<b><a href="https://powercybertraining.github.io">PowerCyber Training</a></b> ( ⭐ 3)  - PowerCyber Training modules source. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/Power-Systems-Textbook/TextbookSimulations">TextbookSimulations</a></b> ( ⭐ 12 · 💤)  - Examples and problems accompanying Daniel Kirschens.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/CURENT/ece522">UTK ECE 522 - Power System Analysis II</a></b> ( ⭐ 6)  - Hands-on Project for Power System Analysis II (UTK.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/bcornelusse/ELEC0447-analysis-power-systems">ELEC0447 Analysis of Electric Power and Energy Systems</a></b> ( ⭐ 24)  - Masters course of power systems analysis at ULige. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/Team-Nando/Tutorial-DERHostingCapacity-0-dss_python">Tutorial on DER Hosting Capacity Part 0</a></b> ( ⭐ 5)  - Using dss_python. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/Team-Nando/Tutorial-DERHostingCapacity-1-AdvancedTools_LV">Tutorial on DER Hosting Capacity Part 1</a></b> ( ⭐ 3)  - Advanced Tools for the Analysis of Three-Phase.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/Team-Nando/Tutorial-DERHostingCapacity-2-TimeSeries_LV">Tutorial on DER Hosting Capacity Part 2</a></b> ( ⭐ 2)  - Time-Series Analysis and PV Hosting Capacity of LV.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/Team-Nando/Tutorial-DERHostingCapacity-3-VoltWatt_LV">Tutorial on DER Hosting Capacity Part 3</a></b> ( ⭐ 1)  - Volt-Watt Control and PV Hosting Capacity of LV.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/Team-Nando/Tutorial-DERHostingCapacity-4-MonteCarlo_MV-LV">Tutorial on DER Hosting Capacity Part 4</a></b> ( ⭐ 2)  - Monte Carlo Assessment of PV Hosting Capacity of an.. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://ltb.curent.org">LTB Demo</a></b> ( ⭐ 2)  - Ready-to-use LTB usage examples. <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code>

<details><summary><b><a href="https://colib.net/">COLIB</a></b> (🥇7 ·  ⭐ 12) - Collaborative dynamic library. <code><a href="https://tldrlegal.com/search?q=CC-BY-4.0">❗️CC-BY-4.0</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/github.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CRESYM/colib0.github.io) (👨‍💻 12 · 🔀 4 · 📋 130 - 9% open · ⏱️ 12.05.2025):

	```
	git clone https://github.com/CRESYM/colib0.github.io
	```
</details>
<br>

## Large Language Model

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://power-agent.github.io">PowerMCP</a></b> (🥇9 ·  ⭐ 47 · 🐣) - Collection of MCP servers for power system software. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Power-Agent/PowerMCP) (👨‍💻 4 · 🔀 10 · ⏱️ 24.08.2025):

	```
	git clone https://github.com/Power-Agent/PowerMCP
	```
</details>
<details><summary><b><a href="https://github.com/cdgaete/pypsa-mcp">PyPSA MCP</a></b> (🥈8 ·  ⭐ 44 · 🐣) - PyPSA Energy Modeling for LLMs. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/pypi2.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/volunteer.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cdgaete/pypsa-mcp) (👨‍💻 2 · 🔀 3 · 📥 2 · ⏱️ 22.04.2025):

	```
	git clone https://github.com/cdgaete/pypsa-mcp
	```
- [PyPi](https://pypi.org/project/pypsamcp) (📥 26 / month · ⏱️ 22.04.2025):
	```
	pip install pypsamcp
	```
</details>
<details><summary><b><a href="https://power-agent.github.io">PowerWorkflow</a></b> (🥉7 ·  ⭐ 24 · 🐣) - Collection of agentic workflows for power system.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Power-Agent/PowerWF) (⏱️ 19.07.2025):

	```
	git clone https://github.com/Power-Agent/PowerWF
	```
</details>
<details><summary><b><a href="https://ltb.curent.org/">P-V Curve LLM</a></b> (🥉7 ·  ⭐ 2 · 🐣) - Using LLMs in Power-Voltage Curves for Voltage.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/python.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CURENT/pv-curve-llm) (⏱️ 19.08.2025):

	```
	git clone https://github.com/CURENT/pv-curve-llm
	```
</details>
<details><summary><b><a href="https://power-agent.github.io">PowerFM</a></b> (🥉5 ·  ⭐ 26 · 🐣) - Foundation models in the power and energy domain. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://github.com/ps-wiki/best-of-ps/blob/main/config/icons/university.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Power-Agent/PowerFM) (⏱️ 19.07.2025):

	```
	git clone https://github.com/Power-Agent/PowerFM
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
