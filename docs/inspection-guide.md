# Inspection Guide

- `status`: approved working guide
- `created_at`: 2026-07-25
- `catalog_source`: `projects.yaml`
- `baseline_report`: `inspection-report.md`

## Purpose

This is the single entry point for repeating an projects list inspection
of the catalog. It combines the classification philosophy with the operational
inspection process.

`projects.yaml` is always the canonical catalog. Inspection reports are
evidence and recommendations; they are not a second editable catalog.

## Core Model

- A **category** is the one exclusive classification of an entry by its primary
  mathematical formulation or, when no central formulation applies, its
  primary computational or artifact role.
- A **label** is a non-exclusive, independently verifiable fact about an entry,
  such as a primary developer-facing implementation language, observable
  GitHub Actions usage, or stewardship model.
- Every entry must have exactly one category.
- An entry may have zero or more labels.
- Secondary capabilities belong in notes or labels, not additional categories.
- Uncertain facts remain unassigned and are reported as ambiguous rather than
  guessed.

## Category Decision Order

For every entry:

1. Identify the project's primary advertised purpose.
2. Identify the mathematical or computational formulation that performs that
   purpose.
3. Choose the category representing the primary scientific or engineering
   computation.
4. For general frameworks, choose the primary computational role, such as
   formulating or solving an optimization problem.
5. If no central formulation applies, choose the primary artifact role, such
   as interface, data, visualization, or education.
6. When a simulator directly implements multiple time-domain or steady-state
   capabilities, choose the first applicable category in this order: `emt`,
   `electromechanical`, then `steady-state`.
7. Apply that capability precedence only to first-party simulation
   formulations. It does not override the artifact role of a wrapper, binding,
   parser, or other interface.
8. When several choices remain defensible, use the project's official scope
   and the main reason it belongs in this catalog.
9. Record unresolved cases as `ambiguous` for human review.

## Target Categories

| Target ID | Legacy ID | Title | Definition |
| --- | --- | --- | --- |
| `electromechanical` | `phasor` | Electromechanical Transient Simulation | Phasor-domain differential-algebraic simulation of electromechanical transients and related dynamic behavior. |
| `emt` | — | Electromagnetic Transient Simulation | Waveform-level time-domain circuit or network simulation using ODE/DAE models or discretized companion-circuit and nodal equivalents, including switching. |
| `steady-state` | — | Steady-State Analysis and Optimization | Steady-state power-system equations, including AC/DC power flow, OPF, economic dispatch, unit commitment, and related planning or operational optimization. |
| `intf` | — | Software Interface | A user-facing API, binding, wrapper, parser, or interchange bridge to another tool or format. |
| `gasnet` | — | Gas-Network Analysis | Modeling, simulation, or optimization of gas networks or tightly coupled gas-power systems. |
| `cosim` | `cosime` | Co-Simulation | Coordination of time, data exchange, and execution across two or more simulators. |
| `opl` | — | Optimization Modeling Language | Expression, transformation, or assembly of optimization problems for numerical solvers. |
| `ops` | — | Optimization Solver | Numerical solution of optimization problems supplied in an established mathematical form. |
| `mrl` | — | Machine and Reinforcement Learning | Machine learning, reinforcement learning, or another data-driven learning formulation applied to power-system work. |
| `vis` | — | Visualization | Visual representation of networks, states, results, or geographic information. |
| `msg` | — | Messaging Environment | Message transport or communication middleware between distributed simulation components. |
| `data` | — | Power-System Data | A dataset, benchmark, test case, measurement collection, model library, or other reusable data artifact. |
| `pe` | — | Power Electronics | Modeling or analysis centered on power-electronic devices, converters, controls, or circuits when broader than an EMT simulator. |
| `dataman` | — | Data Management | Software primarily acquiring, organizing, querying, converting, or constructing power-system data. |
| `education` | `book` | Educational Resources | Textbooks, courses, tutorials, worked examples, reference implementations, or training modules. |
| `llm` | — | Large-Language-Model Application | Work centered on LLMs, foundation models, agents, or model-context protocols. |

### Important Category Boundaries

- Power flow belongs to `steady-state` even when it is a feasibility problem
  rather than an optimization problem.
- EMT formulations may be expressed as ODEs or DAEs and then discretized into
  algebraic companion-circuit equations at each time step.
- Keep `emt` and `pe` distinct: EMT is waveform-level transient simulation;
  `pe` is centered on converters, devices, and their controls.
- A general solver belongs to `ops`; a formulation layer belongs to `opl`.
- A domain application remains in its scientific category even when it calls a
  general solver internally.
- A wrapper, parser, binding, or interchange bridge belongs to `intf`.
- A reusable dataset belongs to `data`; software whose main job is constructing
  or managing data belongs to `dataman`.
- Simulator orchestration belongs to `cosim`; retain `msg` only when message
  transport itself is the principal product.
