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
    <a href="#Contents" title="Project Count"><img src="https://img.shields.io/badge/projects-48-blue.svg?color=5ac4bf"></a>
    <a href="#Contribution" title="Contributions are welcome"><img src="https://img.shields.io/badge/contributions-welcome-green.svg"></a>
    <a href="https://github.com/jinningwang/best-of-ps/releases" title="Best-of Updates"><img src="https://img.shields.io/github/release-date/jinningwang/best-of-ps?color=green&label=updated"></a>
</p>

This curated list contains 48 open-source projects with a total of 12K stars grouped into 14 categories. All projects are ranked by a project-popular score, which is calculated based on various metrics automatically collected from GitHub and different package managers. If you like to add or update projects, feel free to open an [issue](https://github.com/jinningwang/best-of-ps/issues/new/choose), submit a [pull request](https://github.com/jinningwang/best-of-ps/pulls), or directly edit the [projects.yaml](https://github.com/jinningwang/best-of-ps/edit/main/projects.yaml). Contributions are very welcome!

## Contents

- [Dynamic](#dynamic) _6 projects_
- [Steady State](#steady-state) _13 projects_
- [Power System Co-Simulation](#power-system-co-simulation) _1 projects_
- [Co-Simulation Framework](#co-simulation-framework) _1 projects_
- [Interface](#interface) _4 projects_
- [Optimization Solver](#optimization-solver) _2 projects_
- [Optimization Modeling Language](#optimization-modeling-language) _2 projects_
- [Machine/Reinforcement Learning](#machinereinforcement-learning) _3 projects_
- [Co-Simulation Environment](#co-simulation-environment) _2 projects_
- [Gas](#gas) _2 projects_
- [Visualization](#visualization) _2 projects_
- [Messaging](#messaging) _1 projects_
- [Power System Data](#power-system-data) _4 projects_
- [Power Electronics](#power-electronics) _5 projects_

## Explanation
- 🥇🥈🥉&nbsp; Combined project-quality score
- ⭐️&nbsp; Star count from GitHub
- 🐣&nbsp; New project _(less than 6 months old)_
- 💤&nbsp; Inactive project _(6 months no activity)_
- 💀&nbsp; Dead project _(12 months no activity)_
- 📈📉&nbsp; Project is trending up or down
- ➕&nbsp; Project was recently added
- ❗️&nbsp; Warning _(e.g. missing/risky license)_
- 👨‍💻&nbsp; Contributors count from GitHub
- 🔀&nbsp; Fork count from GitHub
- 📋&nbsp; Issue count from GitHub
- ⏱️&nbsp; Last update timestamp on package manager
- 📥&nbsp; Download count from package manager
- 📦&nbsp; Number of dependent projects
- <img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13">&nbsp; Power system analysis projects written in Python
- <img src="https://github.com/JuliaLang/julia-logo-graphics/blob/master/images/julia.ico" style="display:inline;" width="13" height="13">&nbsp; Power system analysis projects written in Python
- <img src="https://raw.githubusercontent.com/ml-tooling/best-of-ml-python/main/config/images/jupyter.ico" style="display:inline;" width="13" height="13">&nbsp; Jupyter related project
- <img src="https://github.com/CURENT/ltb2/blob/main/images/icon/LTB.ico" style="display:inline;" width="13" height="13">&nbsp; CURENT Large-scale Testbed projects
- <img src="https://github.com/CURENT/ltb2/blob/main/images/icon/CURENT_Logo_Transparent.ico" style="display:inline;" width="13" height="13">&nbsp; CURENT, Center for Ultra-Wide-Area Resilient Electric Energy Transmission Networks

<br>

## Dynamic

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_Power System Dynamic Simulation._

<details><summary><b><a href="https://github.com/cuihantao/andes">LTB andes</a></b> (🥇19 ·  ⭐ 140) - Transient Stability Simulator; Part of CURENT LTB. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://raw.githubusercontent.com/ml-tooling/best-of-ml-python/main/config/images/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/CURENT/ltb2/blob/main/images/icon/LTB.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/CURENT/ltb2/blob/main/images/icon/CURENT_Logo_Transparent.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cuihantao/andes) (👨‍💻 16 · 🔀 61 · 📦 7 · 📋 44 - 9% open · ⏱️ 01.12.2022):

	```
	git clone https://github.com/cuihantao/andes
	```
- [PyPi](https://pypi.org/project/andes) (📥 260 / month):
	```
	pip install andes
	```
- [Conda](https://anaconda.org/anaconda/andes):
	```
	conda install -c anaconda andes
	```
- [Docker Hub](https://hub.docker.com/r/cuihantao/andes) (📥 110 · ⏱️ 10.12.2020):
	```
	docker pull cuihantao/andes
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/analysis/siip.html">PowerSimulationsDynamics.jl</a></b> (🥈17 ·  ⭐ 100) - Dynamic Power System simulations; Part of the SIIP at.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/JuliaLang/julia-logo-graphics/blob/master/images/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL-SIIP/PowerSimulationsDynamics.jl) (👨‍💻 10 · 🔀 25 · 📋 110 - 32% open · ⏱️ 29.11.2022):

	```
	git clone https://github.com/NREL-SIIP/PowerSimulationsDynamics.jl
	```
</details>
<details><summary><b><a href="https://github.com/OpenIPSL/OpenIPSL">OpenIPSL</a></b> (🥈17 ·  ⭐ 54 · ➕) - A library of power system models written with Modelica. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code></summary>

- [GitHub](https://github.com/OpenIPSL/OpenIPSL) (👨‍💻 27 · 🔀 41 · 📥 480 · 📋 110 - 14% open · ⏱️ 15.11.2022):

	```
	git clone https://github.com/OpenIPSL/OpenIPSL
	```
</details>
<details><summary><b><a href="https://github.com/modelica-3rdparty/PowerSystems">PowerSystems</a></b> (🥉14 ·  ⭐ 47) - Modelica 3rd party library for electrical power systems. <code><a href="https://modelica.org/licenses/ModelicaLicense2/">❗️Custom</a></code></summary>

- [GitHub](https://github.com/modelica-3rdparty/PowerSystems) (👨‍💻 10 · 🔀 33 · 📋 34 - 26% open · ⏱️ 19.06.2022):

	```
	git clone https://github.com/modelica-3rdparty/PowerSystems
	```
</details>
<details><summary><b><a href="https://github.com/changgang/steps">STEPS</a></b> (🥉8 ·  ⭐ 26 · 💤) - Balanced large-scale AC-DC hybrid power system analysis. <code><a href="http://bit.ly/34MBwT8">MIT</a></code></summary>

- [GitHub](https://github.com/changgang/steps) (👨‍💻 3 · 🔀 11 · 📥 8 · 📦 5 · ⏱️ 13.04.2022):

	```
	git clone https://github.com/changgang/steps
	```
</details>
<details><summary>Show 1 hidden projects...</summary>

- <b><a href="https://github.com/OpenHybridSim/OpenHybridSim-code">OpenHybridSim</a></b> (🥉6 ·  ⭐ 7 · 💀) - Power system EMT-TS hybrid simulation. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code>
</details>
<br>

## Steady State

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_Power System Steady State Simulation_

<details><summary><b><a href="https://www.pandapower.org/">pandapower</a></b> (🥇31 ·  ⭐ 570) - Convenient Power System Modelling and Analysis. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/e2nIEE/pandapower) (👨‍💻 98 · 🔀 380 · 📦 180 · 📋 780 - 19% open · ⏱️ 14.12.2022):

	```
	git clone https://github.com/e2nIEE/pandapower
	```
- [PyPi](https://pypi.org/project/pandapower) (📥 11K / month):
	```
	pip install pandapower
	```
- [Conda](https://anaconda.org/anaconda/pandapower):
	```
	conda install -c anaconda pandapower
	```
- [Docker Hub](https://hub.docker.com/r/pauldepraz/pandapowerapi) (📥 86 · ⏱️ 09.02.2021):
	```
	docker pull pauldepraz/pandapowerapi
	```
</details>
<details><summary><b><a href="https://pypsa.org">PyPSA</a></b> (🥇30 ·  ⭐ 750) - Simulating and optimising power and energy systems. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/PyPSA) (👨‍💻 54 · 🔀 320 · 📦 78 · 📋 220 - 25% open · ⏱️ 14.12.2022):

	```
	git clone https://github.com/PyPSA/PyPSA
	```
- [PyPi](https://pypi.org/project/pypsa) (📥 2.8K / month):
	```
	pip install pypsa
	```
- [Conda](https://anaconda.org/anaconda/pypsa):
	```
	conda install -c anaconda pypsa
	```
</details>
<details><summary><b><a href="https://www.advancedgridinsights.com/gridcal">GridCal</a></b> (🥈20 ·  ⭐ 310) - Cross-platform power systems software. <code><a href="http://bit.ly/37RvQcA">❗️LGPL-3.0</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/SanPen/GridCal) (👨‍💻 27 · 🔀 72 · 📥 23 · 📦 2 · ⏱️ 12.12.2022):

	```
	git clone https://github.com/SanPen/GridCal
	```
- [PyPi](https://pypi.org/project/GridCal) (📥 410 / month):
	```
	pip install GridCal
	```
</details>
<details><summary><b><a href="https://matpower.org/">matpower</a></b> (🥈20 ·  ⭐ 280) - Steady state power flow simulation. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code></summary>

- [GitHub](https://github.com/MATPOWER/matpower) (👨‍💻 12 · 🔀 130 · 📥 150K · 📋 120 - 8% open · ⏱️ 13.12.2022):

	```
	git clone https://github.com/MATPOWER/matpower
	```
- [PyPi](https://pypi.org/project/matpower) (📥 72 / month):
	```
	pip install matpower
	```
- [Docker Hub](https://hub.docker.com/r/matpower/matpower) (📥 360 · ⏱️ 23.11.2022):
	```
	docker pull matpower/matpower
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/analysis/siip.html">PowerSimulations.jl</a></b> (🥈20 ·  ⭐ 190) - Optimization of Power Systems; Part of the SIIP at.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/JuliaLang/julia-logo-graphics/blob/master/images/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL-SIIP/PowerSimulations.jl) (👨‍💻 28 · 🔀 43 · 📋 230 - 9% open · ⏱️ 02.12.2022):

	```
	git clone https://github.com/nrel-siip/powersimulations.jl
	```
</details>
<details><summary><b><a href="rwl.github.io/PYPOWER/api/">PYPOWER</a></b> (🥉19 ·  ⭐ 250) - Port of MATPOWER to Python. <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/rwl/PYPOWER) (👨‍💻 18 · 🔀 90 · 📦 70 · 📋 35 - 68% open · ⏱️ 24.06.2022):

	```
	git clone https://github.com/rwl/PYPOWER
	```
- [PyPi](https://pypi.org/project/PYPOWER) (📥 1.9K / month):
	```
	pip install PYPOWER
	```
- [Conda](https://anaconda.org/anaconda/pypower):
	```
	conda install -c anaconda pypower
	```
- [Docker Hub](https://hub.docker.com/r/hwanghust/pypower) (📥 16 · ⏱️ 19.05.2019):
	```
	docker pull hwanghust/pypower
	```
</details>
<details><summary><b><a href="https://pypsa.org">PyPSA-Eur</a></b> (🥉19 ·  ⭐ 170) - Optimisation Model of the European Transmission System. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/pypsa-eur) (👨‍💻 34 · 🔀 100 · 📋 170 - 30% open · ⏱️ 08.12.2022):

	```
	git clone https://github.com/PyPSA/pypsa-eur
	```
- [Docker Hub](https://hub.docker.com/r/nimfetrisa/pypsa-eur) (📥 35 · ⏱️ 11.04.2022):
	```
	docker pull nimfetrisa/pypsa-eur
	```
</details>
<details><summary><b><a href="https://github.com/alliander-opensource/power-grid-model">Power Grid Model</a></b> (🥉19 ·  ⭐ 58) - Steady-state distribution power system analysis. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/alliander-opensource/power-grid-model) (👨‍💻 12 · 🔀 10 · 📥 740 · 📋 53 - 47% open · ⏱️ 14.12.2022):

	```
	git clone https://github.com/alliander-opensource/power-grid-model
	```
- [PyPi](https://pypi.org/project/power-grid-model) (📥 4K / month):
	```
	pip install power-grid-model
	```
</details>
<details><summary><b><a href="https://github.com/lanl-ansi/PowerModels.jl">PowerModels.jl</a></b> (🥉18 ·  ⭐ 300) - Power Network Optimization. <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://github.com/JuliaLang/julia-logo-graphics/blob/master/images/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/lanl-ansi/PowerModels.jl) (👨‍💻 25 · 🔀 110 · 📋 440 - 21% open · ⏱️ 01.12.2022):

	```
	git clone https://github.com/lanl-ansi/PowerModels.jl
	```
</details>
<details><summary><b><a href="https://github.com/grid-parity-exchange/Egret">EGRET</a></b> (🥉16 ·  ⭐ 96 · 📈) - Tools for Power Systems Optimization Modeling. <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/grid-parity-exchange/Egret) (👨‍💻 38 · 🔀 42 · 📦 2 · 📋 79 - 53% open · ⏱️ 13.12.2022):

	```
	git clone https://github.com/grid-parity-exchange/Egret
	```
</details>
<details><summary><b><a href="https://pypsa.org">PyPSA-Eur-Sec</a></b> (🥉16 ·  ⭐ 66) - Sector-Coupled Optimisation Model of the European Energy System. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/pypsa-eur-sec) (👨‍💻 20 · 🔀 41 · 📋 120 - 51% open · ⏱️ 28.11.2022):

	```
	git clone https://github.com/PyPSA/pypsa-eur-sec
	```
</details>
<details><summary><b><a href="https://www.gridpath.io/">GridPath</a></b> (🥉16 ·  ⭐ 64) - Power system planning and operations. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/blue-marble/gridpath) (👨‍💻 7 · 🔀 25 · 📥 380 · 📋 300 - 20% open · ⏱️ 21.06.2022):

	```
	git clone https://github.com/blue-marble/gridpath
	```
</details>
<details><summary><b><a href="https://l2rpn.chalearn.org/">LightSim2Grid</a></b> (🥉15 ·  ⭐ 31 · ➕) - A fast backend for the Grid2Op. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/BDonnot/lightsim2grid) (🔀 9 · 📥 38 · 📦 17 · 📋 29 - 41% open · ⏱️ 20.06.2022):

	```
	git clone https://github.com/BDonnot/lightsim2grid/
	```
- [PyPi](https://pypi.org/project/LightSim2Grid) (📥 1.1K / month):
	```
	pip install LightSim2Grid
	```
- [Docker Hub](https://hub.docker.com/r/bdonnot/lightsim2grid) (📥 170 · ⏱️ 01.02.2022):
	```
	docker pull bdonnot/lightsim2grid
	```
</details>
<br>

## Power System Co-Simulation

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_Power System Co-Simulation Platform with Integrated Engines_

<details><summary><b><a href="https://github.com/CURENT/ltb2">Large-scale Testbed (LTB)</a></b> (🥇6 ·  ⭐ 3) - CURENT Large-scale Testbed, with Self-Developed Engine. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/CURENT/ltb2/blob/main/images/icon/LTB.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/CURENT/ltb2/blob/main/images/icon/CURENT_Logo_Transparent.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CURENT/ltb2) (👨‍💻 3 · 🔀 1 · ⏱️ 30.11.2022):

	```
	git clone https://github.com/CURENT/ltb2
	```
</details>
<br>

## Co-Simulation Framework

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_Co-Simulation Framework to Integrate Multiple Simulators_

<details><summary><b><a href="https://helics.org/tools/">HELICS</a></b> (🥇22 ·  ⭐ 85) - Framework to Integrate Simulators. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/JuliaLang/julia-logo-graphics/blob/master/images/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/GMLC-TDC/HELICS) (👨‍💻 37 · 🔀 33 · 📥 16K · 📋 600 - 12% open · ⏱️ 02.12.2022):

	```
	git clone https://github.com/GMLC-TDC/HELICS
	```
- [PyPi](https://pypi.org/project/helics) (📥 870 / month):
	```
	pip install helics
	```
- [Conda](https://anaconda.org/anaconda/helics):
	```
	conda install -c anaconda helics
	```
</details>
<br>

## Interface

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_Interface to other tools_

<details><summary><b><a href="https://github.com/mzy2240/ESA">Easy SimAuto</a></b> (🥇19 ·  ⭐ 33) - Python interface to PowerWorld. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/mzy2240/ESA) (👨‍💻 10 · 🔀 6 · 📦 3 · 📋 84 - 9% open · ⏱️ 10.12.2022):

	```
	git clone https://github.com/mzy2240/ESA
	```
- [PyPi](https://pypi.org/project/esa) (📥 380 / month):
	```
	pip install esa
	```
</details>
<details><summary><b><a href="https://github.com/PauloRadatz/py_dss_interface">py-dss-interface</a></b> (🥈17 ·  ⭐ 15 · 📉) - A package for access to direct dll version of OpenDSS. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PauloRadatz/py_dss_interface) (👨‍💻 5 · 🔀 6 · 📦 13 · 📋 53 - 60% open · ⏱️ 23.11.2022):

	```
	git clone https://github.com/PauloRadatz/py_dss_interface
	```
- [PyPi](https://pypi.org/project/py-dss-interface) (📥 140 / month):
	```
	pip install py-dss-interface
	```
</details>
<details><summary><b><a href="https://www.epri.com/pages/sa/opendss">OpenDSSDirect.py</a></b> (🥉16 ·  ⭐ 66 · ➕) - A direct library interface to OpenDSS. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/dss-extensions/OpenDSSDirect.py) (👨‍💻 3 · 🔀 19 · 📋 88 - 17% open · ⏱️ 13.12.2022):

	```
	git clone https://github.com/dss-extensions/OpenDSSDirect.py
	```
- [PyPi](https://pypi.org/project/OpenDSSDirect.py) (📥 2.3K / month):
	```
	pip install OpenDSSDirect.py
	```
- [Conda](https://anaconda.org/anaconda/opendssdirect.py):
	```
	conda install -c anaconda opendssdirect.py
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/grid/pydss.html">PyDSS</a></b> (🥉14 ·  ⭐ 24 · ➕) - A Python wrapper for OpenDSS. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL/PyDSS) (👨‍💻 22 · 🔀 15 · 📦 2 · 📋 23 - 60% open · ⏱️ 18.10.2022):

	```
	git clone https://github.com/NREL/PyDSS
	```
- [PyPi](https://pypi.org/project/pydss) (📥 18 / month):
	```
	pip install pydss
	```
</details>
<br>

## Optimization Solver

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://highs.dev/">HiGHS</a></b> (🥇24 ·  ⭐ 440) - Large-scale Sparse Linear Problem Optimizer. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ERGO-Code/HiGHS) (👨‍💻 45 · 🔀 86 · 📦 5 · 📋 350 - 15% open · ⏱️ 12.12.2022):

	```
	git clone https://github.com/ERGO-Code/HiGHS
	```
- [PyPi](https://pypi.org/project/scikit-highs) (📥 64 / month):
	```
	pip install scikit-highs
	```
</details>
<details><summary><b><a href="https://github.com/coin-or/Ipopt">Ipopt</a></b> (🥉23 ·  ⭐ 940) - COIN-OR Interior Point Optimizer. <code><a href="http://bit.ly/2M0xmjV">EPL-2.0</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/coin-or/Ipopt) (👨‍💻 22 · 🔀 200 · 📥 5.9K · 📋 510 - 0% open · ⏱️ 22.11.2022):

	```
	git clone https://github.com/coin-or/Ipopt
	```
- [PyPi](https://pypi.org/project/ipopt) (📥 3.1K / month):
	```
	pip install ipopt
	```
- [Conda](https://anaconda.org/anaconda/ipopt):
	```
	conda install -c anaconda ipopt
	```
</details>
<br>

## Optimization Modeling Language

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://www.pyomo.org">Pyomo</a></b> (🥇36 ·  ⭐ 1.4K · ➕) - Python-based Optimization Modeling Language. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://raw.githubusercontent.com/ml-tooling/best-of-ml-python/main/config/images/jupyter.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Pyomo/pyomo) (👨‍💻 120 · 🔀 400 · 📥 490 · 📦 1.1K · 📋 1.1K - 25% open · ⏱️ 13.12.2022):

	```
	git clone https://github.com/Pyomo/pyomo
	```
- [PyPi](https://pypi.org/project/Pyomo) (📥 130K / month):
	```
	pip install Pyomo
	```
- [Conda](https://anaconda.org/anaconda/pyomo):
	```
	conda install -c anaconda pyomo
	```
</details>
<details><summary><b><a href="https://jump.dev">JuMP</a></b> (🥉25 ·  ⭐ 1.8K · ➕) - Julia-based Optimization Modeling Language. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://github.com/JuliaLang/julia-logo-graphics/blob/master/images/julia.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://raw.githubusercontent.com/ml-tooling/best-of-ml-python/main/config/images/jupyter.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/jump-dev/JuMP.jl) (👨‍💻 130 · 🔀 360 · 📋 1.3K - 1% open · ⏱️ 13.12.2022):

	```
	git clone https://github.com/jump-dev/JuMP.jl
	```
</details>
<br>

## Machine/Reinforcement Learning

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_AI Power Grid Agent_

<details><summary><b><a href="https://l2rpn.chalearn.org/">Grid2Op</a></b> (🥇22 ·  ⭐ 200 · 📈) - Modeling sequential decision making in power systems. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://raw.githubusercontent.com/ml-tooling/best-of-ml-python/main/config/images/jupyter.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/rte-france/Grid2Op) (👨‍💻 21 · 🔀 82 · 📋 230 - 13% open · ⏱️ 12.12.2022):

	```
	git clone https://github.com/rte-france/Grid2Op
	```
- [PyPi](https://pypi.org/project/Grid2Op) (📥 440 / month):
	```
	pip install Grid2Op
	```
- [Docker Hub](https://hub.docker.com/r/bdonnot/grid2op) (📥 8.3K · ⭐ 1 · ⏱️ 05.07.2022):
	```
	docker pull bdonnot/grid2op
	```
</details>
<details><summary><b><a href="https://github.com/RLGC-Project/RLGC">RLGC</a></b> (🥉9 ·  ⭐ 82 · 💤) - RL for Grid Control (RLGC). <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://raw.githubusercontent.com/ml-tooling/best-of-ml-python/main/config/images/jupyter.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/RLGC-Project/RLGC) (👨‍💻 4 · 🔀 27 · 📋 14 - 28% open · ⏱️ 08.04.2022):

	```
	git clone https://github.com/RLGC-Project/RLGC
	```
</details>
<details><summary><b><a href="https://github.com/cuihantao/andes_gym">andes_gym</a></b> (🥉6 ·  ⭐ 7 · 💤) - ANDES RL Environment for OpenAI Gym. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/CURENT/ltb2/blob/main/images/icon/CURENT_Logo_Transparent.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cuihantao/andes_gym) (👨‍💻 2 · 🔀 3 · ⏱️ 28.01.2022):

	```
	git clone https://github.com/cuihantao/andes_gym
	```
- [PyPi](https://pypi.org/project/andes) (📥 260 / month):
	```
	pip install andes
	```
- [Conda](https://anaconda.org/anaconda/andes):
	```
	conda install -c anaconda andes
	```
</details>
<br>

## Co-Simulation Environment

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_Co-Simulation Environment for Modeling and Simulation_

<details><summary><b><a href="https://openmodelica.org">OpenModelica</a></b> (🥇28 ·  ⭐ 560) - Modelica-based environment for modeling and simulation. <code><a href="https://modelica.org/licenses/ModelicaLicense2/">❗️Custom</a></code></summary>

- [GitHub](https://github.com/OpenModelica/OpenModelica) (👨‍💻 180 · 🔀 230 · 📥 340 · 📋 6.7K - 22% open · ⏱️ 14.12.2022):

	```
	git clone https://github.com/OpenModelica/OpenModelica
	```
- [Docker Hub](https://hub.docker.com/r/openmodelica/openmodelica) (📥 17K · ⭐ 5 · ⏱️ 01.08.2022):
	```
	docker pull openmodelica/openmodelica
	```
</details>
<details><summary><b><a href="https://precice.org/">precice</a></b> (🥉23 ·  ⭐ 490) - Precise Code Interaction Coupling Environment. <code><a href="http://bit.ly/37RvQcA">❗️LGPL-3.0</a></code></summary>

- [GitHub](https://github.com/precice/precice) (👨‍💻 46 · 🔀 130 · 📥 13K · 📋 630 - 24% open · ⏱️ 12.12.2022):

	```
	git clone https://github.com/precice/precice
	```
- [PyPi](https://pypi.org/project/pyprecice) (📥 170 / month):
	```
	pip install pyprecice
	```
- [Conda](https://anaconda.org/anaconda/pyprecice):
	```
	conda install -c anaconda pyprecice
	```
- [Docker Hub](https://hub.docker.com/r/precice/precice) (📥 8.2K · ⏱️ 10.08.2022):
	```
	docker pull precice/precice
	```
</details>
<br>

## Gas

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_Gas Network Simulation_

<details><summary><b><a href="https://www.pandapipes.org/">pandapipes</a></b> (🥇21 ·  ⭐ 67) - Pipeflow Calculation Tool. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/e2nIEE/pandapipes) (👨‍💻 15 · 🔀 33 · 📦 6 · 📋 91 - 53% open · ⏱️ 13.12.2022):

	```
	git clone https://github.com/e2nIEE/pandapipes
	```
- [PyPi](https://pypi.org/project/pandapipes) (📥 1.3K / month):
	```
	pip install pandapipes
	```
</details>
<details><summary><b><a href="https://github.com/lanl-ansi/GasModels.jl">GasModels.jl</a></b> (🥉13 ·  ⭐ 55 · ➕) - Gas Network Optimization. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/JuliaLang/julia-logo-graphics/blob/master/images/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/lanl-ansi/GasModels.jl) (👨‍💻 11 · 🔀 13 · 📋 140 - 31% open · ⏱️ 22.11.2022):

	```
	git clone https://github.com/lanl-ansi/GasModels.jl
	```
</details>
<br>

## Visualization

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_Visualization for Power Grid_

<details><summary><b><a href="https://www.nrel.gov/analysis/siip.html">PowerGraphics</a></b> (🥇12 ·  ⭐ 19) - Visualization for PowerSimulations; Part of the SIIP at NREL. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/JuliaLang/julia-logo-graphics/blob/master/images/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL-SIIP/PowerGraphics.jl) (👨‍💻 9 · 🔀 8 · 📋 30 - 33% open · ⏱️ 17.11.2022):

	```
	git clone https://github.com/nrel-siip/powergraphics.jl
	```
</details>
<details><summary><b><a href="https://github.com/CURENT/agvis">LTB AGVis</a></b> (🥉6 ·  ⭐ 1) - Geographical Visualization for Power Grid; Part of CURENT.. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/CURENT/ltb2/blob/main/images/icon/LTB.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/CURENT/ltb2/blob/main/images/icon/CURENT_Logo_Transparent.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CURENT/agvis) (👨‍💻 7 · 🔀 4 · ⏱️ 30.11.2022):

	```
	git clone https://github.com/CURENT/agvis
	```
</details>
<br>

## Messaging

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_Messaging Environment for Distributed Computation_

<details><summary><b><a href="https://github.com/CURENT/dime">LTB DiME</a></b> (🥇6 ·  ⭐ 1) - Distributed Messaging Environment; Part of CURENT LTB. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/CURENT/ltb2/blob/main/images/icon/LTB.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/CURENT/ltb2/blob/main/images/icon/CURENT_Logo_Transparent.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CURENT/dime) (👨‍💻 3 · 🔀 1 · ⏱️ 23.11.2022):

	```
	git clone https://github.com/CURENT/dime
	```
</details>
<br>

## Power System Data

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_Power System Data Resources and Tools_

🔗&nbsp;<b><a href="https://ourworldindata.org/energy">Data on Energy</a></b> ( ⭐ 140)  - Data on energy by Our World in Data. <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code>

🔗&nbsp;<b><a href="https://github.com/tamu-engineering-research/COVID-EMDA">COVID-EMDA</a></b> ( ⭐ 53 · 💤)  - Cross-Domain Data Hub with Data in USA. <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code>

<details><summary><b><a href="https://pypsa.org">Atlite</a></b> (🥇22 ·  ⭐ 160 · 📉) - Calculating Renewable Power Potentials. <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/atlite) (👨‍💻 22 · 🔀 48 · 📦 15 · 📋 96 - 26% open · ⏱️ 09.12.2022):

	```
	git clone https://github.com/PyPSA/atlite
	```
- [PyPi](https://pypi.org/project/atlite) (📥 970 / month):
	```
	pip install atlite
	```
- [Conda](https://anaconda.org/anaconda/atlite):
	```
	conda install -c anaconda atlite
	```
</details>
<details><summary><b><a href="https://pypsa.org">powerplantmatching</a></b> (🥉19 ·  ⭐ 94) - Tools to combine multiple power plant databases. <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/powerplantmatching) (👨‍💻 15 · 🔀 35 · 📥 36 · 📦 12 · 📋 54 - 22% open · ⏱️ 01.12.2022):

	```
	git clone https://github.com/PyPSA/powerplantmatching
	```
- [PyPi](https://pypi.org/project/powerplantmatching) (📥 73 / month):
	```
	pip install powerplantmatching
	```
- [Conda](https://anaconda.org/anaconda/powerplantmatching):
	```
	conda install -c anaconda powerplantmatching
	```
</details>
<br>

## Power Electronics

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_Power System Data Resources and Tools_

<details><summary><b><a href="https://github.com/devbisme/skidl">skidl</a></b> (🥇18 ·  ⭐ 810 · 💤) - Module to Design Electronic Circuits. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/devbisme/skidl) (👨‍💻 21 · 🔀 96 · 📦 19 · 📋 98 - 30% open · ⏱️ 05.05.2022):

	```
	git clone https://github.com/devbisme/skidl
	```
- [PyPi](https://pypi.org/project/skidl) (📥 110 / month):
	```
	pip install skidl
	```
- [Conda](https://anaconda.org/anaconda/skidl):
	```
	conda install -c anaconda skidl
	```
</details>
<details><summary><b><a href="https://xyce.sandia.gov">Xyce</a></b> (🥇18 ·  ⭐ 240 · ➕) - Analog Circuit Simulator. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code></summary>

- [GitHub](https://github.com/Xyce/Xyce) (👨‍💻 23 · 🔀 42 · 📥 480 · 📋 52 - 17% open · ⏱️ 08.11.2022):

	```
	git clone https://github.com/Xyce/Xyce
	```
</details>
<details><summary><b><a href="https://github.com/gseim/gseim">GSEIM</a></b> (🥉4 ·  ⭐ 2 · ➕) - Interface Python to Ngspice and Xyce. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/gseim/gseim) (👨‍💻 3 · 🔀 1 · 📋 5 - 20% open · ⏱️ 21.09.2022):

	```
	git clone https://github.com/gseim/gseim
	```
</details>
<details><summary>Show 2 hidden projects...</summary>

- <b><a href="https://github.com/PySpice-org/PySpice">PySpice</a></b> (🥉15 ·  ⭐ 450 · 💀) - Interface Python to Ngspice and Xyce. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code>
- <b><a href="http://ngspice.sourceforge.net">NGSPICE</a></b> (🥉9 ·  ⭐ 45 · 💀) - Electric and Electronic Circuits Simulator. <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code>
</details>
---


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

- [**Papers With Code**](https://paperswithcode.com): Discover ML papers, code, and evaluation tables.

## Contribution

Contributions are encouraged and always welcome! If you like to add or update projects, choose one of the following ways:

- Open an issue by selecting one of the provided categories from the [issue page](https://github.com/jinningwang/best-of-ps/issues/new/choose) and fill in the requested information.
- Modify the [projects.yaml](https://github.com/jinningwang/best-of-ps/blob/main/projects.yaml) with your additions or changes, and submit a pull request. This can also be done directly via the [Github UI](https://github.com/jinningwang/best-of-ps/edit/main/projects.yaml).

If you like to contribute to or share suggestions regarding the project metadata collection or markdown generation, please refer to the [best-of-generator](https://github.com/best-of-lists/best-of-generator) repository. If you like to create your own best-of list, we recommend to follow [this guide](https://github.com/best-of-lists/best-of/blob/main/create-best-of-list.md).

For more information on how to add or update projects, please read the [contribution guidelines](https://github.com/jinningwang/best-of-ps/blob/main/CONTRIBUTING.md). By participating in this project, you agree to abide by its [Code of Conduct](https://github.com/jinningwang/best-of-ps/blob/main/.github/CODE_OF_CONDUCT.md).

## License
