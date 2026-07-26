# Repository Modifications

This repository is based on the upstream `best-of` list template and the
`best-of-lists/best-of-update-action` workflow, but it carries several local
changes for the power-system software scope and weekly maintenance process.

## Workflow Changes

- The weekly update workflow uses `PAT_TOKEN` instead of the default
  `GITHUB_TOKEN` for branch creation, checkout, generator access, pull request
  creation, and draft release creation. This keeps the generated update branch,
  pull request, and release path aligned with this repository's permission
  model.
- The update workflow keeps the upstream generator action pinned to
  `best-of-lists/best-of-update-action@v0.8.5`.
- Generated wording for long-inactive projects is softened after generation:
  upstream "dead project" wording and the skull marker are replaced with
  "Long-inactive project" and the ice marker.
- A separate `finish-best-of-update` workflow verifies the reviewed update pull
  request, expected head SHA, draft release, merge result, release publication,
  and update-branch deletion. It can be triggered manually or by a trusted
  maintainer comment.

## List Configuration Changes

- The project list shows all curated entries by setting `min_stars: 0`,
  `min_projectrank: 0`, and `allowed_licenses: ["all"]`.
- Inactivity thresholds are tuned for this list: inactive after 12 months and
  long-inactive after 24 months.
- The category taxonomy is specific to power-system analysis, including phasor,
  EMT, steady-state, interface, gas simulation, co-simulation, optimization,
  data, power electronics, textbooks, and large language model tooling.
- The label taxonomy extends the template with language support, notebook
  examples, public GitHub Actions automation, package channels, and sponsor or
  steward type.
- The old Azure Pipelines label was removed. The GitHub Actions label now means
  public automation for validation, build, docs, release, publish, or deploy
  workflows rather than only generic CI.

## Header, Footer, and Citation Changes

- The README header is maintained through `config/header.md` and includes the
  project DOI, project count, contribution, creation, release-date, status,
  license, and repository-size badges.
- Visitor badges are intentionally omitted because third-party visitor counters
  have been unreliable and can create noisy external dependencies.
- The footer is maintained through `config/footer.md` and includes project
  scoring notes, data-collection limitations, related power-system resources,
  contribution guidance, and license information.
- The repository keeps a `CITATION` file and Zenodo DOI metadata so the list can
  be cited as a research dataset.

## Planned Metadata Extensions

Two important sources are not represented as first-class upstream generator
integrations in the current workflow:

- Julia package registry metadata. Julia projects are currently visible through
  the `julia` language label, but PyPI and Conda do not capture Julia package
  availability, releases, dependencies, or download-like adoption signals. This
  repository should add curated Julia registry metadata and decide how it feeds
  rendering and project scoring.
- Core paper DOI and citation metadata. Several projects are closely tied to a
  method, philosophy, or software paper. DOI and citation information can be an
  important adoption signal, but citation counts are provider-dependent and
  must be collected with a documented source and scoring rule.

The preferred long-run direction is to keep power-system-specific metadata
scripts in this repository first. A forked generator or custom GitHub Action
should be considered only if local scripts become hard to maintain or if the
metadata model becomes broadly useful to other best-of lists.

## Score Extension Experiment

The first local scoring extension uses these curated project fields:

- `julia_id`: Julia package name used by JuliaPkgStats and the Julia General
  registry ecosystem.
- `paper_id`: core software, method, or philosophy paper identifier. It accepts
  one DOI, one `arXiv:` identifier, or a list mixing both for projects with
  multiple official core citation papers.

The local scripts under `scripts/` extend the weekly update workflow:

- `validate_metadata.py` checks repository-specific metadata conventions.
- `collect_julia_metrics.py` collects Julia package-server user download
  counts through JuliaPkgStats.
- `collect_citation_metrics.py` collects DOI citation metadata from OpenAlex
  and records arXiv paper identifiers.
- `validate_collected_metrics.py` stops generation if applicable curated
  metadata is missing from collection or a provider returns an error.
- `score_adjustments.py` owns the bounded scoring formula shared by production
  generation and local previews.
- `best_of_score_extension.py` uses the generator's supported extension hook
  to add the adjustments before filtering, sorting, medal placement, history
  generation, and README rendering. It also registers Julia-package and paper
  detail integrations so `julia_id` links to JuliaHub and every DOI or arXiv
  `paper_id` links to its canonical record.
- `validate_applied_scores.py` verifies the generated history after the
  upstream action and fails the update if the hook did not apply exact scores.
- `preview_score_extensions.py` previews the same applied adjustments against
  the latest generated history CSV.

The score-extension formula is intentionally bounded and log-scaled:

- Julia adjustment: registration bonus plus a capped package-server monthly
  download score.
- Citation adjustment: one paper-record bonus per project plus capped
  lifetime and recent citation-count scores aggregated across the project's
  resolved DOI-backed core papers.
- A curated paper that is absent from OpenAlex keeps the paper-record bonus
  but receives no provider-dependent citation-count bonus.
- The raw components are retained in generated history, while their sum is
  rounded to an integer before it is added to the upstream integer score.

The weekly workflow collects and validates both metric sources before invoking
`best-of-update-action`. The extension records `upstream_projectrank`,
`julia_adjustment`, `citation_adjustment`, and `bestps_adjustment` in generated
history so each displayed score remains auditable.

The main fairness constraints are:

- Do not treat Julia package-server user requests as total Julia downloads.
- Do not treat OpenAlex citation counts as universal citation counts.
- Do not let raw downloads or citations dominate the upstream project score.
- Review rank movement across representative Python, Julia, solver, simulator,
  and data projects when changing the formula or caps.

Generated metric outputs should go under `metadata/generated/`, which is ignored
by default because those files are volatile snapshots.

## Local-Only Workspaces

The `.agents/` directory is ignored on purpose. It can hold local audit notes,
batch plans, and exploratory prompts during larger metadata investigations
without publishing that scratch work in the repository.
