# Complete Catalog Inspection Report

- `status`: complete
- `started_at`: 2026-07-25
- `branch`: `architect-inspect`
- `policy_source`: `philosophy.md`
- `process_source`: `inspection-process.md`
- `catalog_source`: `projects.yaml`
- `catalog_entries`: 170
- `completed_entries`: 170
- `remaining_entries`: 0

## Reporting Rule

An entry is added below only after its category, primary developer-facing
implementation language, stewardship, GitHub Actions presence, and explicit
paper-citation evidence have been inspected.

Every completed entry records current metadata, recommended metadata, sources,
and a decision status. The high-level summary will be written only after all 170
entries are complete.

## Entry Inspections

### 1. ParaEMT

- `repository`: `NatLabRockies/ParaEMT_public`
- `reviewed_commit`: `d79d735a4a587d56c5b88187d1a499195b6b2b84`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (`paper_id` only)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `emt` | `emt` | Keep. The project identifies itself as an EMT simulator and implements an EMT network nodal formulation using the trapezoidal rule. |
| Labels | `python`, `lab` | `python`, `lab` | Keep. Python is the maintained first-party simulation implementation; the MATLAB files are plotting utilities rather than a second core implementation. The project is developed and stewarded by a U.S. national laboratory. |
| GitHub Actions | absent | absent | Keep. No workflow file exists under `.github/workflows`. |
| `paper_id` | absent | `10.1109/TPWRD.2023.3342715`, `10.1016/j.epsr.2024.110734` | Add both papers explicitly requested by the README's “Citing” section. |

Evidence:

- The [project README](https://github.com/NatLabRockies/ParaEMT_public/blob/d79d735a4a587d56c5b88187d1a499195b6b2b84/README.md) describes EMT modeling, the trapezoidal-rule nodal formulation, Numba-compiled Python, both requested citations, and development under NREL projects.
- The maintained simulation source is predominantly Python; the four `.m` files are result-plotting scripts and do not meet the core-language rule.
- No repository citation file or explicit paper-bearing `codemeta.json` or `.zenodo.json` was found; the README is the authoritative citation source for this entry.

Suggested catalog change:

```yaml
paper_id:
  - 10.1109/TPWRD.2023.3342715
  - 10.1016/j.epsr.2024.110734
```

### 2. DPsim

- `repository`: `sogno-platform/dpsim`
- `reviewed_commit`: `b63e7153f2cc94ad8844e1110efeb7e2ac9c13e9`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category, labels, and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `emt` | `electromechanical` | Change. DPsim is a hybrid EMT/dynamic-phasor simulator, but its project identity, principal software paper, and distinctive formulation are dynamic phasor/shifted-frequency simulation. The included EMT and power-flow domains are important secondary capabilities. |
| Labels | `gha`, `pypi`, `jupyter`, `python`, `c`, `university` | `cpp`, `gha`, `university` | Change. The simulation kernel and component models are C++, not C. Python is the binding and scripting layer, so it does not qualify under the core implementation-language rule. `pypi` and `jupyter` are retired labels. |
| GitHub Actions | present | `gha` | Keep. Multiple YAML workflow files exist under `.github/workflows`. |
| `paper_id` | absent | nine-identifier list below | Add. The official documentation explicitly asks users to cite one of its listed papers; nine listed journal/conference papers have DOI identifiers. |

Evidence:

- The [README](https://github.com/sogno-platform/dpsim/blob/b63e7153f2cc94ad8844e1110efeb7e2ac9c13e9/README.md) states that DPsim supports both EMT and dynamic phasor simulation, exposes a Python module, and implements its simulation core in C++.
- The [official documentation](https://github.com/sogno-platform/dpsim/blob/b63e7153f2cc94ad8844e1110efeb7e2ac9c13e9/docs/hugo/content/en/docs/_index.md) says RWTH Aachen's Institute for Automation of Complex Power Systems coordinates development and explicitly requests citation of one of the listed publications.
- The source tree contains hundreds of maintained `.cpp` and `.h` files for the kernel and models. Python provides bindings, packaging, utilities, and user scripts; the repository's `.c` files are not the core implementation.
- The repository has no dedicated citation file, `codemeta.json`, or paper-bearing `.zenodo.json`. Its official in-repository documentation is the explicit citation source.
- The two non-paper project reports in the same publication list have no DOI or arXiv identifier and are not proposed as `paper_id` values. The separately listed dissertation is also omitted because `paper_id` is defined for papers.

Suggested catalog change:

```yaml
category: electromechanical
labels: ["cpp", "gha", "university"]
paper_id:
  - 10.1016/j.softx.2019.100253
  - 10.1109/OSMSES58477.2023.10089718
  - 10.1049/tje2.12208
  - 10.1109/OSMSES54027.2022.9769135
  - 10.3390/en14237989
  - 10.3390/en14071860
  - 10.3390/en13153879
  - 10.1109/ICCEP.2017.8004805
  - 10.1109/EI2.2017.8245739
```

### 3. OpenDSS

- `repository`: EPRI OpenDSS SourceForge repository (no `github_id`)
- `reviewed_revision`: current public repository and OpenDSS 11.0.0.1 distribution
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | `steady-state` | Keep. OpenDSS supports harmonics and dynamics, but distribution power flow and quasi-static time-series analysis are its principal catalog-level role. |
| Labels | `python`, `julia`, `c`, `octave`, `non-profit` | `cpp`, `non-profit` | Change. EPRI documents OpenDSS-X as its C++ translation and core library. Python, Julia, and Octave are external interfaces or automation clients rather than first-party core languages, and EPRI explicitly describes the DSS-Extensions interfaces as unofficial. The current `c` label is not accurate for the C++ core. |
| GitHub Actions | not applicable | absent | Keep absent. The entry has no GitHub repository; SourceForge-hosted automation is outside the narrow `gha` definition. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README section explicitly asks users to cite a paper. Documentation reference lists are technical references, not project citation instructions. |

Evidence:

- EPRI's [OpenDSS repository documentation](https://opendss.epri.com/OpenDSSRepository.html) describes the maintained OpenDSS-X repository as a Delphi-to-C++ translation intended to serve as a core library.
- The [official downloads page](https://opendss.epri.com/Downloads.html) and current [SourceForge distribution](https://sourceforge.net/projects/electricdss/files/) show that the original Delphi/Free Pascal implementation also remains part of the project and its releases.
- EPRI's [Free Pascal build documentation](https://opendss.epri.com/OpenDSSFPCBuild.html) calls the C API, Python, Julia, and other DSS-Extensions interfaces unofficial. They therefore do not satisfy the core-language rule for this entry.
- The public repository/distribution has no explicit project citation instruction. General manuals contain feature-specific reference lists, but do not ask users to cite a core OpenDSS paper.

Architecture note:

- OpenDSS exposes a taxonomy gap: its original maintained implementation is Delphi/Free Pascal, while the approved language vocabulary has no `pascal` label. The recommendation uses `cpp` because EPRI presents OpenDSS-X as the current developer-facing core library. If the catalog later decides to represent both official implementations, add a `pascal` label rather than treating client-language wrappers as substitutes.

Suggested catalog change:

```yaml
labels: ["cpp", "non-profit"]
```

### 4. OpenDER

- `repository`: `epri-dev/OpenDER`
- `reviewed_commit`: `fe7877c664bc6c5eb3832499bf05e0f1dd1825c8`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category and labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `phasor` | `pe` | Change. OpenDER's primary artifact is an inverter-based DER behavior and control model covering grid-support, ride-through, trip, and enter-service behavior. That converter/device/control focus fits `pe` better than the renamed system-level electromechanical-transient category. |
| Labels | `pypi`, `jupyter`, `python`, `c`, `non-profit` | `python`, `non-profit` | Change. The maintained model, packaging, and tests are Python. No maintained first-party C core was found. `pypi` and `jupyter` are retired labels. |
| GitHub Actions | absent | absent | Keep. No workflow file exists under `.github/workflows`. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README citation section explicitly recommends a paper. The linked EPRI model specification is a product report, not an identified paper citation. |

Evidence:

- The [README](https://github.com/epri-dev/OpenDER/blob/fe7877c664bc6c5eb3832499bf05e0f1dd1825c8/README.rst) defines OpenDER as EPRI's model of steady-state and dynamic inverter-based DER behavior, links the model specification, and describes snapshot, QSTS, and dynamic uses.
- The first-party source, package metadata, and extensive test suite are Python. The repository contains no `.c`, `.h`, or `.cpp` implementation files.
- Package authors and contacts use EPRI addresses, and the linked model specification is an EPRI product, confirming `non-profit` stewardship.
- No `CITATION` variant, paper-bearing `codemeta.json` or `.zenodo.json`, or explicit “how to cite” instruction was found.

Suggested catalog change:

```yaml
category: pe
labels: ["python", "non-profit"]
```

### 5. GridPACK

- `repository`: `GridOPTICS/GridPACK`
- `reviewed_commit`: `bb411473c48d0e17aecfe52703546f72bb5bd00d`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category migration, language label, and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `phasor` | `electromechanical` | Rename with the category migration. GridPACK is a multi-application grid-simulation framework; among dynamic formulations, its mature capability is conventional dynamics simulation, while EMT remains under development. Its AC power flow, contingency, and state-estimation applications are substantial secondary capabilities. |
| Labels | `c`, `gha`, `python`, `lab` | `cpp`, `gha`, `lab` | Change. GridPACK explicitly identifies its implementation as C++ with Python wrappers. The wrapper does not qualify as another core implementation language, and `c` should be corrected to `cpp`. |
| GitHub Actions | present | `gha` | Keep. YAML workflows exist under `.github/workflows`. |
| `paper_id` | absent | `10.1177/1094342015607609` | Add. The README has a dedicated “Citing GridPACK” section with this DOI. |

Evidence:

- The [README](https://github.com/GridOPTICS/GridPACK/blob/bb411473c48d0e17aecfe52703546f72bb5bd00d/README.md) lists AC power flow, dynamics simulation, contingency analysis, and state estimation as its mature applications; EMT is listed as still under development.
- The same README states that GridPACK is written in C++ with Python wrappers, provides the explicit GridPACK paper citation, and gives a PNNL contact and national-laboratory funding history.
- The source tree contains hundreds of `.cpp` and `.hpp` files. Python files implement wrappers, documentation, configuration, and examples rather than an independent simulation core.

Suggested catalog change:

```yaml
category: electromechanical
labels: ["cpp", "gha", "lab"]
paper_id: 10.1177/1094342015607609
```

### 6. GridLAB-D

- `repository`: `gridlab-d/gridlab-d`
- `reviewed_commit`: `e1841e1eebced819e45209f4a899763ce337b177`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category and language label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `phasor` | `steady-state` | Change. GridLAB-D is an event/time-series distribution simulator whose electrical network is solved as a sequence of steady states separated by state transitions. Its core grid formulation is unbalanced distribution power flow, not electromechanical transient simulation. |
| Labels | `c`, `gha`, `lab` | `cpp`, `gha`, `lab` | Change. The maintained simulator core and modules are C++; the build requires a C++ compiler. MATLAB, Python, and Java material does not constitute another primary first-party core. |
| GitHub Actions | present | `gha` | Keep. A YAML workflow exists under `.github/workflows`. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or repository README citation section explicitly recommends a paper. A relevant PNNL publication exists, but the process forbids substituting a literature search for a project-authored citation instruction. |

Evidence:

- The [official technical overview](https://gridlab-d.readthedocs.io/en/latest/docs/1.0%20-%20Prospective%20Users/Technical_Overview/) defines GridLAB-D as a distribution-system and connected-end-use simulation platform.
- The [official overview](https://gridlab-d.readthedocs.io/en/docs/docs/2.0%20-%20New%20Users/Tutorial/2.2.1%20-%20Overview/) explicitly says the agent-based simulator computes a series of steady states separated by state transitions.
- The [power-flow guide](https://gridlab-d.readthedocs.io/en/docs/docs/3.0%20-%20Modeling%20Reference/Modules/Powerflow/00-Powerflow_Introduction/) describes its three-phase unbalanced steady-state solvers.
- The reviewed source contains hundreds of `.cpp` and `.h` files, and its README requires `g++` or Clang. The license and official documentation attribute development to DOE/PNNL, supporting `lab`.
- No repository citation file, paper-bearing project metadata, or explicit README citation instruction was found. The bundled MATPOWER README citation belongs to the vendored MATPOWER component and is not a GridLAB-D citation.

Suggested catalog change:

```yaml
category: steady-state
labels: ["cpp", "gha", "lab"]
```

### 7. PowerSimulationsDynamics.jl

- `repository`: `NREL-Sienna/PowerSimulationsDynamics.jl`
- `reviewed_commit`: `f77d3dfc77d82174ff85a4f4fdcf20dcec3c01d1`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category migration and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `phasor` | `electromechanical` | Rename with the category migration. The package performs full-system phasor-domain time simulation of differential-algebraic generator, inverter, controller, load, and network models. |
| Labels | `gha`, `julia`, `lab` | `julia`, `gha`, `lab` | Keep the same set in canonical order. Julia is the first-party implementation; National Laboratory of the Rockies develops the package; GitHub Actions workflows are present. |
| GitHub Actions | present | `gha` | Keep. Multiple YAML workflows exist under `.github/workflows`. |
| `julia_id` | `PowerSimulationsDynamics` | `PowerSimulationsDynamics` | Confirmed current. It matches `Project.toml` and the Julia package name. |
| `paper_id` | absent | `arXiv:2308.02921`, `10.1109/TPWRS.2023.3303291` | Add both identifiers presented in the README's “Citing PowerSimulationsDynamics.jl” section: the package paper and its background methods paper. |

Evidence:

- The [README](https://github.com/NREL-Sienna/PowerSimulationsDynamics.jl/blob/f77d3dfc77d82174ff85a4f4fdcf20dcec3c01d1/README.md) describes power-system dynamics simulation, provides both citations, and identifies development under the laboratory's SIIP/Sienna initiative.
- The [model documentation](https://github.com/NREL-Sienna/PowerSimulationsDynamics.jl/blob/f77d3dfc77d82174ff85a4f4fdcf20dcec3c01d1/docs/src/models.md) describes simultaneous time integration of differential and algebraic states and explicitly covers electromechanical generator dynamics.
- The first-party package source is Julia. Small Python and MATLAB file counts come from support or test material, not separate maintained simulation implementations.
- The README's Zenodo badge identifies software releases and is correctly excluded from `paper_id`.

Suggested catalog change:

```yaml
category: electromechanical
labels: ["julia", "gha", "lab"]
paper_id:
  - "arXiv:2308.02921"
  - 10.1109/TPWRS.2023.3303291
```

### 8. GenSAS

- `repository`: `ANL-CEEESA/gensas`
- `reviewed_commit`: `c9f5d8218681b28699ae78265094379e8cddf1e0`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category and language labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `phasor` | `steady-state` | Change. The current power-grid module provides AC power flow; the other current module is a generic single-model Modelica simulator. Publications describe broader future/method work but are not current implemented power-grid scope. |
| Labels | `cpp`, `gha`, `lab` | `cpp`, `modelica`, `gha`, `lab` | Add `modelica`, which is a primary supported model-authoring language for ModelicaSAS. Keep C++, workflows, and Argonne stewardship. |
| `paper_id` | absent | absent | Confirmed skip. The README lists publications but does not ask users to cite them. |

Evidence: the [README](https://github.com/ANL-CEEESA/gensas/blob/c9f5d8218681b28699ae78265094379e8cddf1e0/README.md) defines the two current modules, C++/Modelica roles, AC-power-flow scope, Argonne funding, and a publication list. Three GitHub Actions workflows are present.

Suggested change:

```yaml
category: steady-state
labels: ["cpp", "modelica", "gha", "lab"]
```

### 9. PowerSAS.m

- `repository`: `ANL-CEEESA/powersas.m`
- `reviewed_commit`: `40f06eae3fe2cc361f9e76016c9b25c07039c5f2`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category migration, labels, and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `phasor` | `electromechanical` | Rename. Its distinguishing capability is phasor-domain dynamic security and transient-stability simulation, alongside power flow and contingency analysis. |
| Labels | `octave`, `lab` | `octave`, `matlab`, `lab` | Add `matlab`: the maintained `.m` implementation explicitly supports both MATLAB and GNU Octave. No GitHub Actions workflow exists. |
| `paper_id` | absent | `10.1109/OAJPE.2023.3245040` | Add the DOI explicitly required by the README's “Citing” section. |

Evidence: the [README](https://github.com/ANL-CEEESA/powersas.m/blob/40f06eae3fe2cc361f9e76016c9b25c07039c5f2/README.md) documents MATLAB/Octave requirements, transient-stability and DAE capabilities, and the citation. Argonne contacts and LDRD support confirm `lab`.

Suggested change:

```yaml
category: electromechanical
labels: ["octave", "matlab", "lab"]
paper_id: 10.1109/OAJPE.2023.3245040
```

### 10. LTB ANDES

- `repository`: `CURENT/andes`
- `reviewed_commit`: `eda5163c9ee8d19945a1dd5d1771fec5da608c27`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category migration and labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `phasor` | `electromechanical` | Rename. ANDES is a phasor-domain power-system dynamics and transient-stability simulator with power flow for initialization and analysis. |
| Labels | `gha`, `pypi`, `conda`, `jupyter`, `python`, `julia`, `university` | `python`, `gha`, `university` | Python is the first-party implementation and model-definition language. Remove retired distribution/notebook labels and the non-core Julia interoperability label. |
| `paper_id` | `10.1109/TPWRS.2020.3017019` | same | Confirmed current against both `CITATION.bib` and the README. |

Evidence: the [README](https://github.com/CURENT/andes/blob/eda5163c9ee8d19945a1dd5d1771fec5da608c27/README.md) identifies Python implementation, time-domain simulation, equation-based Python models, the citation, and development at the University of Tennessee's CURENT center. A GitHub Actions workflow is present.

Suggested change:

```yaml
category: electromechanical
labels: ["python", "gha", "university"]
```

### 11. OpenIPSL

- `repository`: `OpenIPSL/OpenIPSL`
- `reviewed_commit`: `8155c73f51ceeec935eb158247c7c043eb697ff5`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category migration only)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `phasor` | `electromechanical` | Rename. OpenIPSL explicitly provides Modelica component models for phasor time-domain dynamic analysis. |
| Labels | `gha`, `modelica`, `university` | `modelica`, `gha`, `university` | Confirmed, reordered canonically. RPI's ALSETLab currently maintains it and workflows are present. |
| `paper_id` | `10.1016/j.softx.2022.101277` | same | Confirmed current against the `CITATION.cff` preferred citation. |

Evidence: the [README](https://github.com/OpenIPSL/OpenIPSL/blob/8155c73f51ceeec935eb158247c7c043eb697ff5/README.md) states the formulation, language, current RPI steward, and citation policy; [`CITATION.cff`](https://github.com/OpenIPSL/OpenIPSL/blob/8155c73f51ceeec935eb158247c7c043eb697ff5/CITATION.cff) supplies the DOI.

Suggested change:

```yaml
category: electromechanical
labels: ["modelica", "gha", "university"]
```

### 12. PowerSystems

- `repository`: `modelica-3rdparty/PowerSystems`
- `reviewed_commit`: `1ecfd2648d7cd54ed88926594455b713186529de`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category migration only)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `phasor` | `electromechanical` | Rename. This Modelica library supports transient and steady-state AC/DC system models; its dynamic component-modeling role is the best exclusive fit. |
| Labels | `modelica`, `non-profit` | same | Keep. The source is Modelica and the library is under Modelica Association copyright/stewardship. No GitHub Actions workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. The README links a related publication with DOI `10.3384/ECP14096515`, but does not instruct users to cite it. |

Evidence: the [README](https://github.com/modelica-3rdparty/PowerSystems/blob/1ecfd2648d7cd54ed88926594455b713186529de/README.md) defines its transient/steady-state scope, Modelica implementation, publication link, authorship, and Modelica Association copyright.

Suggested change:

```yaml
category: electromechanical
```

### 13. OpenHybridSim

- `repository`: `OpenHybridSim/OpenHybridSim-code`
- `reviewed_commit`: `277101eb16630ccab56022cee8ebb7e7d819d3e0`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `phasor` | `cosim` | Change. Its primary role is partitioning, coordinating, and exchanging boundary data between separate EMT and phasor-domain simulators. |
| Labels | `java`, `university` | same | Keep. The core classes are Java and the project identifies Arizona State University development. No workflow exists. |
| `paper_id` | absent | `10.1109/TPWRS.2015.2479588`, `10.1109/PESGM.2016.7741233` | Add both papers explicitly requested in the README. |

Evidence: the [README](https://github.com/OpenHybridSim/OpenHybridSim-code/blob/277101eb16630ccab56022cee8ebb7e7d819d3e0/README.md) defines the EMT/phasor hybrid coupling role, Java core, ASU developer, and two required citations.

Suggested change:

```yaml
category: cosim
labels: ["java", "university"]
paper_id:
  - 10.1109/TPWRS.2015.2479588
  - 10.1109/PESGM.2016.7741233
```

### 14. STEPS

- `repository`: `changgang/steps`
- `reviewed_commit`: `4f380e8de9ba2ecd8fb59ed3e072001484923c3b`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category, labels, and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `phasor` | `electromechanical` | Rename. Dynamic simulation is a principal capability; power flow and short-circuit analysis are supporting analyses. |
| Labels | `c`, `pypi`, `python`, `university` | `cpp`, `university` | The first-party kernel is C++. Its `.c` files are bundled SuiteSparse/deprecated dependencies and Python is the `stepspy` binding. Remove retired `pypi`. No workflow exists. |
| `paper_id` | absent | three-DOI list below | Add all three papers the README explicitly asks users to cite. |

Evidence: the [README](https://github.com/changgang/steps/blob/4f380e8de9ba2ecd8fb59ed3e072001484923c3b/README.md) identifies the Shandong University maintainer, simulator scope, C++ implementation details, and citation set.

```yaml
category: electromechanical
labels: ["cpp", "university"]
paper_id:
  - 10.1109/TPWRS.2020.3045102
  - 10.1016/j.ijepes.2023.109509
  - 10.1016/j.ijepes.2025.110651
```

### 15. PSAT

- `repository`: `Sinan81/PSAT`
- `reviewed_commit`: `b0519c6cf5e87c6cbc5360bcc973a3cfdddcd864`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category migration and language labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `phasor` | `electromechanical` | Rename. PSAT includes phasor-domain time-domain and small-signal stability analysis as well as power flow, continuation power flow, and OPF. |
| Labels | `octave`, `university` | `octave`, `matlab`, `university` | The maintained `.m` toolbox explicitly contains MATLAB and GNU Octave execution paths. No workflow exists. |
| `paper_id` | absent | absent | Confirmed skip for this repository snapshot: it has no citation file or README citation instruction. |

Evidence: the source identifies Federico Milano and University College Dublin, maintains separate MATLAB/Octave paths, and contains the time-domain, small-signal, power-flow, CPF, and OPF implementations. The GitHub repository is a distribution mirror rather than an active upstream.

```yaml
category: electromechanical
labels: ["octave", "matlab", "university"]
```

### 16. PST

- `repository`: `cuihantao/pst`
- `reviewed_commit`: `7d252542d4615751d59c949915dd149e3da6522d`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category migration, language, and stewardship)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `phasor` | `electromechanical` | Rename. PST is a MATLAB power-system transient-stability and dynamic-equivalencing toolbox. |
| Labels | `octave`, `university` | `matlab`, `community` | The implementation is explicitly MATLAB; no repository evidence establishes GNU Octave compatibility. This personal archival mirror is better represented as community stewardship than as a currently university-governed project. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README citation instruction exists. |

Evidence: the `.m` source repeatedly identifies the MATLAB Power System Toolbox and its original authors/copyright, while the reviewed repository consists of a single archival import without governance or citation documentation.

```yaml
category: electromechanical
labels: ["matlab", "community"]
```

### 17. matmtdc

- `repository`: `HuaizhiWang/matmtdc`
- `reviewed_commit`: `4c84180373fe691dccd826aa5948c64e9e6f4922`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category migration and language)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `phasor` | `electromechanical` | Rename. MATMTDC performs dynamic analysis of hybrid AC/DC power systems using time-domain machine, control, and network models. |
| Labels | `octave`, `university` | `matlab`, `university` | The project describes itself as MATLAB-based. Octave references occur in bundled MATPOWER-derived functions and do not establish compatibility for the dynamic simulator. |
| `paper_id` | absent | absent | Confirmed skip. No explicit project paper citation was found. |

Evidence: the [README](https://github.com/HuaizhiWang/matmtdc/blob/4c84180373fe691dccd826aa5948c64e9e6f4922/README.md) states MATLAB implementation, dynamic AC/DC scope, and a Shenzhen University contact.

```yaml
category: electromechanical
labels: ["matlab", "university"]
```

### 18. Dynaωo

- `repository`: `dynawo/dynawo`
- `reviewed_commit`: `ce7edf72710f4e367a2ffdc84fb5d1afb710f141`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category migration and language)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `phasor` | `electromechanical` | Rename. Dynaωo is a time-domain power-system stability suite using differential-algebraic component and network models. |
| Labels | `gha`, `modelica`, `for-profit` | `cpp`, `modelica`, `gha`, `for-profit` | Add C++: the project explicitly calls itself a hybrid C++/Modelica suite and implements models in both. Python is build/support tooling. RTE remains the named corporate steward and workflows exist. |
| `paper_id` | absent | absent | Confirmed skip. The repository has literature bibliographies but no citation file or README instruction recommending a core paper. |

Evidence: the [README](https://github.com/dynawo/dynawo/blob/ce7edf72710f4e367a2ffdc84fb5d1afb710f141/README.md) defines the architecture and lists current RTE maintainers.

```yaml
category: electromechanical
labels: ["cpp", "modelica", "gha", "for-profit"]
```

### 19. Xyce

- `repository`: `Xyce/Xyce`
- `reviewed_commit`: `d72b5846a0397ddf852a49305cb6f395457685ca`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category and labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `phasor` | `emt` | Change. Xyce is a SPICE-compatible circuit simulator whose transient analysis solves detailed circuit time-domain behavior, matching the waveform/circuit role of `emt`. |
| Labels | `pypi`, `conda`, `jupyter`, `python`, `lab` | `cpp`, `lab` | The parallel simulator is written in C++; Python is an interface and the distribution/notebook labels are retired. Sandia stewardship remains. No GitHub Actions workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. The README explicitly cites Xyce as computer software using DOE CODE software DOIs, not a paper; those identifiers do not qualify as `paper_id`. |

Evidence: the [README](https://github.com/Xyce/Xyce/blob/d72b5846a0397ddf852a49305cb6f395457685ca/README.md) defines its circuit/transient role, C++ implementation, Sandia stewardship, and software-only citation metadata.

```yaml
category: emt
labels: ["cpp", "lab"]
```

### 20. ASSET

- `repository`: `NatLabRockies/ASSET`
- `reviewed_commit`: `db7adcd0986574b293507d6328e14cd041bfef62`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (`paper_id` only)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. ASSET automates operating-point/contingency grid-strength assessment around PSS/E network solutions. |
| Labels | `python`, `lab` | same | Keep. First-party code is Python and the project is an NLR/NREL software record. No workflow exists. |
| `paper_id` | absent | `10.1109/PESGM52009.2025.11225841` | Add the paper explicitly requested by the README; the DOI was confirmed on the laboratory publication record. |

Evidence: [README](https://github.com/NatLabRockies/ASSET/blob/db7adcd0986574b293507d6328e14cd041bfef62/README.md).

### 21. UnitCommitment.jl

- `repository`: `ANL-CEEESA/UnitCommitment.jl`
- `reviewed_commit`: `bac77d6d5d040552fc719c0c5a96fafa1dcbfb5a`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-current

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. SCUC is explicitly a mixed-integer optimization problem in the catalog's optimization-problem category. |
| Labels | `julia`, `gha`, `lab` | same | Keep. Julia core, Argonne lead, and workflows are confirmed. |
| `julia_id` | `UnitCommitment` | same | Confirmed against package metadata. |
| `paper_id` | absent | absent | Confirmed skip. The explicit citation is a Zenodo software record (`10.5281/zenodo.4269874`), not a paper. |

Evidence: [README](https://github.com/ANL-CEEESA/UnitCommitment.jl/blob/bac77d6d5d040552fc719c0c5a96fafa1dcbfb5a/README.md) and `.zenodo.json`.

### 22. EGRIP.jl

- `repository`: `ANL-CEEESA/EGRIP.jl`
- `reviewed_commit`: `13772f6450350d17e0790014e75f5f6186350d6c`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. Restoration planning is formulated primarily as hierarchical, multi-period optimization with power-flow feasibility constraints. |
| Labels | `julia`, `octave`, `gha`, `lab` | `julia`, `matlab`, `gha`, `lab` | The project explicitly calls itself Julia/MATLAB; no Octave support claim was found. Argonne and one workflow are confirmed. |
| `julia_id` | `EGRIP` | same | Confirmed. |
| `paper_id` | absent | absent | Confirmed skip. The README has a “References” item, not a citation instruction. |

Evidence: [README](https://github.com/ANL-CEEESA/EGRIP.jl/blob/13772f6450350d17e0790014e75f5f6186350d6c/README.md).

### 23. REopt

- `repository`: `NatLabRockies/REopt_API`
- `reviewed_commit`: `29854e2b0424f8169888bdba53e8e951d01ba17a`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. REopt is a mixed-integer technology-sizing and dispatch optimization model/API. |
| Labels | `gha`, `python`, `julia`, `lab` | `python`, `gha`, `lab` | This repository implements the Python API; the Julia optimization backend is the separate `REopt.jl` project and does not qualify as this entry's core language. Workflows and laboratory stewardship remain. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README paper instruction was found. |

Evidence: [README](https://github.com/NatLabRockies/REopt_API) describing the API/backend boundary.

### 24. DOPER

- `repository`: `LBNL-ETA/DOPER`
- `reviewed_commit`: `a96fb17d1664feb30afae49aa04ec7300ca27e51`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. DOPER formulates predictive DER scheduling/control as Pyomo optimization. |
| Labels | `gha`, `python`, `jupyter`, `lab` | `python`, `gha`, `lab` | Python core, LBNL stewardship, and workflows are confirmed; remove retired `jupyter`. |
| `paper_id` | absent | absent | Confirmed skip. The explicit citation is a California Energy Commission project report without DOI/arXiv paper identity. |

Evidence: [README](https://github.com/LBNL-ETA/DOPER/blob/a96fb17d1664feb30afae49aa04ec7300ca27e51/README.md).

### 25. AMES - Version 5.0

- `repository`: `ames-market/AMES-V5.0`
- `reviewed_commit`: `ff64fca38870facfa95896300dd8d6772d8155d6`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-current (canonical label ordering only)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. Its core is successive-day SCUC/SCED market optimization, with reinforcement-learning agents as an optional behavior layer. |
| Labels | `java`, `university`, `python` | `python`, `java`, `university` | Both Java and Python are explicitly identified first-party implementations; Iowa State leads development. No workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. The README provides a broad publications bibliography but no instruction selecting a core paper to cite. |

Evidence: [README](https://github.com/ames-market/AMES-V5.0/blob/ff64fca38870facfa95896300dd8d6772d8155d6/README.rst).

### 26. AMES (V4.0)

- `repository`: `ames-market/AMES-v4.0`
- `reviewed_commit`: `8e4e6b0069ff40d12e87a6a42dc001fbb528d407`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. Deterministic/stochastic day-ahead SCUC is the primary formulation. |
| Labels | `java`, `university` | `python`, `java`, `university` | Add Python: the first-party PSST solver is bundled and implements the SCUC optimization called by the Java market test bed. Iowa State stewardship remains; no workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. Publications are listed, but no project citation instruction selects a core paper. |

Evidence: [README](https://github.com/ames-market/AMES-v4.0/blob/8e4e6b0069ff40d12e87a6a42dc001fbb528d407/README.md).

### 27. LTB AMS

- `repository`: `CURENT/ams`
- `reviewed_commit`: `9288067b41cadb6f4309627cc92926fecff81b06`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. AMS formulates scheduling and market-clearing optimization models, with dynamics co-simulation as integration. |
| Labels | `gha`, `pypi`, `conda`, `jupyter`, `python`, `university` | `python`, `gha`, `university` | Python core, workflows, and University of Tennessee/CURENT stewardship are confirmed; remove retired labels. |
| `paper_id` | `10.1109/TSTE.2025.3528027` | same | Confirmed against `CITATION.bib` and the README. |

Evidence: [README](https://github.com/CURENT/ams/blob/9288067b41cadb6f4309627cc92926fecff81b06/README.md) and [`CITATION.bib`](https://github.com/CURENT/ams/blob/9288067b41cadb6f4309627cc92926fecff81b06/CITATION.bib).

### 28. PowSyBl Core

- `repository`: `powsybl/powsybl-core`
- `reviewed_commit`: `7a1ae581a9f8409c366261bdbc60cb64691dc43a`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-current

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. The core provides network models and analysis infrastructure used for load flow, security, and operational studies. |
| Labels | `gha`, `java`, `non-profit` | `java`, `gha`, `non-profit` | Confirmed. The repository is fully Java, has workflows, and is an LF Energy/Linux Foundation project. |
| `paper_id` | absent | absent | Confirmed skip. No core citation instruction exists; DOI-bearing test-data READMEs belong to datasets. |

Evidence: [README](https://github.com/powsybl/powsybl-core/blob/7a1ae581a9f8409c366261bdbc60cb64691dc43a/README.md).

### 29. PyPowSyBl

- `repository`: `powsybl/pypowsybl`
- `reviewed_commit`: `742818acd3a767f633324544f5d1181ebcb7be51`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. It exposes PowSyBl network and steady-state operational analyses to Python. |
| Labels | `gha`, `pypi`, `python`, `java`, `jupyter`, `non-profit` | `python`, `java`, `gha`, `non-profit` | Python and Java are both maintained first-party implementation layers in this repository. Remove retired package/notebook labels; retain workflows and LF Energy stewardship. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README paper instruction exists. |

Evidence: [README](https://github.com/powsybl/pypowsybl/blob/742818acd3a767f633324544f5d1181ebcb7be51/README.md).

### 30. Open RAO

- `repository`: `powsybl/powsybl-open-rao`
- `reviewed_commit`: `13430f2869f0d1580e6caa0d84335f655d60c8fb`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-current

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. OpenRAO optimizes remedial actions under network-security constraints. |
| Labels | `gha`, `java`, `non-profit` | `java`, `gha`, `non-profit` | Java core, workflows, and LF Energy stewardship are confirmed. |
| `paper_id` | absent | absent | Confirmed skip. No explicit paper citation instruction exists. |

Evidence: [README](https://github.com/powsybl/powsybl-open-rao/blob/13430f2869f0d1580e6caa0d84335f655d60c8fb/README.md).

### 31. PowerFlows.jl

- `repository`: `NREL-Sienna/PowerFlows.jl`
- `reviewed_commit`: `28173f513ddb9cb5d44afee861ad00d9306c3f19`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-current

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. Its explicit purpose is solving the power-flow problem through multiple methods. |
| Labels | `gha`, `julia`, `lab` | `julia`, `gha`, `lab` | Julia core, workflows, and NLR Sienna stewardship are confirmed. |
| `julia_id` | `PowerFlows` | same | Confirmed. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README citation instruction exists. |

Evidence: [README](https://github.com/NREL-Sienna/PowerFlows.jl/blob/28173f513ddb9cb5d44afee861ad00d9306c3f19/README.md).

### 32. PowerNetworkMatrices.jl

- `repository`: `NREL-Sienna/PowerNetworkMatrices.jl`
- `reviewed_commit`: `278d05ed358039049ba17d0fce14da5ca6e8b766`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-current

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. The package computes Y-bus, PTDF, LODF, MODF, and related matrices derived from steady-state network formulations. |
| Labels | `gha`, `julia`, `lab` | `julia`, `gha`, `lab` | Julia core, public workflows, and NLR Sienna stewardship are confirmed. |
| `julia_id` | `PowerNetworkMatrices` | same | Confirmed against `Project.toml`. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README instruction requests a core paper; linked technical references explain individual methods. |

Evidence: [README](https://github.com/NREL-Sienna/PowerNetworkMatrices.jl/blob/278d05ed358039049ba17d0fce14da5ca6e8b766/README.md) and [documentation overview](https://github.com/NREL-Sienna/PowerNetworkMatrices.jl/blob/278d05ed358039049ba17d0fce14da5ca6e8b766/docs/src/index.md).

### 33. PowerSimulations.jl

- `repository`: `NREL-Sienna/PowerSimulations.jl`
- `reviewed_commit`: `6de67af7a4ee050577b497a83cff2ca8b8e4e7ac`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-current

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. Its primary computation is sequential quasi-static operations optimization, including production-cost, UC, and ED simulations. |
| Labels | `gha`, `julia`, `lab` | `julia`, `gha`, `lab` | Julia core, workflows, and NLR Sienna stewardship are confirmed. |
| `julia_id` | `PowerSimulations` | same | Confirmed against `Project.toml`. |
| `paper_id` | absent | absent | Confirmed skip. The README badge points to a Zenodo software record and does not request a research-paper citation. |

Evidence: [README](https://github.com/NREL-Sienna/PowerSimulations.jl/blob/6de67af7a4ee050577b497a83cff2ca8b8e4e7ac/README.md) and [documentation overview](https://github.com/NREL-Sienna/PowerSimulations.jl/blob/6de67af7a4ee050577b497a83cff2ca8b8e4e7ac/docs/src/index.md).

### 34. PowerSystemsInvestments.jl

- `repository`: `NREL-Sienna/PowerSystemsInvestments.jl`
- `reviewed_commit`: `293a717519cbddc5ab1bca4876e10fbb6a641419`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-current

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. The package implements power-system investment models using JuMP, PowerModels, network matrices, and portfolio data. |
| Labels | `gha`, `julia`, `lab` | `julia`, `gha`, `lab` | Julia core, workflows, and NLR Sienna stewardship are confirmed. |
| `julia_id` | `PowerSystemsInvestments` | same | Confirmed against `Project.toml`. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or explicit README paper instruction exists. |

Evidence: [README](https://github.com/NREL-Sienna/PowerSystemsInvestments.jl/blob/293a717519cbddc5ab1bca4876e10fbb6a641419/README.md), package dependencies, and first-party source.

### 35. PowerSystemsInvestmentsPortfolios.jl

- `repository`: `NREL-Sienna/PowerSystemsInvestmentsPortfolios.jl`
- `reviewed_commit`: `1c8071f03f291b0ce3ae0a3bd05395a14f68fbe8`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | `dataman` | Change. Its documented primary role is defining data models and structures for technologies, regions, financial data, and investment requirements, rather than formulating or solving investment optimization itself. |
| Labels | `gha`, `julia`, `lab` | `julia`, `gha`, `lab` | Julia core, workflows, and NLR Sienna stewardship are confirmed. |
| `julia_id` | `PowerSystemsInvestmentsPortfolios` | same | Confirmed against `Project.toml`. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or explicit README paper instruction exists. |

Evidence: [documentation overview](https://github.com/NREL-Sienna/PowerSystemsInvestmentsPortfolios.jl/blob/1c8071f03f291b0ce3ae0a3bd05395a14f68fbe8/docs/src/index.md) and [README](https://github.com/NREL-Sienna/PowerSystemsInvestmentsPortfolios.jl/blob/1c8071f03f291b0ce3ae0a3bd05395a14f68fbe8/README.md).

```yaml
category: dataman
labels: ["julia", "gha", "lab"]
```

### 36. PyPSA

- `repository`: `PyPSA/PyPSA`
- `reviewed_commit`: `c2e6801e6f4fee78adfcc399b2ec688d0058eecf`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. PyPSA's central computations are steady-state power flow and optimization across dispatch, commitment, and capacity planning. |
| Labels | `gha`, `pypi`, `conda`, `python`, `jupyter`, `university` | `python`, `gha`, `university` | Python core, workflows, and maintenance led by TU Berlin are explicit; remove retired distribution/notebook labels. |
| `paper_id` | `10.5334/jors.188` | same | Confirmed. Both `CITATION.cff` and the README explicitly request this Journal of Open Research Software paper. |

Evidence: [README](https://github.com/PyPSA/PyPSA/blob/c2e6801e6f4fee78adfcc399b2ec688d0058eecf/README.md) and [`CITATION.cff`](https://github.com/PyPSA/PyPSA/blob/c2e6801e6f4fee78adfcc399b2ec688d0058eecf/CITATION.cff).

```yaml
category: steady-state
labels: ["python", "gha", "university"]
paper_id: 10.5334/jors.188
```

### 37. PyPSA-USA

- `repository`: `PyPSA/pypsa-usa`
- `reviewed_commit`: `f38d7565275884532bd0bcdc07c272244557a417`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. The workflow builds and runs US capacity-expansion, production-cost, and power-flow models. |
| Labels | `gha`, `python`, `jupyter`, `university` | `python`, `gha`, `university` | Python is the primary maintained implementation, a workflow exists, and current project contacts are university based; remove retired `jupyter`. |
| `paper_id` | absent | absent | Confirmed skip. The README explicitly directs users to `CITATION.cff`, but that file requests the Zenodo software DOI `10.5281/zenodo.10815964`, not a paper. The documentation's publications and method references are not substituted for it. |

Evidence: [README](https://github.com/PyPSA/pypsa-usa/blob/f38d7565275884532bd0bcdc07c272244557a417/README.md), [`CITATION.cff`](https://github.com/PyPSA/pypsa-usa/blob/f38d7565275884532bd0bcdc07c272244557a417/CITATION.cff), and [documentation overview](https://github.com/PyPSA/pypsa-usa/blob/f38d7565275884532bd0bcdc07c272244557a417/docs/source/index.md).

```yaml
category: steady-state
labels: ["python", "gha", "university"]
```

### 38. PyPSA-Eur

- `repository`: `PyPSA/pypsa-eur`
- `reviewed_commit`: `308c739705c00a46ee1e4c853150dfba1b4c134f`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (`paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. It builds a European sector-coupled model for operational and capacity-planning optimization. |
| Labels | `gha`, `python`, `university` | `python`, `gha`, `university` | Python core, workflows, and maintenance led by TU Berlin are confirmed. |
| `paper_id` | absent | three DOI values below | Add the three papers that the documentation explicitly asks users to choose among when citing PyPSA-Eur. Do not add the separate Zenodo software DOI. |

Evidence: [README](https://github.com/PyPSA/pypsa-eur/blob/308c739705c00a46ee1e4c853150dfba1b4c134f/README.md), [citation section](https://github.com/PyPSA/pypsa-eur/blob/308c739705c00a46ee1e4c853150dfba1b4c134f/doc/index.md), and [`CITATION.cff`](https://github.com/PyPSA/pypsa-eur/blob/308c739705c00a46ee1e4c853150dfba1b4c134f/CITATION.cff).

```yaml
paper_id:
  - 10.1016/j.esr.2018.08.012
  - 10.1016/j.joule.2023.06.016
  - 10.1016/j.joule.2022.04.016
```

### 39. PyPSA-Distribution

- `repository`: `pypsa-meets-earth/pypsa-distribution`
- `reviewed_commit`: `6be166008bfe7dd70e13458d9bffdfa226ffe053`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (stewardship migration)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. Its stated primary goal is optimization of small-scale, high-resolution multi-energy systems. |
| Labels | `gha`, `python`, `volunteer` | `python`, `gha`, `community` | Python core and workflows are confirmed; the PyPSA meets Earth initiative collectively maintains it, so migrate legacy `volunteer` to `community`. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or explicit README paper instruction exists. |

Evidence: [README](https://github.com/pypsa-meets-earth/pypsa-distribution/blob/6be166008bfe7dd70e13458d9bffdfa226ffe053/README.md) and [documentation](https://github.com/pypsa-meets-earth/pypsa-distribution/blob/6be166008bfe7dd70e13458d9bffdfa226ffe053/doc/index.rst).

### 40. PyPSA-Earth

- `repository`: `pypsa-meets-earth/pypsa-earth`
- `reviewed_commit`: `cd3d07b5aaa874fa203731e3a66094c3cb0ecc6c`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (stewardship migration)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. Its primary computation is global operational and capacity-expansion optimization, including sector coupling. |
| Labels | `gha`, `python`, `volunteer` | `python`, `gha`, `community` | Python core and workflows are confirmed; its own description calls PyPSA meets Earth an independent research initiative, supporting `community`. |
| `paper_id` | `10.1016/j.apenergy.2023.121096` | same | Confirmed. `CITATION.cff` explicitly requests this paper. A second sector-coupled paper is described as model documentation in the README but is not currently the requested software citation. |

Evidence: [README](https://github.com/pypsa-meets-earth/pypsa-earth/blob/cd3d07b5aaa874fa203731e3a66094c3cb0ecc6c/README.md) and [`CITATION.cff`](https://github.com/pypsa-meets-earth/pypsa-earth/blob/cd3d07b5aaa874fa203731e3a66094c3cb0ecc6c/CITATION.cff).

### 41. LightSim2Grid

- `repository`: `BDonnot/lightsim2grid`
- `reviewed_commit`: `5bfc7f81926444fab5824a47541bc7827af42eec`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language and retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. Its core solves AC/DC power-flow equations as a fast Grid2Op backend. |
| Labels | `gha`, `pypi`, `python`, `for-profit` | `cpp`, `gha`, `for-profit` | The maintained computational backend, grid model, and solvers are C++; Python is principally the binding/package interface. Workflows and RTE stewardship remain; remove the retired package label. |
| `paper_id` | absent | absent | Confirmed skip. The README requests a GitHub software citation without a paper identifier. |

Evidence: [README](https://github.com/BDonnot/lightsim2grid/blob/5bfc7f81926444fab5824a47541bc7827af42eec/README.md) and first-party C++ source.

```yaml
category: steady-state
labels: ["cpp", "gha", "for-profit"]
```

### 42. MOST

- `repository`: `MATPOWER/most`
- `reviewed_commit`: `ab17b56e1ae74baf2e1b7b5a7cd6ab4d5c27673f`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. MOST formulates and solves generalized steady-state scheduling, from ED through stochastic security-constrained UC and multiperiod OPF. |
| Labels | `gha`, `octave`, `university` | `octave`, `matlab`, `gha`, `university` | The first-party M-files explicitly support and are developed for both GNU Octave and MATLAB. Cornell-based stewardship and a workflow are confirmed. |
| `paper_id` | two DOI values | same | Confirmed. `CITATION` explicitly requires both the MATPOWER and MOST papers. |

Evidence: [README](https://github.com/MATPOWER/most/blob/ab17b56e1ae74baf2e1b7b5a7cd6ab4d5c27673f/README.md) and [`CITATION`](https://github.com/MATPOWER/most/blob/ab17b56e1ae74baf2e1b7b5a7cd6ab4d5c27673f/CITATION).

### 43. MATPOWER

- `repository`: `MATPOWER/matpower`
- `reviewed_commit`: `95d5a6fabb663167cf7eaff7f67acb41cddbad94`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. Its central functions solve steady-state power flow, continuation power flow, and OPF. |
| Labels | `gha`, `octave`, `university` | `octave`, `matlab`, `gha`, `university` | MATPOWER explicitly identifies itself as MATLAB/Octave M-files and supports both environments; Cornell stewardship and a workflow are confirmed. |
| `paper_id` | `10.1109/TPWRS.2010.2051168` | same | Confirmed. `CITATION` requires the 2011 MATPOWER paper for all use; other papers are conditional on MOST, MIPS, or specific subcomponents and do not belong on the base entry. |

Evidence: [README](https://github.com/MATPOWER/matpower/blob/95d5a6fabb663167cf7eaff7f67acb41cddbad94/README.md) and [`CITATION`](https://github.com/MATPOWER/matpower/blob/95d5a6fabb663167cf7eaff7f67acb41cddbad94/CITATION).

### 44. DPLib

- `repository`: `LSU-RAISE-LAB/DPLib`
- `reviewed_commit`: `7655ef17ca6712b7122ba187a76877b70619cfaa`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category, language, and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | `data` | Change. DPLib's primary artifact is a standard benchmark library of multi-region distributed cases; its bundled OPF solvers are explicitly validation/example tools. |
| Labels | `octave`, `university` | `matlab`, `university` | The project identifies itself as MATLAB-based and provides M-files; no explicit GNU Octave support was found. LSU stewardship is explicit and no workflow exists. |
| `paper_id` | absent | `arXiv:2506.20819` | Add. The README explicitly asks users of the library, generated datasets, partitioner, or solvers to cite this paper. |

Evidence: [README](https://github.com/LSU-RAISE-LAB/DPLib/blob/7655ef17ca6712b7122ba187a76877b70619cfaa/README.md).

```yaml
category: data
labels: ["matlab", "university"]
paper_id: arXiv:2506.20819
```

### 45. pandapower

- `repository`: `e2nIEE/pandapower`
- `reviewed_commit`: `4f139fa6215d7acc9004f003d41d9eb2f877ea5d`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired labels and shared stewardship)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. pandapower automates steady-state network analysis and optimization, including its own and integrated power-flow solvers. |
| Labels | `gha`, `pypi`, `conda`, `jupyter`, `python`, `university` | `python`, `gha`, `university`, `non-profit` | Python core and workflows are confirmed. The project explicitly describes joint stewardship by the University of Kassel and Fraunhofer IEE, so record both; remove retired labels. |
| `paper_id` | `10.1109/TPWRS.2018.2829021` | same | Confirmed against the repository's `CITATION.bib`. |

Evidence: [README](https://github.com/e2nIEE/pandapower/blob/4f139fa6215d7acc9004f003d41d9eb2f877ea5d/README.rst) and [`CITATION.bib`](https://github.com/e2nIEE/pandapower/blob/4f139fa6215d7acc9004f003d41d9eb2f877ea5d/CITATION.bib).

### 46. PYPOWER

- `repository`: `rwl/PYPOWER`
- `reviewed_commit`: `9c719bb14aa35183e2b77eca43796c5cdd19cdc7`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (stewardship, retired labels, and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. PYPOWER directly implements DC/AC power flow and OPF. |
| Labels | `gha`, `pypi`, `conda`, `python`, `non-profit` | `python`, `gha`, `community` | Python core and a workflow are confirmed. Current maintenance is an independent contributor repository rather than stewardship by PSERC, so `community` is a better current-state description; remove retired package labels. |
| `paper_id` | absent | `10.1109/TPWRS.2010.2051168` | Add. The README explicitly requests the MATPOWER paper for publications derived from the port; its separate `CITATION.bib` is only a software citation. |

Evidence: [README](https://github.com/rwl/PYPOWER/blob/9c719bb14aa35183e2b77eca43796c5cdd19cdc7/README.rst) and [`CITATION.bib`](https://github.com/rwl/PYPOWER/blob/9c719bb14aa35183e2b77eca43796c5cdd19cdc7/CITATION.bib).

### 47. EGRET

- `repository`: `grid-parity-exchange/Egret`
- `reviewed_commit`: `28c324f9bf4fb3913b0a60dba3dd732b46084c3b`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (`paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. EGRET implements UC, ED, DC/AC OPF, and alternative grid-optimization formulations. |
| Labels | `gha`, `python`, `lab` | `python`, `gha`, `lab` | Python core, workflows, and Sandia/NTESS stewardship are confirmed. |
| `paper_id` | absent | `10.1287/ijoc.2019.0944` | Add. The README explicitly requests this paper when using EGRET's unit-commitment functionality, which is a principal advertised capability. |

Evidence: [README](https://github.com/grid-parity-exchange/Egret/blob/28c324f9bf4fb3913b0a60dba3dd732b46084c3b/README.md) and repository copyright metadata.

### 48. PowerModels.jl

- `repository`: `lanl-ansi/PowerModels.jl`
- `reviewed_commit`: `dd456754f952269147e868bb905d36d8402bb8d3`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (`paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. It is explicitly a framework for steady-state power-network optimization and formulation comparison. |
| Labels | `gha`, `julia`, `lab` | `julia`, `gha`, `lab` | Julia core, workflows, and Los Alamos stewardship are confirmed. |
| `julia_id` | `PowerModels` | same | Confirmed against `Project.toml`. |
| `paper_id` | absent | `10.23919/PSCC.2018.8442948` | Add. The README explicitly asks users to cite the PowerModels publication. |

Evidence: [README](https://github.com/lanl-ansi/PowerModels.jl/blob/dd456754f952269147e868bb905d36d8402bb8d3/README.md).

### 49. VeraGrid

- `repository`: `SanPen/VeraGrid`
- `reviewed_commit`: `93d70a59cdc84856e69de42a79d98462a04e19a6`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. Although broad, the suite's central architecture and largest feature family remain grid construction, power flow, contingency analysis, and steady-state optimization; RMS and EMT are additional drivers. |
| Labels | `gha`, `pypi`, `python`, `for-profit` | `python`, `gha`, `for-profit` | The project explicitly identifies Python as its implementation language, contains workflows, and continues to connect its commercial distribution/services to eRoots; remove retired `pypi`. |
| `paper_id` | absent | absent | Confirmed skip. The repository presents a Zenodo software DOI badge but no paper citation instruction. |

Evidence: [README](https://github.com/SanPen/VeraGrid/blob/93d70a59cdc84856e69de42a79d98462a04e19a6/README.md).

### 50. GridPath

- `repository`: `blue-marble/gridpath` (redirects to `sylvan-energy/gridpath`)
- `reviewed_commit`: `4a2ed14dfe5b7bb448992a742bfad55f4f8862be`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (repository ID and retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. GridPath's central models cover production cost, capacity expansion, asset valuation, and resource adequacy planning. |
| Labels | `gha`, `pypi`, `python`, `for-profit` | `python`, `gha`, `for-profit` | Python core and workflows are confirmed, and the current steward is Sylvan Energy Analytics; remove retired `pypi`. |
| `github_id` | `blue-marble/gridpath` | `sylvan-energy/gridpath` | Update to the current canonical repository rather than relying on GitHub redirection. |
| `paper_id` | absent | absent | Confirmed skip. The displayed DOI is a Zenodo software DOI and no paper citation instruction exists. |

Evidence: [README](https://github.com/sylvan-energy/gridpath/blob/4a2ed14dfe5b7bb448992a742bfad55f4f8862be/README.md).

### 51. ExaGO

- `repository`: `pnnl/ExaGO` (archived; moved to `ORNL/ExaGO`)
- `reviewed_commit`: `545a8deb6fa35552f0ee402ca83672fe1255f61a`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (repository ID and language)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. ExaGO solves large-scale stochastic, contingency-constrained, multiperiod ACOPF problems. |
| Labels | `gha`, `jupyter`, `c`, `python`, `lab` | `cpp`, `gha`, `lab` | The active repository's computational core is C++ (`.cpp` sources); Python is explicitly a binding. Retire `jupyter`, replace the inaccurate C label, and retain workflows and laboratory stewardship. |
| `github_id` | `pnnl/ExaGO` | `ORNL/ExaGO` | Update. The PNNL repository is archived and explicitly directs development to ORNL. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README paper instruction exists in the active repository. |

Evidence: [archived-repository notice](https://github.com/pnnl/ExaGO/blob/d1a4298ca2a88f3e40166d612f641586ec0a49f1/README.md) and [active ORNL README](https://github.com/ORNL/ExaGO/blob/545a8deb6fa35552f0ee402ca83672fe1255f61a/README.md).

```yaml
github_id: ORNL/ExaGO
labels: ["cpp", "gha", "lab"]
```

### 52. Gurobi OptiMods

- `repository`: `Gurobi/gurobi-optimods`
- `reviewed_commit`: `b47087c0f08b816f105c97232a163a80f831bca6`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category and retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | `opl` | Change. The repository's primary role is exposing data-driven APIs that assemble many kinds of optimization use cases for Gurobi; OPF is one mod among a broad set. |
| Labels | `gha`, `pypi`, `python`, `for-profit` | `python`, `gha`, `for-profit` | Python core, workflows, and Gurobi stewardship are confirmed; remove retired `pypi`. |
| `paper_id` | absent | absent | Confirmed skip. No project citation file or explicit paper instruction exists; literature in individual mod documentation explains formulations. |

Evidence: [README](https://github.com/Gurobi/gurobi-optimods/blob/b47087c0f08b816f105c97232a163a80f831bca6/README.md) and [API index](https://github.com/Gurobi/gurobi-optimods/blob/b47087c0f08b816f105c97232a163a80f831bca6/docs/source/api.rst).

### 53. PowerFlowAnalyzer

- `repository`: `power-flow-analyzer/PowerFlowAnalyzer`
- `reviewed_commit`: `cd97fa59531c73a8a529270a7200d3fdc4d6269a`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category and language)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | `vis` | Change. The project says its main focus is modeling and visualizing transmission/distribution network data; MATPOWER is interfaced for the numerical computation. |
| Labels | `octave`, `java`, `university` | `matlab`, `java`, `university` | Java and MATLAB are both maintained first-party layers. No Octave support or workflow exists; the project identifies TU Berlin roots. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README paper instruction exists. |

Evidence: [README](https://github.com/power-flow-analyzer/PowerFlowAnalyzer/blob/cd97fa59531c73a8a529270a7200d3fdc4d6269a/Readme.md) and source layout.

### 54. ReEDS-2.0

- `repository`: `NatLabRockies/ReEDS-2.0` (archived; moved to `ReEDS-Model/ReEDS`)
- `reviewed_commit`: `f586f6c0fc1686166422ad2a5010f03fc72dee6a`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (repository identity and languages)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Name | `ReEDS-2.0` | `ReEDS` | The active project and repository now use the unversioned name. |
| Category | `steady-state` | same | Keep. ReEDS is NLR's long-term capacity-planning and dispatch optimization model. |
| Labels | `python`, `gha`, `lab` | `python`, `julia`, `gha`, `lab` | The active README explicitly says the maintained model is written in Python, GAMS, and Julia. Add Julia; GAMS cannot yet be represented by the approved label taxonomy. Workflows and NLR stewardship are confirmed. |
| `github_id` | `NatLabRockies/ReEDS-2.0` | `ReEDS-Model/ReEDS` | Update. The catalog repository is archived and points to this active canonical repository. |
| `paper_id` | absent | absent | Confirmed skip. `CITATION.cff` requests a software citation without a paper DOI; the README badge is a Zenodo software DOI. |

Evidence: [archive notice](https://github.com/NatLabRockies/ReEDS-2.0/blob/2f583ff5af61b36b0bed43a2deb6a2c1a1104650/README.md), [active README](https://github.com/ReEDS-Model/ReEDS/blob/f586f6c0fc1686166422ad2a5010f03fc72dee6a/README.md), and [active `CITATION.cff`](https://github.com/ReEDS-Model/ReEDS/blob/f586f6c0fc1686166422ad2a5010f03fc72dee6a/CITATION.cff).

Taxonomy note: GAMS is a primary model-authoring language here. This is the
second clear language-taxonomy gap found during the audit (after OpenDSS's
Object Pascal), and should be considered in the final portfolio summary.

### 55. GenX

- `repository`: `GenXProject/GenX`
- `reviewed_commit`: `3d9596ad9ce69e66ed0404754e58250059bf612b`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-current

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. GenX is a linear/mixed-integer capacity-expansion and operations optimization model. |
| Labels | `julia`, `gha`, `university` | same | Julia/JuMP core, workflows, and joint university stewardship are explicit. |
| `julia_id` | `GenX` | same | Confirmed against `Project.toml`. |
| `paper_id` | absent | absent | Confirmed skip. The requested citations are textual/Zenodo software citations, not a paper; prior publications are offered as examples rather than a substitute citation. |

Evidence: [README](https://github.com/GenXProject/GenX/blob/3d9596ad9ce69e66ed0404754e58250059bf612b/README.md) and [`CITATION.cff`](https://github.com/GenXProject/GenX/blob/3d9596ad9ce69e66ed0404754e58250059bf612b/CITATION.cff).

### 56. Power Grid Model

- `repository`: `PowerGridModel/power-grid-model`
- `reviewed_commit`: `4be7e8e6a446fbeb636efcc2b5bb2302b5936dc0`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language and retired labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. Its core calculations are distribution power flow, state estimation, and short circuit. |
| Labels | `gha`, `pypi`, `conda`, `python`, `c`, `jupyter`, `non-profit` | `cpp`, `gha`, `non-profit` | The README explicitly says the core is C++; Python and C are distributed interfaces. Workflows and LF Energy stewardship are confirmed; retire package/notebook labels. |
| `paper_id` | `10.1049/icp.2023.0633` | same | Confirmed as the conference paper listed by both the README and `CITATION.cff`. |

Evidence: [README](https://github.com/PowerGridModel/power-grid-model/blob/4be7e8e6a446fbeb636efcc2b5bb2302b5936dc0/README.md) and [`CITATION.cff`](https://github.com/PowerGridModel/power-grid-model/blob/4be7e8e6a446fbeb636efcc2b5bb2302b5936dc0/CITATION.cff).

### 57. EV-EcoSim

- `repository`: `ebalogun01/EV-EcoSim`
- `reviewed_commit`: `ccc78ddb69bdbce8b6a855d664b3140f9a8e45c7`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | `cosim` | Change. The project's defining role is coordinating EV/charging optimization with GridLAB-D grid simulation. |
| Labels | `gha`, `python`, `university` | `python`, `gha`, `university` | Python core, workflows, and Stanford project leadership are explicit. |
| `paper_id` | absent | `10.1109/TSG.2023.3339374` | Add. The README links this as the project paper and `CITATION.cff` says it must be cited. |

Evidence: [README](https://github.com/ebalogun01/EV-EcoSim/blob/ccc78ddb69bdbce8b6a855d664b3140f9a8e45c7/README.md) and [`CITATION.cff`](https://github.com/ebalogun01/EV-EcoSim/blob/ccc78ddb69bdbce8b6a855d664b3140f9a8e45c7/CITATION.cff).

### 58. DSSData

- `repository`: `felipemarkson/dssdata`
- `reviewed_commit`: `7c09ff841f5ee30acbaf1a400b5509681f28d4bf`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category and retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | `intf` | Change. DSSData is primarily a Python workflow/API layer around OpenDSS for repeated static, time-series, and probabilistic simulations, rather than the numerical power-flow implementation. |
| Labels | `gha`, `pypi`, `python` | `python`, `gha` | Python core and workflows are confirmed; remove retired `pypi`. No stewardship label has sufficient institutional evidence. |
| `paper_id` | absent | absent | Confirmed skip. The requested identifier in the README and `CITATION.cff` is a Zenodo software DOI. |

Evidence: [README](https://github.com/felipemarkson/dssdata/blob/7c09ff841f5ee30acbaf1a400b5509681f28d4bf/README.md) and [`CITATION.cff`](https://github.com/felipemarkson/dssdata/blob/7c09ff841f5ee30acbaf1a400b5509681f28d4bf/CITATION.cff).

### 59. TESP

- `repository`: `pnnl/tesp`
- `reviewed_commit`: `eab66e2a0141312a7a4d4140cb81253898fd622a`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category and retired labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | `cosim` | Change. TESP's primary role is coordinating GridLAB-D, EnergyPlus, market/power-flow tools, and other federates through HELICS/FNCS. |
| Labels | `gha`, `python`, `jupyter`, `pypi`, `lab` | `python`, `gha`, `lab` | Python is the maintained first-party support/orchestration layer; workflows and PNNL stewardship are confirmed. Retire notebook/package labels. |
| `paper_id` | absent | absent | Confirmed skip. Papers found in example documentation describe individual use cases; no repository-level citation instruction selects a core TESP paper. |

Evidence: [README](https://github.com/pnnl/tesp/blob/eab66e2a0141312a7a4d4140cb81253898fd622a/README.md) and package overview.

### 60. openTEPES

- `repository`: `IIT-EnergySystemModels/openTEPES`
- `reviewed_commit`: `7fc86b3901eef91f37660f7950a404e4a7be790e`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired labels and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. It formulates stochastic generation, storage, and multi-network operation/expansion planning. |
| Labels | `pypi`, `python`, `jupyter`, `gha`, `university` | `python`, `gha`, `university` | Python core, workflows, and Universidad Pontificia Comillas/IIT stewardship are explicit; retire package/notebook labels. |
| `paper_id` | absent | `10.1016/j.softx.2022.101070` | Add the SoftwareX paper explicitly requested in the README. Other case-study papers are conditional examples, not the project citation. |

Evidence: [README](https://github.com/IIT-EnergySystemModels/openTEPES/blob/7fc86b3901eef91f37660f7950a404e4a7be790e/README.md).

### 61. PyPSA-stochUC

- `repository`: `PPGS-Tools/PyPSA-stochUC`
- `reviewed_commit`: `783a04c10e95ca3ed7bc4c1926f66f3e2b610c2a`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-current

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. Its primary formulation is stochastic, multistage unit commitment. |
| Labels | `python` | same | Python is the maintained implementation. No workflow exists and current institutional stewardship is not stated strongly enough for a label. |
| `paper_id` | absent | absent | Confirmed skip. The README identifies the paper associated with the original tagged code but does not request it as the current project's citation. |

Evidence: [README](https://github.com/PPGS-Tools/PyPSA-stochUC/blob/783a04c10e95ca3ed7bc4c1926f66f3e2b610c2a/README.md).

### 62. hynet

- `repository`: `tum-msv/hynet` (GitLab)
- `reviewed_commit`: `d31e90169dca1bc54557bb936bfd63edaa98b401`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired label and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. hynet formulates nonconvex and relaxed OPF for hybrid AC/DC grids. |
| Labels | `pypi`, `python`, `university` | `python`, `university` | Python core and TUM stewardship are explicit; remove retired `pypi`. GitHub Actions is inapplicable to this GitLab repository. |
| `paper_id` | absent | `10.1109/TPWRS.2019.2942988` | Add the hynet paper explicitly requested in the README. A second paper is conditional on one network-reduction feature. |

Evidence: [README](https://gitlab.com/tum-msv/hynet/-/blob/d31e90169dca1bc54557bb936bfd63edaa98b401/README.md).

### 63. OATS

- `repository`: `bukhsh/oats`
- `reviewed_commit`: `80fc82da227f3810476832e078371e82c8aae5f4`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired label and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. OATS provides Pyomo models for a range of steady-state power-system analysis and optimization problems. |
| Labels | `pypi`, `python`, `university` | `python`, `university` | Python model code and University of Strathclyde stewardship are explicit; remove retired `pypi`. No workflow exists. |
| `paper_id` | absent | `10.1109/TPWRS.2020.2986081` | Add. The documentation explicitly requests both this journal paper and a non-paper manual citation; only the paper DOI belongs in `paper_id`. |

Evidence: [README](https://github.com/bukhsh/oats/blob/80fc82da227f3810476832e078371e82c8aae5f4/README.md) and [citation page](https://github.com/bukhsh/oats/blob/80fc82da227f3810476832e078371e82c8aae5f4/docs/intro/citation.rst).

### 64. Prescient

- `repository`: `grid-parity-exchange/Prescient`
- `reviewed_commit`: `8d8568f7ef562644d2483b3dd73e7d7cfbad843a`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (stewardship and retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. Prescient simulates production-cost operations through repeated RUC and SCED optimization. |
| Labels | `gha`, `pypi`, `python` | `python`, `gha`, `lab` | Python core and workflows are confirmed; source and package metadata establish Sandia/NTESS stewardship. Remove retired `pypi`. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or repository-level paper instruction exists. |

Evidence: [README](https://github.com/grid-parity-exchange/Prescient/blob/8d8568f7ef562644d2483b3dd73e7d7cfbad843a/README.md), `setup.py`, and `LICENSE.txt`.

### 65. US-REGEN

- `repository`: `epri-dev/US-REGEN`
- `reviewed_commit`: `5f0d2cca8d2eb2a9a20f3bf7c9b19394d75c9284`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-current with taxonomy gap

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. US-REGEN is an energy-economy optimization model centered on long-term regional energy and emissions decisions. |
| Labels | `non-profit` | same | EPRI stewardship is explicit and no workflow exists. The maintained core is GAMS, which the approved language labels cannot represent. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README paper instruction exists. |

Evidence: [README](https://github.com/epri-dev/US-REGEN/blob/5f0d2cca8d2eb2a9a20f3bf7c9b19394d75c9284/README.md) and first-party GAMS source.

### 66. PowerfulCases

- `repository`: `cuihantao/PowerfulCases`
- `reviewed_commit`: `1da5706b9ad744354640562d7d0e77dcac2b3da0`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category, languages, and retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `data` | `dataman` | Change. This is software for discovering, caching, loading, and managing case data; bundled test cases are secondary artifacts. |
| Labels | `gha`, `pypi`, `octave`, `python` | `python`, `julia`, `matlab`, `gha` | The repository maintains parallel first-party Python, Julia, and MATLAB APIs. No Octave support claim was found; remove retired `pypi`. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README paper instruction exists. |

Evidence: [README](https://github.com/cuihantao/PowerfulCases/blob/1da5706b9ad744354640562d7d0e77dcac2b3da0/README.md) and the three maintained source trees.

### 67. PowerDynData.jl

- `repository`: `cuihantao/PowerDynData.jl`
- `reviewed_commit`: `12ca70676b0818f390b57ed0d56cb8e0e56d8d5b`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `data` | `dataman` | Change. PowerDynData is parser/conversion software for DYR and TOML dynamic-model data, not a fixed dataset. |
| Labels | `julia`, `gha` | same | Julia core and workflows are confirmed; no institutional stewardship is claimed. |
| `julia_id` | `PowerDynData` | same | Confirmed against `Project.toml`. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README paper instruction exists. |

Evidence: [README](https://github.com/cuihantao/PowerDynData.jl/blob/12ca70676b0818f390b57ed0d56cb8e0e56d8d5b/README.md) and `Project.toml`.

### 68. RTS-GMLC

- `repository`: `GridMod/RTS-GMLC`
- `reviewed_commit`: `3ece0d3725c844056132393ee252b3083dd4eab4`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-current

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `data` | same | Keep. Its primary artifact is the RTS-GMLC benchmark dataset in source and tool-specific formats. |
| Labels | `lab` | same | NREL/DOE laboratory stewardship is explicit; conversion scripts are ancillary to the dataset and no workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. The README provides provenance and related calculations but no project paper citation instruction. |

Evidence: [README](https://github.com/GridMod/RTS-GMLC/blob/3ece0d3725c844056132393ee252b3083dd4eab4/README.md).

### 69. ERAD

- `repository`: `NLR-Distribution-Suite/erad`
- `reviewed_commit`: `27f6b8c28601cb1a17c12544a7a0462ace2d5a03`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category, retired label, and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `intf` | `steady-state` (provisional) | ERAD performs hazard/fragility, graph, Monte Carlo, and resilience analysis rather than interfacing another tool. `steady-state` is the closest current analysis category, but the final summary should consider a recurring resilience/reliability category if more examples emerge. |
| Labels | `gha`, `pypi`, `python`, `lab` | `python`, `gha`, `lab` | Python core, workflows, and NLR stewardship are confirmed; remove retired `pypi`. |
| `paper_id` | absent | `10.21105/joss.08782` | Add. The README prominently identifies the JOSS paper for the software. |

Evidence: [README](https://github.com/NLR-Distribution-Suite/erad/blob/27f6b8c28601cb1a17c12544a7a0462ace2d5a03/README.md).

### 70. powfacpy

- `repository`: `FraunhIEE-UniKassel-PowSysStability/powfacpy`
- `reviewed_commit`: `8b4fe3dd685ef4d7947277996b9b4d33f3a54547`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `intf` | same | Keep. It is explicitly a Python wrapper around the DIgSILENT PowerFactory API. |
| Labels | `pypi`, `python`, `non-profit` | `python`, `non-profit` | Python core and principal maintenance by Fraunhofer IEE are explicit; remove retired `pypi`. No workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README paper instruction exists. |

Evidence: [README](https://github.com/FraunhIEE-UniKassel-PowSysStability/powfacpy/blob/8b4fe3dd685ef4d7947277996b9b4d33f3a54547/README.md).

### 71. PSST

- `repository`: `ames-market/psst`
- `reviewed_commit`: `703492fa85fc384f47603cc5a34dfccbce14e457`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | same | Keep. PSST implements SCUC and SCED using Pyomo. |
| Labels | `gha`, `pypi`, `python`, `university` | `python`, `gha`, `university` | Python core, a workflow, and AMES/Iowa State stewardship are supported; remove retired `pypi`. |
| `paper_id` | absent | absent | Confirmed skip. The README points to a paper for details but does not request it as the project citation. |

Evidence: [README](https://github.com/ames-market/psst/blob/703492fa85fc384f47603cc5a34dfccbce14e457/README.rst).

### 72. matpower-pip

- `repository`: `yasirroni/matpower-pip`
- `reviewed_commit`: `138304aff28f8fe6d1d8d3bb18041bc2f82c6530`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `intf` | same | Keep. It packages Python access and startup integration for MATPOWER. |
| Labels | `gha`, `pypi`, `python`, `university` | `python`, `gha`, `university` | Python core, workflows, and UGM support are confirmed; remove retired `pypi`. |
| `paper_id` | absent | absent | Confirmed skip. Its specific requested citation is a Zenodo software record; the generic request for all applicable MATPOWER publications does not select one project paper. |

Evidence: [README](https://github.com/yasirroni/matpower-pip/blob/138304aff28f8fe6d1d8d3bb18041bc2f82c6530/README.md) and `CITATION.bib`.

### 73. mypower

- `repository`: `yasirroni/mypower`
- `reviewed_commit`: `df6d1e5a1895a2225ba74e24f2658e2a51d62bb8`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `steady-state` | `intf` | Change. The project is a Python/Oct2Py access and supplementary-function layer for MATPOWER, not the underlying solver. |
| Labels | `python`, `university` | same | Python is the maintained first-party code; Octave is an external runtime. UGM support is documented and no workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. The project requests a textual software citation and refers generically to applicable MATPOWER papers without selecting a paper for mypower. |

Evidence: [README](https://github.com/yasirroni/mypower/blob/df6d1e5a1895a2225ba74e24f2658e2a51d62bb8/README.md) and `CITATION.md`.

### 74. matpowercaseframes

- `repository`: `UGM-EPSLab/matpowercaseframes`
- `reviewed_commit`: `66f56efc8173c0d0211008c515e402cda51efa76`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `intf` | same | Keep. Its primary role is parsing MATPOWER cases into pandas data frames. |
| Labels | `gha`, `python`, `pypi`, `jupyter`, `university` | `python`, `gha`, `university` | Python parser core, workflows, and UGM stewardship are supported; remove retired labels. |
| `paper_id` | absent | absent | Confirmed skip. The README states that citing related UGM work is optional and only gives a software DOI for optional matpower-pip usage. |

Evidence: [README](https://github.com/UGM-EPSLab/matpowercaseframes/blob/66f56efc8173c0d0211008c515e402cda51efa76/README.md).

### 75. CIMTool-Builders-Library

- `repository`: `CIMug-org/CIMTool-Builders-Library`
- `reviewed_commit`: `375897f40bd420d4c66aa04020b39a97800d1cc9`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-current

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `intf` | same | Keep. The XSLT builders transform CIM schemas and profiles into interoperable artifacts. |
| Labels | `non-profit` | same | UCAIug/CIMug stewardship is confirmed; XSLT is not in the approved language taxonomy and no workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or project paper instruction exists. |

Evidence: [README](https://github.com/CIMug-org/CIMTool-Builders-Library/blob/375897f40bd420d4c66aa04020b39a97800d1cc9/README.md).

### 76. CIMTool

- `repository`: `CIMug-org/CIMTool`
- `reviewed_commit`: `c22dd50c8b2acdfcfbd0e126c045e28a76633e3f`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-current

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `intf` | same | Keep. CIMTool supports creation and editing of CIM profiles and related interoperability artifacts. |
| Labels | `gha`, `java`, `non-profit` | `java`, `gha`, `non-profit` | Java core, a workflow, and UCAIug stewardship are confirmed. AspenTech is described as a corporate sponsor, not the governing steward, so no `for-profit` label is added. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README paper instruction exists. |

Evidence: [README](https://github.com/CIMug-org/CIMTool/blob/c22dd50c8b2acdfcfbd0e126c045e28a76633e3f/README.md).

### 77. cimpyorm

- `repository`: `RWTH-IAEW/cimpyorm`
- `reviewed_commit`: `143406055ba962a5b152fc111084f9b4d5944e89`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category and retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `intf` | `dataman` | Change. Its defining role is parsing CIM/CGMES exports into a database-backed ORM for loading and querying datasets. |
| Labels | `gha`, `python`, `pypi`, `university` | `python`, `gha`, `university` | Python core, a workflow, and RWTH IAEW stewardship are confirmed; remove retired `pypi`. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README paper instruction exists. |

Evidence: [README](https://github.com/RWTH-IAEW/cimpyorm/blob/143406055ba962a5b152fc111084f9b4d5944e89/README.md) and package metadata.

### 78. CIMpy

- `repository`: `sogno-platform/cimpy`
- `reviewed_commit`: `ac400d43c015afc4ac58e7e833b91fcba6f32812`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category, retired label, and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `intf` | `dataman` | Change. CIMpy imports, modifies, and exports CIM/CGMES grid data and generated data classes; data transformation is its primary role. |
| Labels | `gha`, `pypi`, `python`, `non-profit` | `python`, `gha`, `non-profit` | Python core, workflows, and SOGNO stewardship are supported; remove retired `pypi`. |
| `paper_id` | absent | `10.1049/tje2.12208` | Add the paper explicitly requested in the README. |

Evidence: [README](https://github.com/sogno-platform/cimpy/blob/ac400d43c015afc4ac58e7e833b91fcba6f32812/README.md).

### 79. PSSE RAW

- `repository`: `anderson-optimization/em-psse`
- `reviewed_commit`: `f10da2a6c1cf44d790d709fefdab2117873209f1`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `intf` | `dataman` | Change. This package parses RAW files into pandas data frames and reformats their contents rather than interfacing the PSS/E application. |
| Labels | `python`, `for-profit` | same | Python core and Anderson Optimization stewardship are retained; no workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README paper instruction exists. |

Evidence: [README](https://github.com/anderson-optimization/em-psse/blob/f10da2a6c1cf44d790d709fefdab2117873209f1/README.md).

### 80. grg-pssedata

- `repository`: `lanl-ansi/grg-pssedata`
- `reviewed_commit`: `ea8c63e97f802ed69d985d318a0d5748e5c6de30`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category and retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `intf` | `dataman` | Change. It parses, validates, represents, and exports PSS/E data files without wrapping PSS/E itself. |
| Labels | `pypi`, `python`, `lab` | `python`, `lab` | Python core and LANL stewardship are explicit; remove retired `pypi`. No workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README paper instruction exists. |

Evidence: [README](https://github.com/lanl-ansi/grg-pssedata/blob/ea8c63e97f802ed69d985d318a0d5748e5c6de30/README.rst).

### 81. Andes.jl

- `repository`: `cuihantao/Andes.jl`
- `reviewed_commit`: `08736ee0011bf579317758d41c299f9e46049881`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (`julia_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `intf` | same | Keep. It exposes the ANDES Python API to Julia through PythonCall. |
| Labels | `gha`, `julia`, `university` | `julia`, `gha`, `university` | Julia core, workflows, and CURENT/university development are confirmed. |
| `julia_id` | absent | `Andes` | Add. `Project.toml` and the documented `Pkg.add("Andes")` identify the registered package name. |
| `paper_id` | absent | absent | Confirmed skip. No interface-specific paper citation is requested. |

Evidence: [README](https://github.com/cuihantao/Andes.jl/blob/08736ee0011bf579317758d41c299f9e46049881/README.md) and `Project.toml`.

### 82. OpenDER interface

- `repository`: `epri-dev/OpenDER_interface`
- `reviewed_commit`: `1faa70bf7bd911005dc30f7b5c3c3f8fe1cf9248`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `intf` | same | Keep. It couples OpenDER models to distribution simulators, currently OpenDSS. |
| Labels | `python`, `jupyter`, `non-profit` | `python`, `non-profit` | Python core and EPRI stewardship are supported; remove retired `jupyter`. No workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README paper instruction exists. |

Evidence: [README](https://github.com/epri-dev/OpenDER_interface/blob/1faa70bf7bd911005dc30f7b5c3c3f8fe1cf9248/README.rst).

### 83. PyDSS

- `repository`: `NatLabRockies/PyDSS`
- `reviewed_commit`: `c58d1fbf564c1677bbac01f0a43ffbd4be518510`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `intf` | same | Keep. PyDSS is explicitly a high-level Python interface extending OpenDSS workflows, analytics, and co-simulation. |
| Labels | `gha`, `pypi`, `python`, `lab` | `python`, `gha`, `lab` | Python core, workflows, and NLR stewardship are confirmed; remove retired `pypi`. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or repository-level paper instruction exists. |

Evidence: [README](https://github.com/NatLabRockies/PyDSS/blob/c58d1fbf564c1677bbac01f0a43ffbd4be518510/README.md).

### 84. AltDSS-Python

- `repository`: `dss-extensions/AltDSS-Python`
- `reviewed_commit`: `2b6fa7e5961cedaf8482c07d377b20bdab4a1bee`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired labels and stewardship)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `intf` | same | Keep. It is the high-level Python binding/API for the AltDSS engine. |
| Labels | `pypi`, `python`, `jupyter` | `python`, `community` | Python core and DSS-Extensions community stewardship are explicit; remove retired labels. No workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. No paper citation instruction exists. |

Evidence: [README](https://github.com/dss-extensions/AltDSS-Python/blob/2b6fa7e5961cedaf8482c07d377b20bdab4a1bee/README.md).

### 85. OpenDSSDirect.py

- `repository`: `dss-extensions/OpenDSSDirect.py`
- `reviewed_commit`: `d654af2055564881f10c343c94e640d0cfa6da4b`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired labels and stewardship migration)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `intf` | same | Keep. It implements a direct Python library interface to the DSS-Extensions engine. |
| Labels | `gha`, `pypi`, `python`, `jupyter`, `volunteer` | `python`, `gha`, `community` | Python core and a workflow are confirmed; retire package/notebook labels and migrate `volunteer` to `community`. |
| `paper_id` | absent | absent | Confirmed skip. `CITATION.cff` requests a software citation without a paper identifier. |

Evidence: [README](https://github.com/dss-extensions/OpenDSSDirect.py/blob/d654af2055564881f10c343c94e640d0cfa6da4b/README.md) and `CITATION.cff`.

### 86. OpenDSSDirect.jl

- `repository`: `dss-extensions/OpenDSSDirect.jl`
- `reviewed_commit`: `d5fdedb5310be9f94321711702ae6ce84acd616e`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (stewardship migration)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `intf` | same | Keep. It is a Julia direct-library interface to the DSS-Extensions engine. |
| Labels | `gha`, `julia`, `volunteer` | `julia`, `gha`, `community` | Julia core and workflows are confirmed; migrate `volunteer` to `community`. |
| `julia_id` | `OpenDSSDirect` | same | Confirmed against `Project.toml`. |
| `paper_id` | absent | absent | Confirmed skip. No paper citation instruction exists. |

Evidence: [README](https://github.com/dss-extensions/OpenDSSDirect.jl/blob/d5fdedb5310be9f94321711702ae6ce84acd616e/README.md).

### 87. AltDSS/DSS C-API

- `repository`: `dss-extensions/dss_capi`
- `reviewed_commit`: `f5728aec36becd20c19ad2dfc98fa8cf181f8835`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category and stewardship migration)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `intf` | `steady-state` | Change. Despite exposing a C API, this repository contains and maintains the full alternative OpenDSS simulation engine; downstream language projects provide the interfaces. |
| Labels | `gha`, `volunteer` | `gha`, `community` | A workflow and DSS-Extensions community stewardship are confirmed. The primary implementation is Pascal, which remains a taxonomy gap; the C files are API/examples rather than the engine core. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README paper instruction exists. |

Evidence: [README](https://github.com/dss-extensions/dss_capi/blob/f5728aec36becd20c19ad2dfc98fa8cf181f8835/README.md) and source layout.

### 88. DSS MATLAB

- `repository`: `dss-extensions/dss_matlab`
- `reviewed_commit`: `0d0f19aa9a030523248275d4d644aa65db494679`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language and stewardship)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `intf` | same | Keep. It is the maintained MATLAB interface to DSS C-API. |
| Labels | `gha`, `octave`, `volunteer` | `matlab`, `gha`, `community` | The first-party implementation is MATLAB and a workflow exists. No explicit Octave compatibility claim was found; migrate `volunteer` to `community`. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README paper instruction exists. |

Evidence: [README](https://github.com/dss-extensions/dss_matlab/blob/0d0f19aa9a030523248275d4d644aa65db494679/README.md) and source layout.

### 89. DSS Sharp

- `repository`: `dss-extensions/dss_sharp`
- `reviewed_commit`: `15de0f33c3cf8d1add3946d6b2f7d4845e52d343`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language and stewardship)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `intf` | same | Keep. It is explicitly the C#/.NET wrapper for DSS C-API. |
| Labels | `gha`, `volunteer` | `csharp`, `gha`, `community` | C# is the maintained implementation language and a workflow exists; migrate `volunteer` to `community`. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README paper instruction exists. |

Evidence: [README](https://github.com/dss-extensions/dss_sharp/blob/15de0f33c3cf8d1add3946d6b2f7d4845e52d343/README.md) and project files.

### 90. py-dss-interface

- `repository`: `PauloRadatz/py_dss_interface`
- `reviewed_commit`: `03f96d742953c6e7e7bc4baa3613dcbb49738312`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `intf` | same | Keep. It provides Python control of the official EPRI OpenDSS engine. |
| Labels | `pypi`, `python`, `jupyter`, `non-profit` | `python`, `non-profit` | Python is the maintained implementation and EPRI support is explicit. Remove retired package/notebook labels; no GitHub Actions workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. The README gives a textual software citation, not an explicit paper citation. |

Evidence: [README](https://github.com/PauloRadatz/py_dss_interface/blob/03f96d742953c6e7e7bc4baa3613dcbb49738312/README.md) and repository metadata.

### 91. Easy SimAuto

- `repository`: `mzy2240/ESA`
- `reviewed_commit`: `0c24c608313e316cb80e44c6555e1dca8ee45bca`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `intf` | same | Keep. ESA is a Python connector to PowerWorld Simulator's SimAuto automation server. |
| Labels | `pypi`, `python`, `university` | `python`, `university` | Python core and Texas A&M university authorship are explicit; remove retired `pypi`. No GitHub Actions workflow exists. |
| `paper_id` | `10.21105/joss.02289` | same | Keep. `CITATION.cff` names this JOSS article as the preferred citation and the documentation requests it. |

Evidence: [`CITATION.cff`](https://github.com/mzy2240/ESA/blob/0c24c608313e316cb80e44c6555e1dca8ee45bca/CITATION.cff), [citation documentation](https://github.com/mzy2240/ESA/blob/0c24c608313e316cb80e44c6555e1dca8ee45bca/docs/rst/citation.rst), and `setup.py`.

### 92. EasySimauto.jl

- `repository`: `mzy2240/EasySimauto.jl`
- `reviewed_commit`: `ba1ad793058d2547e003c1f28819a43651003772`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-current

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `intf` | same | Keep. It provides a Julia interface through ESA to PowerWorld SimAuto. |
| Labels | `gha`, `julia`, `university` | `julia`, `gha`, `university` | Julia core, workflows, and university authorship are confirmed. |
| `julia_id` | `EasySimauto` | same | Confirmed against `Project.toml`. |
| `paper_id` | absent | absent | Confirmed skip. No repository-level paper citation instruction exists. |

Evidence: [README](https://github.com/mzy2240/EasySimauto.jl/blob/ba1ad793058d2547e003c1f28819a43651003772/README.md) and `Project.toml`.

### 93. mhi-pscad

- `repository`: unavailable (official proprietary distribution)
- `reviewed_version`: `3.1.2`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `intf` | same | Keep. The package automates and remotely controls the PSCAD application. |
| Labels | `pypi`, `python`, `for-profit` | `python`, `for-profit` | Official documentation says the library is written in Python and authored by Manitoba Hydro International Ltd.; remove retired `pypi`. GitHub Actions cannot be assessed because no source repository is provided. |
| `paper_id` | absent | absent | Confirmed skip. No explicit paper citation was found in the official package page or documentation. |

Evidence: [official Automation Library page](https://www.pscad.com/software/pscad/automation-library), [official documentation](https://www.pscad.com/webhelp-v502-al/quick_start.html), and [PyPI metadata](https://pypi.org/project/mhi-pscad/).

### 94. powerfactory-tools

- `repository`: `ieeh-tu-dresden/powerfactory-tools`
- `reviewed_commit`: `89adb7bf390912652201d0819395bdd0e8150688`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `intf` | same | Keep. It is a Python toolbox for controlling and exchanging data with DIgSILENT PowerFactory. |
| Labels | `pypi`, `python`, `university`, `jupyter`, `gha` | `python`, `gha`, `university` | Python core, workflows, and TU Dresden stewardship are explicit; remove retired package/notebook labels. |
| `paper_id` | `10.21105/joss.09281` | same | Keep. Both the README and `CITATION.cff` explicitly select this JOSS paper. |

Evidence: [README](https://github.com/ieeh-tu-dresden/powerfactory-tools/blob/89adb7bf390912652201d0819395bdd0e8150688/README.md) and [`CITATION.cff`](https://github.com/ieeh-tu-dresden/powerfactory-tools/blob/89adb7bf390912652201d0819395bdd0e8150688/CITATION.cff).

### 95. Clarabel.jl

- `repository`: `oxfordcontrol/Clarabel.jl`
- `reviewed_commit`: `fbc5dd01576d47fda53861a992a02e93c8dbd03e`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-current

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `ops` | same | Keep. Clarabel.jl directly implements a primal-dual interior-point conic optimizer. |
| Labels | `gha`, `julia`, `university` | `julia`, `gha`, `university` | Julia core, workflows, and University of Oxford stewardship are confirmed. |
| `julia_id` | `Clarabel` | same | Confirmed against `Project.toml`. |
| `paper_id` | `arXiv:2405.12762` | same | Keep. The repository citation metadata explicitly requests this solver paper. |

Evidence: [README](https://github.com/oxfordcontrol/Clarabel.jl/blob/fbc5dd01576d47fda53861a992a02e93c8dbd03e/README.md), `Project.toml`, and `CITATION.bib`.

### 96. Clarabel.rs

- `repository`: `oxfordcontrol/Clarabel.rs`
- `reviewed_commit`: `b6aa0421ec818a31c7f26ada8f6cef2558c768bf`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language scope and retired labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `ops` | same | Keep. It directly implements a primal-dual interior-point conic optimizer. |
| Labels | `gha`, `pypi`, `conda`, `python`, `rust`, `university` | `rust`, `gha`, `university` | Rust is the primary developer-facing implementation. Python and Julia are binding layers, not additional core languages; remove retired package-manager labels. |
| `paper_id` | `arXiv:2405.12762` | same | Keep. `CITATION.bib` explicitly requests the Clarabel solver paper. |

Evidence: [README](https://github.com/oxfordcontrol/Clarabel.rs/blob/b6aa0421ec818a31c7f26ada8f6cef2558c768bf/README.md), source layout, and `CITATION.bib`.

### 97. CBC

- `repository`: `coin-or/Cbc`
- `reviewed_commit`: `c69261633774bbb47d367d550dda5419b0867e8c`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language scope and retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `ops` | same | Keep. CBC directly implements a branch-and-cut mixed-integer optimizer. |
| Labels | `gha`, `conda`, `python`, `julia`, `c`, `non-profit` | `cpp`, `gha`, `non-profit` | The maintained solver core is C++. Python and Julia are external interfaces rather than this repository's core implementation, `c` is inaccurate, and `conda` is retired. COIN-OR provides non-profit stewardship. |
| `paper_id` | absent | absent | Confirmed skip. The README's requested identifier is a Zenodo software DOI; related papers in the bibliography are not selected as the project citation. |

Evidence: [README](https://github.com/coin-or/Cbc/blob/c69261633774bbb47d367d550dda5419b0867e8c/README.md), source layout, and repository citation guidance.

### 98. Clp

- `repository`: `coin-or/Clp`
- `reviewed_commit`: `0ff4207ca7c82d5c5e9b19eb925dfcb79ed21f50`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (repository ID, language scope, and retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Canonical source | `coin-or/Cbc` | `coin-or/Clp` | Correct the copied CBC repository ID to Clp's own development repository. |
| Category | `ops` | same | Keep. Clp directly implements primal and dual simplex linear-programming solvers. |
| Labels | `gha`, `conda`, `python`, `julia`, `c`, `non-profit` | `cpp`, `gha`, `non-profit` | Clp explicitly identifies C++ as its implementation. Python and Julia are external interfaces, `c` is inaccurate, and `conda` is retired. Workflows and COIN-OR Foundation stewardship are confirmed. |
| `paper_id` | absent | absent | Confirmed skip. The requested identifier is a Zenodo software DOI rather than a paper. |

Evidence: [README](https://github.com/coin-or/Clp/blob/0ff4207ca7c82d5c5e9b19eb925dfcb79ed21f50/README.md) and source layout.

### 99. SCS

- `repository`: `cvxgrp/scs`
- `reviewed_commit`: `41efd34f7e83c682f41306328fa5404e87b4c315`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language scope and retired labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `ops` | same | Keep. SCS directly solves large-scale convex cone problems. |
| Labels | `gha`, `pypi`, `conda`, `python`, `octave`, `julia`, `r`, `c`, `university` | `c`, `gha`, `university` | The maintained solver core is C. Other languages are separately maintained interfaces; package labels are retired. Workflows and CVX-group university stewardship are retained. |
| `julia_id` | `SCS` | same | The external Julia interface remains correctly identified as structured package metadata, not a core-language label. |
| `paper_id` | `10.1007/s10957-016-0892-3` | same | Keep. `CITATION.cff` selects this article as the preferred citation. |

Evidence: [README](https://github.com/cvxgrp/scs/blob/41efd34f7e83c682f41306328fa5404e87b4c315/README.md) and [`CITATION.cff`](https://github.com/cvxgrp/scs/blob/41efd34f7e83c682f41306328fa5404e87b4c315/CITATION.cff).

### 100. ECOS

- `repository`: `embotech/ecos`
- `reviewed_commit`: `5d3aa62ef437e41c0314b4a16427d5d06a90b7e6`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language, stewardship, retired labels, and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `ops` | same | Keep. ECOS directly implements an embedded second-order-cone optimizer. |
| Labels | `pypi`, `conda`, `python`, `julia`, `c`, `octave`, `r`, `university` | `c` | ANSI C is the solver core; all other listed languages are external interfaces and package labels are retired. Current principal stewardship is not explicit enough to retain `university`; no workflow exists. |
| `julia_id` | `ECOS` | same | Retain the external Julia package identifier independently of the core-language decision. |
| `paper_id` | absent | `10.23919/ECC.2013.6669541` | Add the ECOS conference paper explicitly requested by the README. |

Evidence: [README](https://github.com/embotech/ecos/blob/5d3aa62ef437e41c0314b4a16427d5d06a90b7e6/README.md), source layout, and the [paper record](https://web.stanford.edu/~boyd/papers/ecos.html).

### 101. OSQP

- `repository`: `osqp/osqp`
- `reviewed_commit`: `1572ae068e9ce9ca723cf8223548ade1ff7acc29`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language scope and retired labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `ops` | same | Keep. OSQP directly implements an operator-splitting quadratic-program solver. |
| Labels | `gha`, `pypi`, `conda`, `python`, `c`, `julia`, `octave`, `r`, `university` | `c`, `gha`, `university` | The first-party solver core is C; other languages are interfaces and package labels are retired. Workflows and university-led stewardship are retained. |
| `julia_id` | `OSQP` | same | Retain the external Julia package identifier as structured metadata. |
| `paper_id` | `10.1007/s12532-020-00179-2` | same | Keep. `CITATION.cff` explicitly selects this paper. |

Evidence: [README](https://github.com/osqp/osqp/blob/1572ae068e9ce9ca723cf8223548ade1ff7acc29/README.md), [`CITATION.cff`](https://github.com/osqp/osqp/blob/1572ae068e9ce9ca723cf8223548ade1ff7acc29/CITATION.cff), and source layout.

### 102. PIQP

- `repository`: `PREDICT-EPFL/piqp`
- `reviewed_commit`: `2f16417cde0628928ad0103db4ea84b09a76552b`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language scope, retired labels, and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `ops` | same | Keep. PIQP directly implements a proximal interior-point quadratic-program solver. |
| Labels | `gha`, `pypi`, `conda`, `python`, `c`, `octave`, `r`, `university` | `cpp`, `gha`, `university` | PIQP explicitly identifies a header-only C++14 core. C, Python, MATLAB/Octave, and R are interfaces; package labels are retired. Workflows and EPFL stewardship are confirmed. |
| `paper_id` | absent | `10.1109/CDC49753.2023.10383915` | Add the main PIQP paper requested by the README. The additional `arXiv:2503.12664` request is conditional on use of one specialized backend. |

Evidence: [README](https://github.com/PREDICT-EPFL/piqp/blob/2f16417cde0628928ad0103db4ea84b09a76552b/README.md) and the [official package citation](https://pypi.org/project/piqp/).

### 103. AMPLPY

- `repository`: `ampl/amplpy`
- `reviewed_commit`: `5262d367cce8dae60e6682198c8d83075da88fb5`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category and retired labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `ops` | `intf` | Change. `amplpy` is explicitly a Python API intermediary to AMPL; AMPL performs model generation and solver interaction. |
| Labels | `gha`, `pypi`, `conda`, `jupyter`, `python`, `for-profit` | `python`, `gha`, `for-profit` | Python implements this separate interface package, workflows exist, and AMPL Optimization Inc. stewardship is explicit. Remove retired labels. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README paper instruction exists. |

Evidence: [README](https://github.com/ampl/amplpy/blob/5262d367cce8dae60e6682198c8d83075da88fb5/README.md) and package source.

### 104. Ipopt

- `repository`: `coin-or/Ipopt`
- `reviewed_commit`: `72a29c9aab198afa0dbb940339022a22c415a4eb`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language, retired labels, and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `ops` | same | Keep. Ipopt directly implements an interior-point nonlinear optimizer. |
| Labels | `pypi`, `conda`, `python`, `non-profit` | `cpp`, `non-profit` | The maintained implementation is C++; Python is an external interface and package labels are retired. COIN-OR stewardship is retained and no workflow exists. |
| `paper_id` | absent | `10.1007/s10107-004-0559-y` | Add the implementation paper explicitly requested under “Please Cite Us.” |

Evidence: [README](https://github.com/coin-or/Ipopt/blob/72a29c9aab198afa0dbb940339022a22c415a4eb/README.md) and source layout.

### 105. HiGHS

- `repository`: `ERGO-Code/HiGHS`
- `reviewed_commit`: `04024d701f79feb8e2f18bc3df0dffc04ef05088`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language scope and retired labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `ops` | same | Keep. HiGHS directly implements LP, QP, and MIP solvers. |
| Labels | `gha`, `pypi`, `conda`, `jupyter`, `python`, `c`, `julia`, `rust`, `r`, `cpp`, `university` | `cpp`, `c`, `gha`, `university` | C++ implements most solvers, while maintained C subsystems implement BasicLU and cuPDLP. Other languages are interfaces and retired labels are removed. Workflows and University of Edinburgh leadership are confirmed. |
| `julia_id` | `HiGHS` | same | Retain the external Julia package identifier. |
| `paper_id` | `10.1007/s12532-017-0130-5` | same | Keep. The README and `CITATION.cff` select this article. |

Evidence: [README](https://github.com/ERGO-Code/HiGHS/blob/04024d701f79feb8e2f18bc3df0dffc04ef05088/README.md), [`CITATION.cff`](https://github.com/ERGO-Code/HiGHS/blob/04024d701f79feb8e2f18bc3df0dffc04ef05088/CITATION.cff), and solver source layout.

### 106. PySCIPOpt

- `repository`: `scipopt/PySCIPOpt`
- `reviewed_commit`: `b89b56503d47d738eda15dda2e414e187a92c897`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category, stewardship, and retired labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `ops` | `intf` | Change. PySCIPOpt's primary role is a Python interface and extension mechanism for the separately implemented SCIP Optimization Suite. |
| Labels | `gha`, `pypi`, `conda`, `python`, `lab` | `python`, `gha`, `community` | Python implements this interface, workflows exist, and the README now says it is sustained by volunteer effort while seeking maintainers. Remove retired package labels and replace outdated laboratory stewardship. |
| `paper_id` | `10.1007/978-3-319-42432-3_37` | same | Keep. The README and `CITATION.bib` explicitly request this PySCIPOpt paper. |

Evidence: [README](https://github.com/scipopt/PySCIPOpt/blob/b89b56503d47d738eda15dda2e414e187a92c897/README.md) and [`CITATION.bib`](https://github.com/scipopt/PySCIPOpt/blob/b89b56503d47d738eda15dda2e414e187a92c897/CITATION.bib).

### 107. OptiVerse

- `repository`: `feyntech-opt/OptiVerse`
- `reviewed_commit`: `c8fe45d5486168149ae0b235a4592966738e1b5e`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category and stewardship migration)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `ops` | `education` | Change. The repository is a collection of worked optimization applications and reference scripts built on other solvers, not a reusable numerical solver implementation. |
| Labels | `python`, `volunteer` | `python`, `community` | Python implements the worked models and the README explicitly describes the collection as community-driven. Migrate the legacy stewardship label; no workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README paper instruction exists. |

Evidence: [README](https://github.com/feyntech-opt/OptiVerse/blob/c8fe45d5486168149ae0b235a4592966738e1b5e/README.md), directory layout, and representative worked-model documentation.

### 108. OR-Tools

- `repository`: `google/or-tools`
- `reviewed_commit`: `98c165af62df62b3056c2ee0fca66b24e79097cb`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language scope and retired labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `ops` | same | Keep. OR-Tools contains first-party constraint, SAT, linear, and routing solvers. |
| Labels | `gha`, `pypi`, `conda`, `python`, `cpp`, `java`, `for-profit` | `cpp`, `gha`, `for-profit` | C++ implements the solver suite. Python, Java, and C# are generated or binding layers rather than additional cores; package labels are retired. Workflows and Google stewardship are explicit. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README paper instruction exists. |

Evidence: [README](https://github.com/google/or-tools/blob/98c165af62df62b3056c2ee0fca66b24e79097cb/README.md) and solver source layout.

### 109. Tulip

- `repository`: `ds4dm/Tulip.jl`
- `reviewed_commit`: `aa9f803d4a110de807f80c56b850643fbe64437d`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (repository ID and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Canonical source | `google/or-tools` | `ds4dm/Tulip.jl` | Correct the copied OR-Tools repository ID to Tulip's official repository. |
| Category | `ops` | same | Keep. Tulip directly implements a primal-dual interior-point linear optimizer. |
| Labels | `gha`, `julia`, `university` | `julia`, `gha`, `university` | The pure-Julia solver core, workflows, and university research-group stewardship are confirmed. |
| `julia_id` | `Tulip` | same | Confirmed against `Project.toml`. |
| `paper_id` | absent | `10.1007/s12532-020-00200-8` | Add the Tulip paper explicitly requested by the README. |

Evidence: [README](https://github.com/ds4dm/Tulip.jl/blob/aa9f803d4a110de807f80c56b850643fbe64437d/README.md), [`CITATION.bib`](https://github.com/ds4dm/Tulip.jl/blob/aa9f803d4a110de807f80c56b850643fbe64437d/CITATION.bib), and `Project.toml`.

### 110. Xopt

- `repository`: `xopt-org/Xopt`
- `reviewed_commit`: `39d5e3f1ae255a049580d15e3b5ba19e30b1161b`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (repository ID, retired labels, and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Canonical source | `google/or-tools` | `xopt-org/Xopt` | Correct the copied OR-Tools repository ID to Xopt's current official organization. |
| Category | `ops` | same | Keep. Xopt supplies optimization algorithms that directly optimize arbitrary experimental or simulated evaluation functions. |
| Labels | `gha`, `python`, `pypi`, `conda`, `lab` | `python`, `gha`, `lab` | Python core, workflows, and SLAC-led development are confirmed; remove retired package labels. |
| `paper_id` | absent | `10.18429/JACoW-IPAC2023-THPL164` | Add the Xopt paper explicitly requested by the README. The separately offered Zenodo record is a software release. |

Evidence: [README](https://github.com/xopt-org/Xopt/blob/39d5e3f1ae255a049580d15e3b5ba19e30b1161b/README.md), package metadata, and the [JACoW paper record](https://proceedings.jacow.org/ipac2023/doi/jacow-ipac2023-thpl164).

### 111. MadNLP

- `repository`: `MadNLP/MadNLP.jl`
- `reviewed_commit`: `e102809626ae048d4d5690cb93f6e28f0032e5fd`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (stewardship)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `ops` | same | Keep. MadNLP directly implements an interior-point nonlinear optimizer with CPU and GPU backends. |
| Labels | `gha`, `julia`, `university` | `julia`, `gha`, `lab` | Julia core and workflows are confirmed. Current project authorship and the cited development work are Argonne-led, so laboratory stewardship is better supported than university stewardship. |
| `julia_id` | `MadNLP` | same | Confirmed against `Project.toml`. |
| `paper_id` | `arXiv:2307.16830`, `arXiv:2010.02404` | same | Keep. `CITATION.bib` still explicitly records these two identifiers; the README now presents their published forms without DOI fields. |

Evidence: [README](https://github.com/MadNLP/MadNLP.jl/blob/e102809626ae048d4d5690cb93f6e28f0032e5fd/README.md), [`CITATION.bib`](https://github.com/MadNLP/MadNLP.jl/blob/e102809626ae048d4d5690cb93f6e28f0032e5fd/CITATION.bib), and project documentation.

### 112. KVXOPT

- `repository`: `sanurielf/kvxopt`
- `reviewed_commit`: `cf4c028a58696ebd2085d2e00f48b9f2283d6c7a`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language, stewardship, and retired labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `ops` | same | Keep. KVXOPT retains CVXOPT's convex solvers and adds sparse-solver functionality. |
| Labels | `gha`, `pypi`, `conda`, `python`, `volunteer` | `python`, `c`, `gha` | Python and first-party C extensions implement the package; remove retired labels. A single independent fork maintainer does not by itself establish community stewardship, so the legacy label is removed rather than mechanically migrated. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README paper instruction exists. |

Evidence: [README](https://github.com/sanurielf/kvxopt/blob/cf4c028a58696ebd2085d2e00f48b9f2283d6c7a/README.md) and `src/python`/`src/C` source layout.

### 113. CVXOPT

- `repository`: `cvxopt/cvxopt`
- `reviewed_commit`: `a5aff2916006346d4100aeb1a8ee2230869127a2`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language scope and retired labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `ops` | same | Keep. CVXOPT directly supplies convex-optimization solvers and numerical primitives. |
| Labels | `gha`, `pypi`, `conda`, `python`, `octave`, `julia`, `university` | `python`, `c`, `gha`, `university` | Python and C substantially implement the maintained package. MATLAB and Julia are external interface repositories; package labels are retired. Workflows and university stewardship are retained. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README paper instruction exists. |

Evidence: [README](https://github.com/cvxopt/cvxopt/blob/a5aff2916006346d4100aeb1a8ee2230869127a2/README.md) and the first-party `src/python` and `src/C` trees.

### 114. PyOptInterface

- `repository`: `metab0t/PyOptInterface`
- `reviewed_commit`: `713da3380c9a5ed6ea2aa4636e8e404daac1f4c9`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language, stewardship, retired labels, and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `opl` | same | Keep. It constructs optimization models and passes them through a unified interface to numerical optimizers. |
| Labels | `gha`, `pypi`, `jupyter`, `python`, `volunteer` | `python`, `cpp`, `gha` | Official development documentation calls this a mixed C++/Python library and says the core parts are C++. Remove retired labels; public evidence does not establish community stewardship. |
| `paper_id` | absent | `10.1109/TPWRS.2024.3483489` | Add the OPF/code-generation paper explicitly requested in the README. |

Evidence: [README](https://github.com/metab0t/PyOptInterface/blob/713da3380c9a5ed6ea2aa4636e8e404daac1f4c9/README.md), [development documentation](https://github.com/metab0t/PyOptInterface/blob/713da3380c9a5ed6ea2aa4636e8e404daac1f4c9/docs/source/develop.md), and the [author's university publication record](https://www.eea.tsinghua.edu.cn/en/faculties/wuwench.htm).

### 115. RSOME

- `repository`: `XiongPengNUS/rsome`
- `reviewed_commit`: `1a0cf887efaa122e941651f8a40cc20d46f0dbf5`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired labels and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `opl` | same | Keep. RSOME formulates robust and stochastic optimization models and transforms them for external solvers. |
| Labels | `gha`, `pypi`, `jupyter`, `python`, `university` | `python`, `gha`, `university` | Python core, a workflow, and NUS/CUHK university maintenance are explicit; remove retired labels. |
| `paper_id` | absent | `10.1287/ijoc.2023.1291`, `10.1287/mnsc.2020.3603` | Add both papers explicitly requested by the README's citation section. |

Evidence: [README](https://github.com/XiongPengNUS/rsome/blob/1a0cf887efaa122e941651f8a40cc20d46f0dbf5/README.md).

### 116. CVXPY

- `repository`: `cvxpy/cvxpy`
- `reviewed_commit`: `2947be67b9f203674ae9d6705f852c9fbfafbfa5`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language, stewardship, retired labels, and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `opl` | same | Keep. CVXPY is explicitly a Python-embedded optimization modeling language, not a solver. |
| Labels | `gha`, `pypi`, `conda`, `python`, `university` | `python`, `cpp`, `gha`, `community` | Python implements the modeling system and C++ implements the maintained CVXCore canonicalization subsystem. The README now explicitly calls CVXPY a community project across institutions; remove package labels and replace university stewardship. |
| `paper_id` | absent | `10.1080/23307706.2017.1397554` | Add the DOI-bearing rewriting-system paper explicitly requested by the official citation page. Its jointly requested JMLR software paper has no DOI or arXiv identifier in the project citation. |

Evidence: [README](https://github.com/cvxpy/cvxpy/blob/2947be67b9f203674ae9d6705f852c9fbfafbfa5/README.md), [official citation page](https://github.com/cvxpy/cvxpy/blob/2947be67b9f203674ae9d6705f852c9fbfafbfa5/doc/source/resources/citing/index.rst), and CVXCore source.

### 117. Pyomo

- `repository`: `Pyomo/pyomo`
- `reviewed_commit`: `b953cf90d6ed26df46cb5924301a89e2e76716fa`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `opl` | same | Keep. Pyomo formulates and analyzes symbolic optimization models for standard solvers. |
| Labels | `gha`, `pypi`, `conda`, `jupyter`, `python`, `lab` | `python`, `gha`, `lab` | Python core, workflows, and Sandia/NTESS stewardship are supported; remove retired package/notebook labels. |
| `paper_id` | `10.1007/978-3-030-68928-5` | same | Keep. `CITATION.cff` explicitly selects this book as the preferred citation. |

Evidence: [README](https://github.com/Pyomo/pyomo/blob/b953cf90d6ed26df46cb5924301a89e2e76716fa/README.md), [`CITATION.cff`](https://github.com/Pyomo/pyomo/blob/b953cf90d6ed26df46cb5924301a89e2e76716fa/CITATION.cff), and license metadata.

### 118. JuMP

- `repository`: `jump-dev/JuMP.jl`
- `reviewed_commit`: `62b9c47e522821f4c0645d8a54d79ca67f6c7ebe`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `opl` | same | Keep. JuMP is a Julia-embedded domain-specific language for mathematical optimization. |
| Labels | `gha`, `jupyter`, `julia`, `non-profit` | `julia`, `gha`, `non-profit` | Julia core, workflows, and NumFOCUS sponsored-project stewardship are confirmed; remove retired `jupyter`. |
| `julia_id` | `JuMP` | same | Confirmed against `Project.toml`. |
| `paper_id` | `10.1007/s12532-023-00239-3` | same | Keep. The README and `CITATION.bib` identify this as the requested current JuMP paper; two older papers are provided only as earlier works. |

Evidence: [README](https://github.com/jump-dev/JuMP.jl/blob/62b9c47e522821f4c0645d8a54d79ca67f6c7ebe/README.md), [`CITATION.bib`](https://github.com/jump-dev/JuMP.jl/blob/62b9c47e522821f4c0645d8a54d79ca67f6c7ebe/CITATION.bib), and `Project.toml`.

### 119. ExaModels

- `repository`: `exanauts/ExaModels.jl`
- `reviewed_commit`: `027d69ef88cfa4389b36cd254d204ea3d5963c8b`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (stewardship)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `opl` | same | Keep. ExaModels is an algebraic modeling and automatic-differentiation layer specialized for SIMD nonlinear programs. |
| Labels | `gha`, `julia`, `university` | `julia`, `gha`, `lab` | Julia core and workflows are confirmed. Project documentation, maintainer contact, and the cited work support Argonne laboratory stewardship rather than university stewardship. |
| `julia_id` | `ExaModels` | same | Confirmed against `Project.toml`. |
| `paper_id` | `10.1016/j.epsr.2024.110651` | same | Keep. The repository citation metadata selects the published ExaModels/MadNLP application paper represented by this DOI. |

Evidence: [README](https://github.com/exanauts/ExaModels.jl/blob/027d69ef88cfa4389b36cd254d204ea3d5963c8b/README.md), [`CITATION.bib`](https://github.com/exanauts/ExaModels.jl/blob/027d69ef88cfa4389b36cd254d204ea3d5963c8b/CITATION.bib), and project documentation.

### 120. EnergyDataModel

- `repository`: `rebase-energy/EnergyDataModel`
- `reviewed_commit`: `40e4ebd3316ab9330fa50d54f6a6a2f7b35a4b15`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category and retired labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `data` | `dataman` | Change. This is software for representing, structuring, serializing, and converting energy-system data, not a fixed data resource. |
| Labels | `pypi`, `python`, `jupyter`, `for-profit` | `python`, `gha`, `for-profit` | Python core, a workflow, and rebase.energy stewardship are confirmed. Remove retired labels and add the observable workflow label. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or README paper instruction exists. |

Evidence: [README](https://github.com/rebase-energy/EnergyDataModel/blob/40e4ebd3316ab9330fa50d54f6a6a2f7b35a4b15/README.md) and `pyproject.toml`.

### 121. PowerGenome

- `repository`: `PowerGenome/PowerGenome`
- `reviewed_commit`: `499e18f2d5e2aa011cb90ab82d9764d659662655`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category and retired labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `data` | `dataman` | Change. PowerGenome acquires, combines, transforms, and constructs input datasets for capacity-expansion models. |
| Labels | `gha`, `pypi`, `conda`, `python` | `python`, `gha` | Python core and a workflow are confirmed; remove retired package labels. Contributor affiliations do not establish one current principal stewardship type. |
| `paper_id` | absent | absent | Confirmed skip. The README and `.zenodo.json` identify a software archive, not a project-recommended paper. |

Evidence: [README](https://github.com/PowerGenome/PowerGenome/blob/499e18f2d5e2aa011cb90ab82d9764d659662655/README.md) and [`.zenodo.json`](https://github.com/PowerGenome/PowerGenome/blob/499e18f2d5e2aa011cb90ab82d9764d659662655/.zenodo.json).

### 122. DeepSolar

- `repository`: `wangzhecheng/DeepSolar`
- `reviewed_commit`: `39643e97d628c9317aca398d28e37ed25472a7f6`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `data` | `mrl` | Change. The repository's primary formulation trains deep convolutional models to classify, segment, and localize residential solar panels; unavailable training data is not its public artifact. |
| Labels | `python`, `university` | same | The maintained model code is Python and the project is Stanford-led. No workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. The README points to a project website for details but does not explicitly request a project paper citation. |

Evidence: [README](https://github.com/wangzhecheng/DeepSolar/blob/39643e97d628c9317aca398d28e37ed25472a7f6/README.md) and model source.

### 123. Australian MV-LV Networks

- `repository`: `Team-Nando/MV-LV-Networks`
- `reviewed_commit`: `8429f8a19f7b95acca2965cc48f2736880e5b31c`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired/incidental labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `data` | same | Keep. The primary artifacts are four network datasets and anonymized residential-demand profiles. |
| Labels | `jupyter`, `python`, `university` | `university` | The single notebook/script is an ancillary demonstration rather than the dataset's core implementation; remove retired `jupyter` and incidental `python`. University of Melbourne team stewardship is explicit. |
| `paper_id` | absent | absent | Confirmed skip. The README links background work and a project report but does not request a repository-level paper citation. |

Evidence: [README](https://github.com/Team-Nando/MV-LV-Networks/blob/8429f8a19f7b95acca2965cc48f2736880e5b31c/README.md) and artifact layout.

### 124. Power Grid Lib - Optimal Power Flow

- `repository`: `power-grid-lib/pglib-opf`
- `reviewed_commit`: `dc6be4b2f85ca0e776952ec22cbd4c22396ea5a3`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (`paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `data` | same | Keep. Its primary artifact is a curated AC-OPF benchmark case library. |
| Labels | `non-profit` | same | IEEE PES Task Force stewardship is explicit. MATPOWER-format case files are data, not a MATLAB implementation label, and no workflow exists. |
| `paper_id` | absent | `arXiv:1908.02788` | Add the archive report explicitly named in the citation guidelines for these benchmarks. |

Evidence: [README](https://github.com/power-grid-lib/pglib-opf/blob/dc6be4b2f85ca0e776952ec22cbd4c22396ea5a3/README.md) and the [report record](https://arxiv.org/abs/1908.02788).

### 125. Power Grid Lib - Unit Commitment

- `repository`: `power-grid-lib/pglib-uc`
- `reviewed_commit`: `39a7f38cf4703de92f0291f0c873c2e98c789301`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-current

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `data` | same | Keep. Its primary artifact is a curated unit-commitment benchmark case library. |
| Labels | `non-profit` | same | IEEE PES Task Force stewardship is explicit. Small reference scripts are ancillary and no workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. The README requests different original-source citations conditionally by case family rather than selecting one project-level paper. |

Evidence: [README](https://github.com/power-grid-lib/pglib-uc/blob/39a7f38cf4703de92f0291f0c873c2e98c789301/README.md).

### 126. Power Grid Lib - Optimal Power Flow with HVDC Lines

- `repository`: `power-grid-lib/pglib-opf-hvdc`
- `reviewed_commit`: `f928f95cde06d035554d92854f03950e074850e0`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (`paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `data` | same | Keep. Its primary artifact is a set of benchmark AC/DC OPF cases with HVDC lines. |
| Labels | `non-profit` | same | IEEE PES Task Force stewardship is explicit. MATPOWER-format files are data, not a MATLAB implementation label, and no workflow exists. |
| `paper_id` | absent | `10.1109/TPWRS.2019.2897835` | Add the transactions paper explicitly identified as the extensive description of the case data and model. |

Evidence: [README](https://github.com/power-grid-lib/pglib-opf-hvdc/blob/f928f95cde06d035554d92854f03950e074850e0/README.md) and the linked [IEEE paper metadata](https://ieeexplore.ieee.org/document/8636236).

### 127. WECC-and-NPCC-Electricity-Economic-Data

- `repository`: `enliten/ENLITEN-Grid-Econ-Data`
- `reviewed_commit`: `20f5f0490404813427a2f9623fe4df6c9b7f8890`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (`paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `data` | same | Keep. The primary artifact is a reusable economic dataset for WECC and NPCC market studies. |
| Labels | `university` | same | University of Tennessee/CURENT stewardship is explicit. MATLAB construction and validation scripts are ancillary to the dataset and no workflow exists. |
| `paper_id` | absent | `10.1038/s41597-023-02448-w` | Add the Scientific Data paper the README explicitly asks users to cite. |

Evidence: [README](https://github.com/enliten/ENLITEN-Grid-Econ-Data/blob/20f5f0490404813427a2f9623fe4df6c9b7f8890/README.md) and the [publisher record](https://www.nature.com/articles/s41597-023-02448-w).

### 128. GridStatus

- `repository`: `gridstatus/gridstatus`
- `reviewed_commit`: `86001c44a5ab4ed7f261f8c6e0961ad81f1528fb`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category and retired labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `data` | `dataman` | Change. The Python library acquires and normalizes current ISO/RTO and EIA data rather than supplying a fixed dataset. |
| Labels | `gha`, `pypi`, `conda`, `python`, `for-profit` | `python`, `gha`, `for-profit` | The maintained core is Python, six workflows exist, and Grid Status states that it maintains the library; remove retired package labels. |
| `paper_id` | absent | absent | Confirmed skip. `CITATION.cff` describes the software and supplies no paper identifier. |

Evidence: [README](https://github.com/gridstatus/gridstatus/blob/86001c44a5ab4ed7f261f8c6e0961ad81f1528fb/README.md) and [`CITATION.cff`](https://github.com/gridstatus/gridstatus/blob/86001c44a5ab4ed7f261f8c6e0961ad81f1528fb/CITATION.cff).

### 129. powerplantmatching

- `repository`: `PyPSA/powerplantmatching`
- `reviewed_commit`: `f6215915b924563bab8ea275ab788be92e2e499c`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category and retired labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `data` | `dataman` | Change. The tool cleans, standardizes, combines, and augments power-plant databases. |
| Labels | `gha`, `pypi`, `conda`, `python`, `university` | `python`, `gha`, `university` | Python implements the tool, four workflows exist, and TU Berlin/PyPSA stewardship is explicit; remove retired package labels. |
| `paper_id` | `10.1016/j.esr.2018.11.004` | same | Confirmed current from the project citation metadata. |

Evidence: [README](https://github.com/PyPSA/powerplantmatching/blob/f6215915b924563bab8ea275ab788be92e2e499c/README.md) and [`CITATION.cff`](https://github.com/PyPSA/powerplantmatching/blob/f6215915b924563bab8ea275ab788be92e2e499c/CITATION.cff).

### 130. Atlite

- `repository`: `PyPSA/atlite`
- `reviewed_commit`: `7ec4529bc7636e1e5a7a130b65a0d26371d0b693`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category and retired labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `data` | `dataman` | Change. Atlite converts weather and land-use datasets into energy-system time series and potentials. |
| Labels | `gha`, `pypi`, `conda`, `jupyter`, `python`, `university` | `python`, `gha`, `university` | Python is the core, three workflows exist, and the PyPSA/TU Berlin team stewards it; remove retired labels. |
| `paper_id` | `10.21105/joss.03294` | same | Confirmed current from `CITATION.cff`. |

Evidence: [README](https://github.com/PyPSA/atlite/blob/7ec4529bc7636e1e5a7a130b65a0d26371d0b693/README.md) and [`CITATION.cff`](https://github.com/PyPSA/atlite/blob/7ec4529bc7636e1e5a7a130b65a0d26371d0b693/CITATION.cff).

### 131. OpenDataElia

- `canonical_source`: `https://opendata.elia.be/`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (stewardship)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `data` | same | Keep. The entry is Elia's public grid and market data portal. |
| Labels | `non-profit` | `for-profit` | Change. The portal attributes its datasets to Elia Transmission Belgium SA, whose parent Elia Group is a listed company. GitHub and language checks are not applicable. |
| `paper_id` | absent | absent | Confirmed skip. The portal does not request a project paper citation. |

Evidence: [Elia Open Data](https://opendata.elia.be/pages/home/?flg=en-gb) and [Elia's corporate report](https://www.elia.be/-/media/project/elia/shared/documents/elia-group/publications/annual-reports/2021/en/20210415_etb-annual-report-2020_en.pdf).

### 132. Data on Energy

- `repository`: `owid/energy-data`
- `reviewed_commit`: `7e387a16f70a510e433f8aac7efeac6faa1e5059`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-current

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `data` | same | Keep. The primary artifact is the fixed-version OWID energy dataset. |
| Labels | `non-profit` | same | Our World in Data is the current non-profit steward; no core implementation language or workflow applies. |
| `paper_id` | absent | absent | Confirmed skip. The README requests attribution to OWID and underlying sources but selects no project paper. |

Evidence: [README](https://github.com/owid/energy-data/blob/7e387a16f70a510e433f8aac7efeac6faa1e5059/README.md).

### 133. COVID-EMDA

- `repository`: `tamu-engineering-research/COVID-EMDA`
- `reviewed_commit`: `f066e2d89d4581ec1cab224402d94ee35713915d`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `data` | same | Keep. The public artifact is a cross-domain COVID-19 and electricity-market dataset. |
| Labels | `python`, `university` | `university` | Python processing files are ancillary to the dataset; Texas A&M stewardship is explicit. No workflow exists. |
| `paper_id` | absent | `arXiv:2005.06631` | Add the main paper explicitly requested by the README; other listed studies are contextual recommendations. |

Evidence: [README](https://github.com/tamu-engineering-research/COVID-EMDA/blob/f066e2d89d4581ec1cab224402d94ee35713915d/README.md).

### 134. SimBench

- `repository`: `e2nIEE/simbench`
- `reviewed_commit`: `c426a1a3fecbe986a868edc2beed56349c37baf7`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired labels and stewardship)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `data` | same | Keep. Its primary artifact is a benchmark grid dataset; the package provides access and conversion. |
| Labels | `gha`, `pypi`, `conda`, `jupyter`, `python` | `python`, `gha`, `university`, `non-profit` | Python and three workflows are confirmed. University Kassel and Fraunhofer IEE jointly coordinate the project; remove retired labels. |
| `paper_id` | absent | absent | Confirmed skip. The root README contains no explicit paper-citation request. |

Evidence: [README](https://github.com/e2nIEE/simbench/blob/c426a1a3fecbe986a868edc2beed56349c37baf7/README.md).

### 135. Electrical Signals Databases

- `repository`: `rte-france/digital-fault-recording-database`
- `reviewed_commit`: `0db3b67481970f674e0390c4142a6ea688914e26`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-current

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `data` | same | Keep. The repository supplies disturbance waveform records. |
| Labels | `for-profit` | same | RTE is the stated steward; no core language or workflow applies. |
| `paper_id` | absent | absent | Confirmed skip. The README gives a textual database attribution rather than a paper DOI or arXiv identifier. |

Evidence: [README](https://github.com/rte-france/digital-fault-recording-database/blob/0db3b67481970f674e0390c4142a6ea688914e26/README.md).

### 136. A new power system benchmark

- `repository`: `China-CSEE/Power-system-benchmark`
- `reviewed_commit`: `20ea4b3610bba0e14c4398b4d930e367c621be7e`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (`paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `data` | same | Keep. The primary artifact is a benchmark system and associated cases. |
| Labels | `lab` | same | China Electric Power Research Institute stewardship is explicit; no core language or workflow applies. |
| `paper_id` | absent | `10.13334/j.0258-8013.pcsee.230534` | Add the DOI-bearing paper explicitly listed by the README; the other listed works have no DOI or arXiv ID. |

Evidence: [README](https://github.com/China-CSEE/Power-system-benchmark/blob/20ea4b3610bba0e14c4398b4d930e367c621be7e/README.md).

### 137. pmuBAGE

- `repository`: `arleen-eng/pmuBAGE`
- `reviewed_commit`: `8b2498aae97ab77ca816a6a9deff89e21d0686e7`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (`paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `data` | same | Keep. The repository supplies synthetic PMU measurement data. |
| Labels | `university` | same | Academic stewardship is supported; scripts are ancillary and no workflow exists. |
| `paper_id` | absent | `arXiv:2204.01095` | Add the paper the README explicitly asks users to cite. |

Evidence: [README](https://github.com/arleen-eng/pmuBAGE/blob/8b2498aae97ab77ca816a6a9deff89e21d0686e7/README.md).

### 138. PyPSA MCP

- `repository`: `DanielSchmied/pypsa-mcp`
- `reviewed_commit`: `b771396ec065560b6f179f372fc3881d9a4d0dd6`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired and unsupported stewardship labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `llm` | same | Keep. Its primary role is exposing PyPSA through the Model Context Protocol. |
| Labels | `python`, `pypi`, `volunteer` | `python` | Python implements the server; remove the retired package label. A personal repository alone does not establish community stewardship. No workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or explicit README paper request exists. |

Evidence: [README](https://github.com/DanielSchmied/pypsa-mcp/blob/b771396ec065560b6f179f372fc3881d9a4d0dd6/README.md) and package source.

### 139. P-V Curve LLM

- `repository`: `CURENT/Power-Flow-Analysis-via-LLM`
- `reviewed_commit`: `7637acb6173e583f6c60efa3ed8e0cb2e99038c7`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-current

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `llm` | same | Keep. The project uses an LLM agent to conduct P–V curve analysis. |
| Labels | `python`, `university` | same | Python implements the workflow and CURENT/UTK stewardship is explicit. No GitHub Actions workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or explicit README paper request exists. |

Evidence: [README](https://github.com/CURENT/Power-Flow-Analysis-via-LLM/blob/7637acb6173e583f6c60efa3ed8e0cb2e99038c7/README.md).

### 140. PowerMCP

- `repository`: `Power-Agent/PowerMCP`
- `reviewed_commit`: `52deb675d3a83fd63948a18175158590622cc5ef`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (`gha`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `llm` | same | Keep. The package is a collection of MCP servers for power-system tools. |
| Labels | `python`, `university` | `python`, `gha`, `university` | Python implements the servers, two workflows exist, and Harvard Power and AI Initiative stewardship is explicit. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or explicit README paper request exists. |

Evidence: [README](https://github.com/Power-Agent/PowerMCP/blob/52deb675d3a83fd63948a18175158590622cc5ef/README.md) and [workflows](https://github.com/Power-Agent/PowerMCP/tree/52deb675d3a83fd63948a18175158590622cc5ef/.github/workflows).

### 141. PowerFM

- `repository`: `Power-Agent/PowerFM`
- `reviewed_commit`: `cc89c61cc0332c22863d891fc2d3e928ac5dbf66`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-current

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `llm` | same | Keep. The repository curates foundation models for power and energy work. |
| Labels | `university` | same | Harvard Power and AI Initiative stewardship is explicit; no maintained software core or workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or explicit README paper request exists. |

Evidence: [README](https://github.com/Power-Agent/PowerFM/blob/cc89c61cc0332c22863d891fc2d3e928ac5dbf66/README.md).

### 142. PowerWorkflow

- `repository`: `Power-Agent/PowerWF`
- `reviewed_commit`: `afd0eaa09dbc366999cef5ad70dcb87ab0e4c464`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-current

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `llm` | same | Keep. Its primary artifact is a collection of agentic power-system workflows. |
| Labels | `python`, `university` | same | Python implements the workflows and Harvard Power and AI Initiative stewardship is explicit. No GitHub Actions workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or explicit README paper request exists. |

Evidence: [README](https://github.com/Power-Agent/PowerWF/blob/afd0eaa09dbc366999cef5ad70dcb87ab0e4c464/README.md).

### 143. Daline

- `repository`: `JarvisETHZ/Daline`
- `reviewed_commit`: `ffb09a82945f2f3171b16216d3243b34e1bfaca8`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `mrl` | same | Keep. Daline derives data-driven linear power-flow models. |
| Labels | `octave`, `university` | `matlab`, `university` | The README explicitly describes a MATLAB toolbox and does not claim GNU Octave compatibility. No workflow exists. |
| `paper_id` | absent | `10.3929/ethz-b-000681867` | Add the publication explicitly requested in the README's citation section. |

Evidence: [README](https://github.com/JarvisETHZ/Daline/blob/ffb09a82945f2f3171b16216d3243b34e1bfaca8/README.md).

### 144. Grid2Op

- `repository`: `Grid2op/grid2op`
- `reviewed_commit`: `a1736886d18c14f6e19520813d2b3e432179e3b9`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired labels)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `mrl` | same | Keep. Grid2Op is a reinforcement-learning environment for sequential grid operation. |
| Labels | `gha`, `pypi`, `jupyter`, `python`, `for-profit` | `python`, `gha`, `for-profit` | Python is the core, four workflows exist, and RTE stewardship is explicit; remove retired labels. |
| `paper_id` | absent | absent | Confirmed skip. Project metadata provides software citation but no explicitly requested paper identifier. |

Evidence: [README](https://github.com/Grid2op/grid2op/blob/a1736886d18c14f6e19520813d2b3e432179e3b9/README.md) and citation metadata.

### 145. andes_gym

- `repository`: `cuihantao/andes_gym`
- `reviewed_commit`: `cea0b470239da1a4ade8636d4c3e7b9860c0af49`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `mrl` | same | Keep. It is a reinforcement-learning environment backed by ANDES. |
| Labels | `python`, `jupyter`, `university` | `python`, `university` | Python implements the environment and university stewardship is supported; remove `jupyter`. No workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or explicit README paper request exists. |

Evidence: [README](https://github.com/cuihantao/andes_gym/blob/cea0b470239da1a4ade8636d4c3e7b9860c0af49/README.md).

### 146. RLGC

- `repository`: `RLGC-Project/RLGC`
- `reviewed_commit`: `6471d67e6ee952ad99455d19c9b07036316e2b0d`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language, retired label, and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `mrl` | same | Keep. RLGC is a deep-reinforcement-learning environment for emergency grid control. |
| Labels | `python`, `jupyter`, `lab` | `python`, `java`, `lab` | Python and the Java/InterPSS server implement essential subsystems; remove `jupyter`. PNNL stewardship is explicit. No workflow exists. |
| `paper_id` | absent | `10.1109/TSG.2019.2933191` | Add the paper the README explicitly asks users to cite. |

Evidence: [README](https://github.com/RLGC-Project/RLGC/blob/6471d67e6ee952ad99455d19c9b07036316e2b0d/README.md) and the [DOE publication record](https://www.osti.gov/biblio/1605420).

### 147. OpenModelica

- `repository`: `OpenModelica/OpenModelica`
- `reviewed_commit`: `25015a6ea603be63341363472d29e474cdfb6b3a`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category ID and languages)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `cosime` | `cosim` | Apply the agreed ID migration. Co-simulation is the closest target category, although OpenModelica is more broadly an equation-based modeling and simulation environment. |
| Labels | `gha`, `modelica`, `python`, `university` | `modelica`, `c`, `cpp`, `gha`, `university` | Modelica/MetaModelica and the C/C++ compiler-runtime subsystems form the core; Python is an interface. Four workflows exist and university stewardship is explicit. |
| `paper_id` | `10.4173/mic.2020.4.1` | same | Confirmed current from `CITATION.cff`. |

Evidence: [README](https://github.com/OpenModelica/OpenModelica/blob/25015a6ea603be63341363472d29e474cdfb6b3a/README.md), source layout, and [`CITATION.cff`](https://github.com/OpenModelica/OpenModelica/blob/25015a6ea603be63341363472d29e474cdfb6b3a/CITATION.cff).

### 148. precice

- `repository`: `precice/precice`
- `reviewed_commit`: `124ee9bf387a24415a2308911871482072571431`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category ID, language, retired labels, and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `cosime` | `cosim` | Apply the agreed ID migration. The C++ library coordinates partitioned multiphysics simulations. |
| Labels | `gha`, `c`, `pypi`, `conda`, `university` | `cpp`, `gha`, `university` | C++, not C, implements the core; thirteen workflows exist and academic stewardship is explicit. Remove retired package labels. |
| `paper_id` | absent | `10.12688/openreseurope.14445.2` | Add the latest general reference paper explicitly requested by official project documentation. |

Evidence: [source repository](https://github.com/precice/precice/tree/124ee9bf387a24415a2308911871482072571431) and the official [literature guide](https://precice.org/fundamentals-literature-guide).

### 149. MPNG

- `repository`: `MATPOWER/mpng`
- `reviewed_commit`: `70d98d112117c9af07e81adf16c34b8314a6ab6c`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `gasnet` | same | Keep. MPNG formulates coupled optimal power and natural-gas flow. |
| Labels | `octave`, `university` | `matlab`, `university` | MATLAB is explicitly required; GNU Octave support is not claimed. No workflow exists. |
| `paper_id` | absent | `10.1109/TPWRS.2022.3195684` | Add the paper explicitly requested by the README. |

Evidence: [README](https://github.com/MATPOWER/mpng/blob/70d98d112117c9af07e81adf16c34b8314a6ab6c/README.md).

### 150. pandapipes

- `repository`: `e2nIEE/pandapipes`
- `reviewed_commit`: `5b52494e3f3d1ca29d6cdb89eb8653f449f41d43`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired labels, stewardship, and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `gasnet` | same | Keep. Its primary formulation is static and quasi-static gas and heat pipe-flow analysis. |
| Labels | `gha`, `pypi`, `jupyter`, `python`, `university` | `python`, `gha`, `university`, `non-profit` | Python is the core, four workflows exist, and University Kassel/Fraunhofer IEE share stewardship; remove retired labels. |
| `paper_id` | absent | `10.3390/su12239899` | Add the reference paper explicitly requested by the official project documentation. |

Evidence: [README](https://github.com/e2nIEE/pandapipes/blob/5b52494e3f3d1ca29d6cdb89eb8653f449f41d43/README.md) and the official [citation page](https://www.pandapipes.org/references/).

### 151. GasModels.jl

- `repository`: `lanl-ansi/GasModels.jl`
- `reviewed_commit`: `36cbbdfc038371d6bc2ea7a3b075e72b8cc8d580`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-current

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `gasnet` | same | Keep. The package formulates gas-network optimization problems. |
| Labels | `gha`, `julia`, `lab` | same | Julia is the core, four workflows exist, and LANL stewardship is explicit. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or explicit README paper request exists. `julia_id: GasModels` is consistent. |

Evidence: [README](https://github.com/lanl-ansi/GasModels.jl/blob/36cbbdfc038371d6bc2ea7a3b075e72b8cc8d580/README.md) and `Project.toml`.

### 152. HELICS

- `repository`: `GMLC-TDC/HELICS`
- `reviewed_commit`: `4f9d04c266b5c02c9113b4fd4b5dd507576c765d`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category, language, retired labels, and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `msg` | `cosim` | Change. HELICS identifies itself as a co-simulation framework whose primary role is time and execution coordination, not only message transport. |
| Labels | `gha`, `pypi`, `conda`, `python`, `julia`, `octave`, `java`, `c`, `lab` | `cpp`, `gha`, `lab` | C++ implements the broker/federate core; the other languages are APIs or bindings. Thirteen workflows exist and laboratory stewardship is explicit. |
| `paper_id` | absent | `10.1109/ACCESS.2024.3363615` | Add the current reference paper explicitly requested by the README. `julia_id: HELICS` remains valid. |

Evidence: [README](https://github.com/GMLC-TDC/HELICS/blob/4f9d04c266b5c02c9113b4fd4b5dd507576c765d/README.md) and core source layout.

### 153. LTB DiME

- `repository`: `CURENT/dime`
- `reviewed_commit`: `4aad0d6260818af6d0df6ed605413b28086e73a4`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language and `paper_id`)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `msg` | same | Keep. DiME's primary product is a distributed message transport server. |
| Labels | `c`, `python`, `octave`, `university` | `c`, `university` | C implements the core server; Python and MATLAB clients are bindings and GNU Octave is not claimed. No workflow exists. |
| `paper_id` | absent | three-identifier list below | Add all three publications the README explicitly requests. |

```yaml
paper_id:
  - arXiv:2211.11990
  - 10.1109/MPE.2019.2959054
  - 10.1109/TPWRS.2020.3017019
```

Evidence: [README](https://github.com/CURENT/dime/blob/4aad0d6260818af6d0df6ed605413b28086e73a4/README.md) and server/client source layout.

### 154. PowSyBl Diagram

- `repository`: `powsybl/powsybl-diagram`
- `reviewed_commit`: `ab67c4bf78f54824b32a074f82257d6c7121d7c7`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired label and stewardship)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `vis` | same | Keep. The component generates network-area and single-line diagrams from PowSyBl network models. |
| Labels | `gha`, `java`, `jupyter`, `for-profit` | `java`, `gha`, `non-profit` | Java implements the core and three workflows exist. Remove `jupyter`; PowSyBl is governed as an LF Energy/Linux Foundation Europe project rather than by one commercial steward. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or explicit README paper request exists. |

Evidence: [README](https://github.com/powsybl/powsybl-diagram/blob/ab67c4bf78f54824b32a074f82257d6c7121d7c7/README.md), source layout, and official [PowSyBl governance](https://www.powsybl.org/pages/project/governance.html).

### 155. LTB AGVis

- `repository`: `CURENT/agvis`
- `reviewed_commit`: `3bef98a0710106a7e3456bce74b44aabe75d746a`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `vis` | same | Keep. AGVis provides geographical visualization of network topology and simulation results. |
| Labels | `gha`, `pypi`, `python`, `university` | `python`, `gha`, `university` | Python implements the maintained application, one workflow exists, and CURENT/UTK stewardship is explicit; remove the retired package label. |
| `paper_id` | `10.1109/NAPS58826.2023.10318583` | same | Confirmed current from both `CITATION.bib` and the README's citation section. |

Evidence: [README](https://github.com/CURENT/agvis/blob/3bef98a0710106a7e3456bce74b44aabe75d746a/README.md) and [`CITATION.bib`](https://github.com/CURENT/agvis/blob/3bef98a0710106a7e3456bce74b44aabe75d746a/CITATION.bib).

### 156. PowerGraphics.jl

- `repository`: `NREL-Sienna/PowerGraphics.jl`
- `reviewed_commit`: `783e77ff1062397df9da92140c13752063d58d35`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `vis` | same | Keep. The Julia package visualizes results from the Sienna power-system modeling ecosystem. |
| Labels | `gha`, `julia`, `jupyter`, `lab` | `julia`, `gha`, `lab` | Julia implements the package, six workflows exist, and National Laboratory of the Rockies stewardship is explicit; remove `jupyter`. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or explicit README paper request exists. `julia_id: PowerGraphics` is consistent. |

Evidence: [README](https://github.com/NREL-Sienna/PowerGraphics.jl/blob/783e77ff1062397df9da92140c13752063d58d35/README.md) and `Project.toml`.

### 157. GSEIM

- `listed_repository`: `gseim/gseim` (unavailable on 2026-07-25)
- `fallback_source`: PyPI `GSEIM` 1.4 source distribution
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change with repository-verification caveat

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `pe` | same | Keep. Official documentation and the published source describe electrical-circuit simulation focused especially on power electronics. |
| Labels | `pypi`, `python`, `volunteer` | `python`, `cpp` | The published source describes a Python schematic/plotting application and a C++ solver as essential subsystems. Remove the retired package label; one PyPI maintainer does not establish community stewardship. GitHub Actions is unverifiable because the repository is unavailable. |
| `paper_id` | absent | absent | Confirmed skip. The package README links a related arXiv paper but does not explicitly ask users to cite it. |

Evidence: official [GSEIM documentation](https://gseim.github.io/build/html/index.html), [PyPI release](https://pypi.org/project/GSEIM/), and the inspected `GSEIM-1.4.tar.gz` README and source manifest.

### 158. PowerCyber Training

- `repository`: `PowerCyberTraining/powercybertraining.github.io`
- `reviewed_commit`: `038e90377c1d15031548401d480bcc32782dfe87`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category ID and retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `book` | `education` | Apply the agreed category migration. The primary artifact is a set of power-cyber training modules. |
| Labels | `jupyter`, `gha`, `python`, `university` | `python`, `gha`, `university` | Python is the executable language of 34 training notebooks, one workflow exists, and the named authors are university-based; remove `jupyter`. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or project-paper request exists; the book bibliography contains teaching references, not a project citation. |

Evidence: [README](https://github.com/PowerCyberTraining/powercybertraining.github.io/blob/038e90377c1d15031548401d480bcc32782dfe87/README.md), book configuration, and notebook metadata.

### 159. TextbookSimulations

- `repository`: `Power-Systems-Textbook/TextbookSimulations`
- `reviewed_commit`: `1bace95786e2e8ced581b5274cb021393c257a4d`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category ID and retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `book` | `education` | Apply the agreed category migration. The repository contains interactive examples and problems accompanying a power-systems textbook. |
| Labels | `julia`, `jupyter`, `university` | `julia`, `university` | Julia implements the notebooks and supporting tools; `.m` files are MATPOWER case data rather than MATLAB implementations. Remove `jupyter`. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or explicit README project-paper request exists. |

Evidence: [README](https://github.com/Power-Systems-Textbook/TextbookSimulations/blob/1bace95786e2e8ced581b5274cb021393c257a4d/README.md), notebook metadata, and source layout.

### 160. UTK ECE 522 - Power System Analysis II

- `repository`: `CURENT/ece522`
- `reviewed_commit`: `02c7a241ac3cbfc57052b1750967e43a9580dd4f`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category ID and retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `book` | `education` | Apply the agreed category migration. This is a UTK graduate-course tutorial and final project. |
| Labels | `python`, `jupyter`, `university` | `python`, `university` | Python is the executable language of the ANDES teaching notebooks and UTK stewardship is explicit; remove `jupyter`. No workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. The README identifies the ANDES framework paper as background but does not request a citation for this course repository. |

Evidence: [README](https://github.com/CURENT/ece522/blob/02c7a241ac3cbfc57052b1750967e43a9580dd4f/README.md) and notebook metadata.

### 161. ELEC0447 Analysis of Electric Power and Energy Systems

- `repository`: `bcornelusse/ELEC0447-analysis-power-systems`
- `reviewed_commit`: `dbf3759d438c5d3eea9e3cacf3c5f2528c8045fe`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category ID and retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `book` | `education` | Apply the agreed category migration. The entry is a master's-level power-systems course. |
| Labels | `python`, `jupyter`, `university` | `python`, `university` | Python is the course's stated scientific-computing language and powers its exercises; ULiège stewardship is explicit. Remove `jupyter`; no workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. Course bibliographies are topical references rather than an explicit repository paper citation. |

Evidence: [README](https://github.com/bcornelusse/ELEC0447-analysis-power-systems/blob/dbf3759d438c5d3eea9e3cacf3c5f2528c8045fe/README.md) and notebook metadata.

### 162. Tutorial on DER Hosting Capacity Part 0

- `repository`: `Team-Nando/Tutorial-DERHostingCapacity-0-dss_python`
- `reviewed_commit`: `093288584d84f15cc975b6bce5826d231d756b63`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category ID and retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `book` | `education` | Apply the agreed category migration. The artifact is an interactive introduction to DSS-Python for DER hosting-capacity studies. |
| Labels | `jupyter`, `python`, `university` | `python`, `university` | Python is the tutorial's executable language and Team Nando is university-based; remove `jupyter`. No workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or explicit README project-paper request exists. |

Evidence: [README](https://github.com/Team-Nando/Tutorial-DERHostingCapacity-0-dss_python/blob/093288584d84f15cc975b6bce5826d231d756b63/README.md) and notebook metadata.

### 163. Tutorial on DER Hosting Capacity Part 1

- `repository`: `Team-Nando/Tutorial-DERHostingCapacity-1-AdvancedTools_LV`
- `reviewed_commit`: `b3751cf37b336c09b3a59f1a8dbbe7ffdc3e3c6e`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category ID and retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `book` | `education` | Apply the agreed category migration. The artifact teaches advanced analysis of unbalanced LV networks. |
| Labels | `jupyter`, `python`, `university` | `python`, `university` | Python is the executable tutorial language and Team Nando is university-based; remove `jupyter`. No workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or explicit README project-paper request exists. |

Evidence: [README](https://github.com/Team-Nando/Tutorial-DERHostingCapacity-1-AdvancedTools_LV/blob/b3751cf37b336c09b3a59f1a8dbbe7ffdc3e3c6e/README.md) and notebook metadata.

### 164. Tutorial on DER Hosting Capacity Part 2

- `repository`: `Team-Nando/Tutorial-DERHostingCapacity-2-TimeSeries_LV`
- `reviewed_commit`: `a73bfebf91661b77e386ee2d7ea159bcdc003796`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category ID and retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `book` | `education` | Apply the agreed category migration. The artifact teaches time-series analysis and PV hosting-capacity assessment. |
| Labels | `jupyter`, `python`, `university` | `python`, `university` | Python is the executable tutorial language and Team Nando is university-based; remove `jupyter`. No workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or explicit README project-paper request exists. |

Evidence: [README](https://github.com/Team-Nando/Tutorial-DERHostingCapacity-2-TimeSeries_LV/blob/a73bfebf91661b77e386ee2d7ea159bcdc003796/README.md) and notebook metadata.

### 165. Tutorial on DER Hosting Capacity Part 3

- `repository`: `Team-Nando/Tutorial-DERHostingCapacity-3-VoltWatt_LV`
- `reviewed_commit`: `af5b83a9c7b8823170a3ea1c607c1bc771c15f69`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category ID and retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `book` | `education` | Apply the agreed category migration. The artifact teaches Volt-Watt control and PV hosting-capacity analysis. |
| Labels | `jupyter`, `python`, `university` | `python`, `university` | Python is the executable tutorial language and Team Nando is university-based; remove `jupyter`. No workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or explicit README project-paper request exists. |

Evidence: [README](https://github.com/Team-Nando/Tutorial-DERHostingCapacity-3-VoltWatt_LV/blob/af5b83a9c7b8823170a3ea1c607c1bc771c15f69/README.md) and notebook metadata.

### 166. Tutorial on DER Hosting Capacity Part 4

- `repository`: `Team-Nando/Tutorial-DERHostingCapacity-4-MonteCarlo_MV-LV`
- `reviewed_commit`: `ccadf79338dd01f41df9b2f769a2d734d81279fa`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category ID and retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `book` | `education` | Apply the agreed category migration. The artifact teaches Monte Carlo hosting-capacity assessment for integrated MV-LV networks. |
| Labels | `jupyter`, `python`, `university` | `python`, `university` | Python is the executable tutorial language and Team Nando is university-based; remove `jupyter`. No workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or explicit README project-paper request exists. |

Evidence: [README](https://github.com/Team-Nando/Tutorial-DERHostingCapacity-4-MonteCarlo_MV-LV/blob/ccadf79338dd01f41df9b2f769a2d734d81279fa/README.md) and notebook metadata.

### 167. LTB Demo

- `repository`: `CURENT/demo`
- `reviewed_commit`: `1a17426a9a2f9250a168bfd89ccc2dacab8b1ebd`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category ID and retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `book` | `education` | Apply the agreed category migration. Its primary artifact is a collection of worked LTB examples and benchmarks. |
| Labels | `jupyter`, `python`, `university` | `python`, `university` | Python implements the executable examples and CURENT/UTK stewardship is explicit; remove `jupyter`. No workflow exists. |
| `paper_id` | absent | absent | Confirmed skip. Citations inside individual case subdirectories apply to those imported cases, not to the LTB Demo collection as a whole. |

Evidence: [README](https://github.com/CURENT/demo/blob/1a17426a9a2f9250a168bfd89ccc2dacab8b1ebd/README.md), notebook metadata, and case-level READMEs.

### 168. COLIB

- `repository`: `CRESYM/colib0.github.io`
- `reviewed_commit`: `d56206b644c37f8899866f89f7321f9662b98cff`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category and stewardship)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `book` | `data` | Change. COLIB's primary artifact is a curated library of component models, networks, and test cases, not educational material; the Jekyll site presents that collection. |
| Labels | `gha`, `volunteer` | `gha`, `non-profit` | One workflow exists. CRESYM explicitly coordinates COLIB and is a registered non-profit association; site/build languages are incidental to the catalog artifact. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or collection-level paper request exists; model pages may carry their own references. |

Evidence: [README](https://github.com/CRESYM/colib0.github.io/blob/d56206b644c37f8899866f89f7321f9662b98cff/README.md), official [COLIB description](https://cresym.eu/colib/), and [CRESYM governance](https://cresym.eu/about-us/).

### 169. dsgrid

- `repository`: `dsgrid/dsgrid`
- `reviewed_commit`: `6d8c0bdc07db22119a118c1aac463546a77d23f0`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (language, retired label, and structured field)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `dataman` | same | Keep. The toolkit registers, queries, transforms, and serves demand-side grid datasets and projects. |
| Labels | `gha`, `python`, `pypi`, `lab` | `python`, `rust`, `gha`, `lab` | Python implements the API and Rust an integrated high-performance pattern-analysis subsystem; five workflows exist and laboratory stewardship is explicit. Remove `pypi`. |
| `paper_id` | absent | absent | Confirmed skip. No citation file or explicit README paper request exists. |
| `pypi_id` | `dsgrid` | remove for now | The current package metadata names `dsgrid-toolkit`, the README says no formal release exists, and the old `dsgrid` PyPI project does not establish this repository's package identity. |

Evidence: [README](https://github.com/dsgrid/dsgrid/blob/6d8c0bdc07db22119a118c1aac463546a77d23f0/README.md), `pyproject.toml`, `rust/Cargo.toml`, and the Rust subsystem documentation.

### 170. dGen

- `repository`: `NatLabRockies/dgen`
- `reviewed_commit`: `beb0df188607e8dd52eccc85d7c5e832c0c5e9e5`
- `reviewed_at`: 2026-07-25
- `decision`: confirmed-change (category and retired label)

| Field | Current | Recommended | Finding |
| --- | --- | --- | --- |
| Category | `dataman` | `steady-state` | Change. dGen is a bottom-up agent-based market-adoption and long-term planning model, not software whose primary role is data management. `steady-state` is the closest existing category because its definition includes related planning models; this is a documented boundary case. |
| Labels | `gha`, `python`, `jupyter`, `lab` | `python`, `gha`, `lab` | Python implements the model, two workflows exist, and laboratory stewardship is explicit; remove `jupyter`. |
| `paper_id` | absent | absent | Confirmed skip. The repository README and prescribed citation files do not explicitly request a project paper citation. |

Evidence: [README](https://github.com/NatLabRockies/dgen/blob/beb0df188607e8dd52eccc85d7c5e832c0c5e9e5/README.md), model source, and the official [dGen methodology overview](https://www.nrel.gov/analysis/dgen/about-dgen.html).

## Catalog-Wide Summary

### Completion and Decision Counts

| Measure | Count |
| --- | ---: |
| Catalog entries inspected | 170 |
| Entries with at least one recommended change | 147 |
| Entries confirmed current | 23 |
| Category changes, including agreed ID migrations | 59 |
| Category assignments retained | 111 |
| Label-set changes | 145 |
| Label sets retained | 25 |
| New `paper_id` recommendations | 40 |
| Existing `paper_id` values confirmed | 25 |
| Confirmed citation skips | 105 |

The high change count is expected: every occurrence of the retired categories
and labels is reported as a change even when the underlying project
classification is otherwise sound.

### Category Conclusions

The exclusive-category principle is workable for all 170 entries. The audit
supports the agreed migrations `phasor` → `electromechanical`, `cosime` →
`cosim`, and `book` → `education`. It also found substantive corrections where
the existing category described a repository artifact or historical placement
rather than the project's primary formulation.

The largest recurring corrections are:

- Seven software projects currently under `data` primarily acquire, construct,
  or transform data and should move to `dataman`.
- Four current `intf` entries primarily perform data management and should move
  to `dataman`.
- HELICS should move from `msg` to `cosim`; DiME remains in `msg` because its
  primary product is communication middleware.
- COLIB should move from `book` to `data`; it is a curated model and test-case
  library rather than an educational resource.
- dGen should move from `dataman` to `steady-state` as the closest existing
  planning category; it is an agent-based market-adoption model, not a data
  manager.

No new category is recommended yet. Three isolated boundary cases—ERAD
resilience analysis, OpenModelica's general equation-based simulation
environment, and dGen's agent-based planning simulation—do not presently form
a coherent recurring group. If similar entries are added, revisit a
reliability/resilience category or a broader planning/simulation category.

Keep `gasnet` as an explicit physical-domain exception and keep `pe` separate
from `emt`. Keep `msg` for now, but it becomes a one-entry category after HELICS
moves and should be reconsidered if DiME is removed or reframed.

### Label Conclusions

The audit supports the approved target portfolio:

- Remove `jupyter`, `pypi`, and `conda` from every label set. Package
  availability remains represented by structured IDs.
- Replace `volunteer` only when evidence supports `community`; do not migrate
  personal repositories mechanically.
- Add `matlab` where MATLAB is explicit and retain `octave` only where GNU
  Octave support is independently documented.
- Distinguish C from C++. Several current `c` assignments are C++ cores, while
  bindings and C APIs do not establish a C implementation.
- Add `csharp` to the taxonomy even though the current catalog produced only
  limited immediate use; it is still a necessary language distinction.
- Add `gha` to two entries and remove it from four entries based solely on
  workflow-file presence, as agreed.

Two implementation languages remain genuine vocabulary gaps: Object Pascal
for OpenDSS/DSS C-API and GAMS for ReEDS and US-REGEN. Add `pascal` and `gams`
before applying language corrections so these cores are not left
unrepresented. No JavaScript label is recommended from this audit because the
catalog did not establish a recurring need under the primary-core rule.

### Stewardship Conclusions

The five stewardship labels are sufficient. The audit does not justify adding
`consortium` or `public-sector`:

- LF Energy governance, as with PowSyBl, fits `non-profit`.
- CRESYM's explicit legal and maintenance role for COLIB fits `non-profit`.
- University–Fraunhofer collaborations can carry both `university` and
  `non-profit` when shared stewardship is explicit.
- Regulated or state-linked transmission operators organized as companies
  remain `for-profit` under the current institution-type definition.
- A personal repository or an open contribution invitation alone is not
  evidence of `community` stewardship.

### Citation Conclusions

The citation review found 40 missing project-recommended paper identifiers.
All are additions; no existing `paper_id` requires replacement. Twenty-five
existing values are confirmed current, and 105 entries have a confirmed skip.
Software archive DOIs, dataset DOIs, background references, and
feature-conditional papers were excluded unless the project explicitly asked
users to cite them for the listed artifact or principal capability.

### Structured-Metadata Findings

The audit identified these non-taxonomy corrections:

- `blue-marble/gridpath` → `sylvan-energy/gridpath`
- `pnnl/ExaGO` → `ORNL/ExaGO`
- `NatLabRockies/ReEDS-2.0` → `ReEDS-Model/ReEDS`
- add `julia_id: Andes`
- remove the unrelated `pypi_id: dsgrid`
- resolve or remove the unavailable `github_id: gseim/gseim`

All other inspected Julia identifiers were consistent with package metadata.

### Decision Queue Before Catalog Edits

The evidence supports proceeding with the planned catalog commits after the
following policy choices are accepted:

1. Accept provisional `steady-state` placement for ERAD and dGen.
2. Accept `cosim` as the closest current category for broad OpenModelica.
3. Add `pascal` and `gams` language labels before correcting affected entries.
4. Keep the one-entry `msg` category for DiME during this migration.
5. Treat regulated, company-form TSOs as `for-profit` unless foundation or
   association governance is the current project steward.

No tracked catalog changes or generated README changes are included in this
inspection report. Under the approved process, the report remains an ignored
local working artifact; repository edits begin only after this decision queue
is approved.

### Report Validation

The completed report contains 170 sequentially numbered entry headings, 170
category findings, 170 label findings, and 170 `paper_id` findings. Entry names
and order match `projects.yaml`. No target label recommendation contains
`jupyter`, `pypi`, `conda`, or `volunteer`.