- Keep `gasnet` as an explicit physical-domain exception unless a future audit
  supports a better portfolio-wide treatment.
- Do not add a category for a single awkward entry. Add one only when a
  coherent recurring group cannot be classified without violating these rules.

## Label Philosophy

Language labels describe the primary developer-facing implementation used to
build and maintain the project's first-party core.

- Do not label every supported user interface or binding.
- Exclude vendored, generated, copied, test, documentation, example, notebook,
  build-script, and binding-only code.
- Repository language statistics are candidate evidence, not a decision.
- Assign multiple languages only when they implement essential core
  subsystems.
- A C simulator with a Python binding normally receives `c`, not `python`.
- A separately listed Python wrapper receives `python` because Python
  implements that wrapper's core.
- A C++ core does not receive `c` merely because it exposes a C API.
- Assign `matlab` and `octave` independently; compatibility is not automatic.

## Target Labels

| ID | Legacy ID | Facet | Definition |
| --- | --- | --- | --- |
| `python` | — | Language | Python substantially implements the maintained first-party core. |
| `julia` | — | Language | Julia substantially implements the maintained first-party core. |
| `octave` | — | Language | GNU Octave is a primary implementation or model-authoring language. |
| `matlab` | — | Language | MATLAB is a primary implementation or model-authoring language. |
| `java` | — | Language | Java substantially implements the maintained first-party core. |
| `c` | — | Language | C substantially implements the maintained first-party core. |
| `cpp` | — | Language | C++ substantially implements the maintained first-party core. |
| `csharp` | — | Language | C# substantially implements the maintained first-party core. |
| `modelica` | — | Language | Modelica is a primary implementation or model-authoring language. |
| `rust` | — | Language | Rust substantially implements the maintained first-party core. |
| `r` | — | Language | R is a primary implementation or model-authoring language. |
| `pascal` | — | Language | Object Pascal substantially implements the maintained first-party core. |
| `gams` | — | Language | GAMS is a primary implementation or model-authoring language. |
| `gha` | — | Automation | At least one `.yml` or `.yaml` file exists under the public repository's `.github/workflows`. |
| `university` | — | Stewardship | A university-based team is the current principal steward. |
| `lab` | — | Stewardship | A national or government laboratory is the current principal steward. |
| `non-profit` | — | Stewardship | Another non-profit organization is the current principal steward. |
| `community` | `volunteer` | Stewardship | An independent contributor community is the current principal steward. |
| `for-profit` | — | Stewardship | A commercial organization is the current principal steward. |

The complete catalog audit confirmed recurring needs for `pascal` and `gams`;
both are approved target labels.

### Retired and Structured Metadata

- Remove `jupyter`; notebook presence is not a strong signal.
- Remove `pypi` and `conda` labels; use `pypi_id` and `conda_id`.
- Replace `volunteer` only when evidence supports `community`; do not migrate
  personal repositories mechanically.
- `julia_id` and `paper_id` are structured fields, not labels.
- Derive “has package,” “registered Julia package,” and “has paper” displays
  from structured fields rather than duplicating them as labels.

## Stewardship Determination

Stewardship describes current principal responsibility, not funding or original
authorship.

1. Prefer explicit governance, maintainer, team, or ownership statements.
2. Check official documentation and project websites for “maintained by” or
   equivalent language.
3. Treat organization ownership and maintainer affiliations only as supporting
   evidence.
4. Do not infer stewardship from a license, funder, original author, repository
   owner alone, or one contributor's affiliation.
5. Allow multiple labels only when current responsibility is explicitly shared.
6. Use no stewardship label and report `ambiguous` when evidence is
   insufficient.

The five stewardship types are presently sufficient. Do not add `consortium`
or `public-sector` unless repeated future evidence shows that the existing
types cannot represent a meaningful group.

## GitHub Actions Check

Assign `gha` if and only if the canonical public repository currently contains
at least one workflow file under `.github/workflows`.

This is deliberately a cheap observable check. It does not claim that CI/CD is
enabled, passing, comprehensive, or properly designed.

## Paper Citation Review

Review every entry, including entries with no current `paper_id`.

Check in this order:

1. Root and `.github` citation files such as `CITATION.cff`,
   `CITATION.bib`, `CITATION.md`, and case variants.
2. Project-authored `codemeta.json` or `.zenodo.json`.
3. An explicit “Citing,” “Citation,” “How to cite,” or equivalent README
   section.
4. Official project documentation only when repository sources do not settle
   the question.

For each entry:

- Extract DOI and `arXiv:` identifiers for papers the project explicitly asks
  users to cite.
- Do not automatically treat a software-release, dataset, or Zenodo archive DOI
  as a paper.
- Normalize and compare the complete requested set with the current scalar or
  list-valued `paper_id`.
- Recommend an addition when an explicit paper recommendation is missing.
- Recommend an update when the explicitly requested set differs.
- Preserve multiple identifiers when the project requests multiple core
  papers.
