<!-- markdownlint-disable -->
<h1 align="center">
    Popular Open Source Libraries for Power System Analysis
    <br>
</h1>

<p align="center">
    <strong>🏆&nbsp; A ranked list of popular projects for Power System Analysis. Updated weekly.</strong>
</p>

<p align="center">
    <a href="https://best-of.org" title="Best-of Badge"><img src="http://bit.ly/3o3EHNN"></a>
    <a href="#Contents" title="Project Count"><img src="https://img.shields.io/badge/projects-36-blue.svg?color=5ac4bf"></a>
    <a href="#Contribution" title="Contributions are welcome"><img src="https://img.shields.io/badge/contributions-welcome-green.svg"></a>
    <a href="https://github.com/jinningwang/best-of-ps/releases" title="Best-of Updates"><img src="https://img.shields.io/github/release-date/jinningwang/best-of-ps?color=green&label=updated"></a>
</p>

This curated list contains 36 popular open-source projects with a total of 6.6K stars grouped into 10 categories. All projects are ranked by a project-popular score, which is calculated based on various metrics automatically collected from GitHub and different package managers. If you like to add or update projects, feel free to open an [issue](https://github.com/jinningwang/best-of-ps/issues/new/choose), submit a [pull request](https://github.com/jinningwang/best-of-ps/pulls), or directly edit the [projects.yaml](https://github.com/jinningwang/best-of-ps/edit/main/projects.yaml). Contributions are very welcome!

## Contents

- [Dynamic](#dynamic) _6 projects_
- [Steady State](#steady-state) _14 projects_
- [Optimizer](#optimizer) _2 projects_
- [Machine/Reinforcement Learning](#machinereinforcement-learning) _2 projects_
- [Power System Co-Simulation](#power-system-co-simulation) _1 projects_
- [Co-Simulation Framework](#co-simulation-framework) _3 projects_
- [Gas](#gas) _1 projects_
- [Visualization](#visualization) _2 projects_
- [Messaging](#messaging) _1 projects_
- [Power System Data](#power-system-data) _4 projects_

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
- <img src="https://github.com/CURENT/ltb2/blob/main/images/icon/CURENT_Logo_Transparent.ico" style="display:inline;" width="13" height="13">&nbsp; CURENT, Center for Ultra-Wide-Area Resilient Electric Energy Transmission Networks

<br>

## Dynamic

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_Power System Dynamic Simulation._

<details><summary><b><a href="https://github.com/cuihantao/andes">LTB andes</a></b> (🥇19 ·  ⭐ 140) - Transient Stability Simulator with Hybrid Symbolic-.. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://raw.githubusercontent.com/ml-tooling/best-of-ml-python/main/config/images/jupyter.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/CURENT/ltb2/blob/main/images/icon/LTB.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/CURENT/ltb2/blob/main/images/icon/CURENT_Logo_Transparent.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cuihantao/andes) (👨‍💻 16 · 🔀 60 · 📦 6 · 📋 44 - 9% open · ⏱️ 01.12.2022):

	```
	git clone https://github.com/cuihantao/andes
	```
- [PyPi](https://pypi.org/project/andes) (📥 280 / month):
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

- [GitHub](https://github.com/NREL-SIIP/PowerSimulationsDynamics.jl) (👨‍💻 10 · 🔀 24 · 📋 110 - 32% open · ⏱️ 29.11.2022):

	```
	git clone https://github.com/NREL-SIIP/PowerSimulationsDynamics.jl
	```
</details>
<details><summary><b><a href="https://github.com/modelica-3rdparty/PowerSystems">PowerSystems</a></b> (🥈14 ·  ⭐ 47) - Modelica 3rd party library for electrical power systems. <code><a href="https://modelica.org/licenses/ModelicaLicense2/">❗️Custom</a></code></summary>

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
<details><summary><b><a href="https://www.dsatools.com">TSAT</a></b> (🥉2) - Electromechanical Time-domain Simulation; Part of DSA Tools. <code><a href="https://www.dsatools.com/dsatools-software-license-agreement/">❗️Custom</a></code></summary>

- _No project information available._</details>
<details><summary>Show 1 hidden projects...</summary>

- <b><a href="https://github.com/OpenHybridSim/OpenHybridSim-code">OpenHybridSim</a></b> (🥉6 ·  ⭐ 7 · 💀) - Power system Electromagnetic Transient-Transient Stability.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code>
</details>
<br>

## Steady State

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_Power System Steady State Simulation_

<details><summary><b><a href="https://www.pandapower.org/">pandapower</a></b> (🥇31 ·  ⭐ 570) - Convenient Power System Modelling and Analysis. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/e2nIEE/pandapower) (👨‍💻 95 · 🔀 370 · 📦 180 · 📋 770 - 18% open · ⏱️ 03.12.2022):

	```
	git clone https://github.com/e2nIEE/pandapower
	```
- [PyPi](https://pypi.org/project/pandapower) (📥 10K / month):
	```
	pip install pandapower
	```
- [Conda](https://anaconda.org/anaconda/pandapower):
	```
	conda install -c anaconda pandapower
	```
- [Docker Hub](https://hub.docker.com/r/pauldepraz/pandapowerapi) (📥 85 · ⏱️ 09.02.2021):
	```
	docker pull pauldepraz/pandapowerapi
	```
</details>
<details><summary><b><a href="https://pypsa.org">PyPSA</a></b> (🥇30 ·  ⭐ 750) - Simulating and optimising modern power and energy systems. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/PyPSA) (👨‍💻 53 · 🔀 310 · 📦 76 · 📋 220 - 24% open · ⏱️ 02.12.2022):

	```
	git clone https://github.com/PyPSA/PyPSA
	```
- [PyPi](https://pypi.org/project/pypsa) (📥 3K / month):
	```
	pip install pypsa
	```
- [Conda](https://anaconda.org/anaconda/pypsa):
	```
	conda install -c anaconda pypsa
	```
</details>
<details><summary><b><a href="https://www.advancedgridinsights.com/gridcal">GridCal</a></b> (🥈20 ·  ⭐ 300) - Cross-platform power systems software. <code><a href="http://bit.ly/37RvQcA">❗️LGPL-3.0</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/SanPen/GridCal) (👨‍💻 27 · 🔀 71 · 📥 23 · 📦 2 · ⏱️ 13.10.2022):

	```
	git clone https://github.com/SanPen/GridCal
	```
- [PyPi](https://pypi.org/project/GridCal) (📥 700 / month):
	```
	pip install GridCal
	```
</details>
<details><summary><b><a href="https://matpower.org/">matpower</a></b> (🥈20 ·  ⭐ 280) - Steady state power flow simulation. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code></summary>

- [GitHub](https://github.com/MATPOWER/matpower) (👨‍💻 12 · 🔀 120 · 📥 140K · 📋 120 - 8% open · ⏱️ 23.11.2022):

	```
	git clone https://github.com/MATPOWER/matpower
	```
- [PyPi](https://pypi.org/project/matpower) (📥 97 / month):
	```
	pip install matpower
	```
- [Docker Hub](https://hub.docker.com/r/matpower/matpower) (📥 350 · ⏱️ 23.11.2022):
	```
	docker pull matpower/matpower
	```
</details>
<details><summary><b><a href="https://www.nrel.gov/analysis/siip.html">PowerSimulations.jl</a></b> (🥈20 ·  ⭐ 180) - Optimization Simulation and Modeling of Power.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/JuliaLang/julia-logo-graphics/blob/master/images/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL-SIIP/PowerSimulations.jl) (👨‍💻 28 · 🔀 42 · 📋 220 - 7% open · ⏱️ 02.12.2022):

	```
	git clone https://github.com/nrel-siip/powersimulations.jl
	```
</details>
<details><summary><b><a href="rwl.github.io/PYPOWER/api/">PYPOWER</a></b> (🥈19 ·  ⭐ 250) - Port of MATPOWER to Python. <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/rwl/PYPOWER) (👨‍💻 18 · 🔀 89 · 📦 70 · 📋 35 - 68% open · ⏱️ 24.06.2022):

	```
	git clone https://github.com/rwl/PYPOWER
	```
- [PyPi](https://pypi.org/project/PYPOWER) (📥 2.1K / month):
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
<details><summary><b><a href="https://pypsa.org">PyPSA-Eur</a></b> (🥈19 ·  ⭐ 160 · ➕) - Open Optimisation Model of the European Transmission System. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/pypsa-eur) (👨‍💻 34 · 🔀 100 · 📋 170 - 29% open · ⏱️ 29.11.2022):

	```
	git clone https://github.com/PyPSA/pypsa-eur
	```
- [Docker Hub](https://hub.docker.com/r/nimfetrisa/pypsa-eur) (📥 35 · ⏱️ 11.04.2022):
	```
	docker pull nimfetrisa/pypsa-eur
	```
</details>
<details><summary><b><a href="https://github.com/lanl-ansi/PowerModels.jl">PowerModels.jl</a></b> (🥉18 ·  ⭐ 300) - Power Network Optimization. <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://github.com/JuliaLang/julia-logo-graphics/blob/master/images/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/lanl-ansi/PowerModels.jl) (👨‍💻 25 · 🔀 110 · 📋 440 - 21% open · ⏱️ 01.12.2022):

	```
	git clone https://github.com/lanl-ansi/PowerModels.jl
	```
</details>
<details><summary><b><a href="https://github.com/PauloRadatz/py_dss_interface">py-dss-interface</a></b> (🥉18 ·  ⭐ 15 · ➕) - Providing access to OpenDSS direct dll version of.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PauloRadatz/py_dss_interface) (👨‍💻 5 · 🔀 6 · 📦 13 · 📋 53 - 60% open · ⏱️ 23.11.2022):

	```
	git clone https://github.com/PauloRadatz/py_dss_interface
	```
- [PyPi](https://pypi.org/project/py-dss-interface) (📥 190 / month):
	```
	pip install py-dss-interface
	```
</details>
<details><summary><b><a href="https://pypsa.org">PyPSA-Eur-Sec</a></b> (🥉16 ·  ⭐ 65 · ➕) - Sector-Coupled Open Optimisation Model of the European.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

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
<details><summary><b><a href="https://github.com/grid-parity-exchange/Egret">EGRET</a></b> (🥉15 ·  ⭐ 96) - Tools for Power Systems Optimization Modeling. <code><a href="https://tldrlegal.com/search?q=BSD">❗️BSD</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/grid-parity-exchange/Egret) (👨‍💻 38 · 🔀 42 · 📦 2 · 📋 79 - 53% open · ⏱️ 02.11.2022):

	```
	git clone https://github.com/grid-parity-exchange/Egret
	```
</details>
<details><summary><b><a href="https://www.dsatools.com">VSAT</a></b> (🥉2) - Voltage Security Assessment using powerflow-based steady-state methods; Part of DSA.. <code><a href="https://www.dsatools.com/dsatools-software-license-agreement/">❗️Custom</a></code></summary>

- _No project information available._</details>
<details><summary><b><a href="https://www.dsatools.com">PSAT</a></b> (🥉2) - Powerflow Analysis; Part of DSA Tools. <code><a href="https://www.dsatools.com/dsatools-software-license-agreement/">❗️Custom</a></code></summary>

- _No project information available._</details>
<br>

## Optimizer

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://highs.dev/">HiGHS</a></b> (🥇24 ·  ⭐ 430 · 📈) - High performance serial and parallel solver for large scale sparse.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ERGO-Code/HiGHS) (👨‍💻 45 · 🔀 86 · 📦 5 · 📋 340 - 14% open · ⏱️ 01.12.2022):

	```
	git clone https://github.com/ERGO-Code/HiGHS
	```
- [PyPi](https://pypi.org/project/scikit-highs) (📥 22 / month):
	```
	pip install scikit-highs
	```
</details>
<details><summary><b><a href="https://github.com/coin-or/Ipopt">Ipopt</a></b> (🥉23 ·  ⭐ 930) - COIN-OR Interior Point Optimizer. <code><a href="http://bit.ly/2M0xmjV">EPL-2.0</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/coin-or/Ipopt) (👨‍💻 22 · 🔀 200 · 📥 5.8K · 📋 510 - 0% open · ⏱️ 22.11.2022):

	```
	git clone https://github.com/coin-or/Ipopt
	```
- [PyPi](https://pypi.org/project/ipopt) (📥 3K / month):
	```
	pip install ipopt
	```
- [Conda](https://anaconda.org/anaconda/ipopt):
	```
	conda install -c anaconda ipopt
	```
</details>
<br>

## Machine/Reinforcement Learning

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_AI Power Grid Agent_

<details><summary><b><a href="https://l2rpn.chalearn.org/">Grid2Op</a></b> (🥇20 ·  ⭐ 200) - A testbed platform to model sequential decision making in.. <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://raw.githubusercontent.com/ml-tooling/best-of-ml-python/main/config/images/jupyter.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/rte-france/Grid2Op) (👨‍💻 21 · 🔀 82 · 📋 230 - 19% open · ⏱️ 05.07.2022):

	```
	git clone https://github.com/rte-france/Grid2Op
	```
- [PyPi](https://pypi.org/project/Grid2Op) (📥 440 / month):
	```
	pip install Grid2Op
	```
- [Docker Hub](https://hub.docker.com/r/bdonnot/grid2op) (📥 8.2K · ⭐ 1 · ⏱️ 05.07.2022):
	```
	docker pull bdonnot/grid2op
	```
</details>
<details><summary><b><a href="https://github.com/cuihantao/andes_gym">andes_gym</a></b> (🥉6 ·  ⭐ 7 · 💤) - ANDES RL Environment for OpenAI Gym. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/CURENT/ltb2/blob/main/images/icon/CURENT_Logo_Transparent.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/cuihantao/andes_gym) (👨‍💻 2 · 🔀 3 · ⏱️ 28.01.2022):

	```
	git clone https://github.com/cuihantao/andes_gym
	```
- [PyPi](https://pypi.org/project/andes) (📥 280 / month):
	```
	pip install andes
	```
- [Conda](https://anaconda.org/anaconda/andes):
	```
	conda install -c anaconda andes
	```
</details>
<br>

## Power System Co-Simulation

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_Power System Co-Simulation Platform with Integrated Engines_

<details><summary><b><a href="https://github.com/CURENT/ltb2">Large-scale Testbed (LTB)</a></b> (🥇5 ·  ⭐ 2) - Large-scale Testbed, with SELF-DEVELOPED Engine. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/CURENT/ltb2/blob/main/images/icon/LTB.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/CURENT/ltb2/blob/main/images/icon/CURENT_Logo_Transparent.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CURENT/ltb2) (👨‍💻 3 · 🔀 1 · ⏱️ 30.11.2022):

	```
	git clone https://github.com/CURENT/ltb2
	```
</details>
<br>

## Co-Simulation Framework

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_Co-Simulation Framework to Integrate Multiple Simulators_

<details><summary><b><a href="https://openmodelica.org">OpenModelica</a></b> (🥇28 ·  ⭐ 550) - Modelica-based modeling and simulation environment. <code><a href="https://modelica.org/licenses/ModelicaLicense2/">❗️Custom</a></code></summary>

- [GitHub](https://github.com/OpenModelica/OpenModelica) (👨‍💻 170 · 🔀 230 · 📥 340 · 📋 6.6K - 22% open · ⏱️ 04.12.2022):

	```
	git clone https://github.com/OpenModelica/OpenModelica
	```
- [Docker Hub](https://hub.docker.com/r/openmodelica/openmodelica) (📥 17K · ⭐ 5 · ⏱️ 01.08.2022):
	```
	docker pull openmodelica/openmodelica
	```
</details>
<details><summary><b><a href="https://precice.org/">precice</a></b> (🥉23 ·  ⭐ 480) - Partitioned multi-physics simulations. <code><a href="http://bit.ly/37RvQcA">❗️LGPL-3.0</a></code></summary>

- [GitHub](https://github.com/precice/precice) (👨‍💻 46 · 🔀 130 · 📥 13K · 📋 620 - 24% open · ⏱️ 01.12.2022):

	```
	git clone https://github.com/precice/precice
	```
- [PyPi](https://pypi.org/project/pyprecice) (📥 220 / month):
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
<details><summary><b><a href="https://helics.org/tools/">HELICS</a></b> (🥉23 ·  ⭐ 84 · 📈) - Framework to Integrate Simulators Designed for Separate TDC.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/JuliaLang/julia-logo-graphics/blob/master/images/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/GMLC-TDC/HELICS) (👨‍💻 37 · 🔀 33 · 📥 16K · 📋 600 - 12% open · ⏱️ 02.12.2022):

	```
	git clone https://github.com/GMLC-TDC/HELICS
	```
- [PyPi](https://pypi.org/project/helics) (📥 880 / month):
	```
	pip install helics
	```
- [Conda](https://anaconda.org/anaconda/helics):
	```
	conda install -c anaconda helics
	```
</details>
<br>

## Gas

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_Gas Network Simulation_

<details><summary><b><a href="https://www.pandapipes.org/">pandapipes</a></b> (🥇21 ·  ⭐ 65) - A pipeflow calculation tool. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/e2nIEE/pandapipes) (👨‍💻 13 · 🔀 33 · 📦 6 · 📋 90 - 53% open · ⏱️ 01.12.2022):

	```
	git clone https://github.com/e2nIEE/pandapipes
	```
- [PyPi](https://pypi.org/project/pandapipes) (📥 1.5K / month):
	```
	pip install pandapipes
	```
</details>
<br>

## Visualization

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_Visualization for Power Grid_

<details><summary><b><a href="https://www.nrel.gov/analysis/siip.html">PowerGraphics</a></b> (🥇12 ·  ⭐ 19) - Visualization Program for PowerSimulations; Part of the SIIP.. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code><img src="https://github.com/JuliaLang/julia-logo-graphics/blob/master/images/julia.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/NREL-SIIP/PowerGraphics.jl) (👨‍💻 9 · 🔀 8 · 📋 30 - 33% open · ⏱️ 17.11.2022):

	```
	git clone https://github.com/nrel-siip/powergraphics.jl
	```
</details>
<details><summary><b><a href="https://github.com/CURENT/agvis">LTB AGVis</a></b> (🥉6 ·  ⭐ 1) - Geographical Visualization of Power Grid; Part of CURENT.. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/CURENT/ltb2/blob/main/images/icon/LTB.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/CURENT/ltb2/blob/main/images/icon/CURENT_Logo_Transparent.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/CURENT/agvis) (👨‍💻 7 · 🔀 4 · ⏱️ 30.11.2022):

	```
	git clone https://github.com/CURENT/agvis
	```
</details>
<br>

## Messaging

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_Messaging Environment for Distributed Computation_

<details><summary><b><a href="https://github.com/CURENT/dime">LTB DiME</a></b> (🥇6 ·  ⭐ 1) - Distributed Messaging Environment for LTB; Part of CURENT LTB. <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> <code><img src="https://github.com/CURENT/ltb2/blob/main/images/icon/LTB.ico" style="display:inline;" width="13" height="13"></code> <code><img src="https://github.com/CURENT/ltb2/blob/main/images/icon/CURENT_Logo_Transparent.ico" style="display:inline;" width="13" height="13"></code></summary>

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

🔗&nbsp;<b><a href="https://github.com/tamu-engineering-research/COVID-EMDA">COVID-EMDA</a></b> ( ⭐ 53 · 💤)  - Cross-Domain Data Hub with Electricity Market, Coronavirus Case, Mobility.. <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code>

<details><summary><b><a href="https://pypsa.org">Atlite</a></b> (🥇23 ·  ⭐ 160 · ➕) - Calculating Renewable Power Potentials and Time Series. <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/atlite) (👨‍💻 22 · 🔀 48 · 📦 15 · 📋 95 - 26% open · ⏱️ 29.11.2022):

	```
	git clone https://github.com/PyPSA/atlite
	```
- [PyPi](https://pypi.org/project/atlite) (📥 1.3K / month):
	```
	pip install atlite
	```
- [Conda](https://anaconda.org/anaconda/atlite):
	```
	conda install -c anaconda atlite
	```
</details>
<details><summary><b><a href="https://pypsa.org">powerplantmatching</a></b> (🥉19 ·  ⭐ 93 · ➕) - https://powerplantmatching.readthedocs.io/en/latest/. <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> <code><img src="https://www.python.org/static/favicon.ico" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/PyPSA/powerplantmatching) (👨‍💻 15 · 🔀 35 · 📥 36 · 📦 12 · 📋 54 - 22% open · ⏱️ 01.12.2022):

	```
	git clone https://github.com/PyPSA/powerplantmatching
	```
- [PyPi](https://pypi.org/project/powerplantmatching) (📥 82 / month):
	```
	pip install powerplantmatching
	```
- [Conda](https://anaconda.org/anaconda/powerplantmatching):
	```
	conda install -c anaconda powerplantmatching
	```
</details>

---
## Limitations

- **Project Data Collection**: The data collection is incomplete for the projects that are not majorly hosted in GitHub.
- [**Project Popularity Score**](https://github.com/best-of-lists/best-of-generator#project-quality-score): The source template calls it as ***Quality***, however, I rename it as ***Popularity***. 
  > This calculation is just chosen by ***EXPERIENCE***. There is ***NO*** scientific proof that this really reflects the ***QUALITY*** of a project. 


## Related Resources

- [**Papers With Code**](https://paperswithcode.com): Discover ML papers, code, and evaluation tables.

## Contribution

Contributions are encouraged and always welcome! If you like to add or update projects, choose one of the following ways:

- Open an issue by selecting one of the provided categories from the [issue page](https://github.com/jinningwang/best-of-ps/issues/new/choose) and fill in the requested information.
- Modify the [projects.yaml](https://github.com/jinningwang/best-of-ps/blob/main/projects.yaml) with your additions or changes, and submit a pull request. This can also be done directly via the [Github UI](https://github.com/jinningwang/best-of-ps/edit/main/projects.yaml).

If you like to contribute to or share suggestions regarding the project metadata collection or markdown generation, please refer to the [best-of-generator](https://github.com/best-of-lists/best-of-generator) repository. If you like to create your own best-of list, we recommend to follow [this guide](https://github.com/best-of-lists/best-of/blob/main/create-best-of-list.md).

For more information on how to add or update projects, please read the [contribution guidelines](https://github.com/jinningwang/best-of-ps/blob/main/CONTRIBUTING.md). By participating in this project, you agree to abide by its [Code of Conduct](https://github.com/jinningwang/best-of-ps/blob/main/.github/CODE_OF_CONDUCT.md).

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