- Record a confirmed skip when no explicit paper recommendation exists.
- Do not substitute a paper found only through a general literature search for
  the project's own recommendation.

## Evidence Policy

Use current sources in this order:

1. Official repository files and organization metadata.
2. Official project documentation and governance pages.
3. Official package registries and release channels.
4. Project-authored papers, citation files, or institutional pages.
5. Third-party sources only as corroboration.

For external evidence, record the URL, access date, observed fact, and any
interpretation. Pin repository links to the reviewed commit when practical.

## Per-Entry Inspection Procedure

For every entry in `projects.yaml`:

1. Resolve the canonical repository or official project page.
2. Record the reviewed commit and inspection date.
3. Compare the current category with exactly one recommended target category.
4. Inspect repository structure, manifests, build files, and core source to
   determine implementation languages.
5. Determine stewardship using explicit current evidence.
6. Check `.github/workflows` and assign or remove `gha` mechanically.
7. Remove retired labels and inspect missing supported labels.
8. Review citation files, README, and when necessary official documentation.
9. Validate `pypi_id`, `conda_id`, `julia_id`, repository identity, and other
   structured fields.
10. Record one decision status and concise reasoning.
11. Add the completed entry to the report immediately; do not wait until the
    end of the batch.

### Required Review Record

Each entry must include:

- exact catalog name;
- canonical source and reviewed commit, when available;
- review date;
- current and recommended category;
- current and recommended labels;
- primary implementation-language evidence;
- stewardship evidence or `ambiguous`;
- GitHub Actions result;
- citation sources checked;
- current and recommended `paper_id`;
- relevant structured-field findings;
- decision status and boundary notes.

### Decision Status

- `confirmed-current`: current metadata is supported.
- `confirmed-change`: evidence supports a specific replacement.
- `ambiguous`: two or more defensible decisions remain.
- `unverifiable`: authoritative evidence is unavailable.
- `not-applicable`: the field does not apply.

Collect ambiguous and unverifiable findings in a decision queue before editing
the catalog.

## Inspection Strategy

Review related projects together so family-level decisions stay consistent:

1. `electromechanical`, `emt`, `pe`, `cosim`, `msg`, and `education`;
2. `opl` and `ops`;
3. `intf`, grouped by tool ecosystem;
4. `steady-state`, planning, operations, and markets;
5. `data` and `dataman`;
6. `gasnet`, `mrl`, `llm`, and `vis`.

Within these batches, compare related ecosystems such as PyPSA, Sienna,
OpenDSS, PowSyBl, MATPOWER, and LTB.

## Report Requirements

Create a new dated report for each full inspection. Do not overwrite the
previous report.

The report must contain:

1. scope, dates, catalog revision, and evidence policy;
2. counts of reviewed, changed, unchanged, ambiguous, and unverifiable entries;
3. category and label conclusions;
4. category, language, stewardship, `gha`, citation, and structured-field
   changes by project;
5. unresolved decisions and recommended follow-up;
6. a complete entry-by-entry record in `projects.yaml` order;
7. validation commands and results;
8. catalog commit list and generated-output review, if changes are later made.

Use a dated name such as:

`inspection-report-YYYY-MM-DD.md`

The 2026-07-25 baseline remains in `inspection-report.md`.

## Validation Gates

Before declaring an inspection complete:

1. Parse `projects.yaml`.
2. Verify the report contains every entry exactly once, in catalog order.
3. Verify every entry has one category finding, one label finding, and one
   `paper_id` finding.
4. Verify each recommendation uses only known target categories and labels.
5. Verify no recommendation contains `phasor`, `cosime`, `book`, `jupyter`,
   `pypi`, `conda`, or `volunteer`.
6. Check duplicate project names, repository IDs, package IDs, and Julia IDs.
7. Verify every proposed `paper_id` comes from explicit project-authored
   citation guidance.
8. Summarize category, label, citation, and structured-field changes.
9. Present the decision queue before changing `projects.yaml`.

If catalog changes are approved, additionally:

1. make changes on a feature branch in coherent commits;
2. run `scripts/validate_metadata.py`;
3. verify exactly one known category and only known labels per entry;
4. preserve all entries unless removal is separately approved;
5. generate the README with the pinned project tooling;
6. inspect category anchors, icons, counts, representative rows, and unexpected
   ranking or visibility changes;
7. inspect the complete branch diff before handoff.

## Recommended Catalog Commit Sequence

1. Migrate category identifiers.
2. Reclassify projects by primary formulation.
3. Update the label taxonomy and retire obsolete labels.
4. Correct implementation-language labels.
5. Correct stewardship and `gha`.
6. Align explicit paper citations.
7. Correct structured metadata.
8. Add taxonomy-invariant tests.
9. Align contributor documentation.

Keep each commit internally valid and split large diffs by a coherent category
or project ecosystem.
