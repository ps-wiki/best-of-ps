# Scoring and Data Collection

The list displays an empirical project-popularity score, called
`projectrank`. It is intended for comparison within this list and is not a
scientific measure of software quality.

The score has two parts:

```text
final projectrank = upstream projectrank
                    + round(Julia adjustment + citation adjustment)
```

The upstream score is calculated by the pinned
[`best-of-update-action`](https://github.com/best-of-lists/best-of-update-action)
and its best-of generator. Its documented inputs are:

- One-point project properties: homepage and description, repository, license,
  common license, multiple releases, semantic-versioned stable release, recent
  release, recent repository activity, and project age.
- Log-scaled GitHub and package-manager metrics: stars, contributors, commits,
  forks, monthly downloads, dependent projects, watchers, and closed issues.

See the upstream [project-quality score documentation](https://github.com/best-of-lists/best-of-generator#project-quality-score)
for the base formula and its limitations.

## Best-of-PS adjustment

This repository adds bounded, logarithmic adjustments for Julia registry usage
and curated core-paper citations before filtering, sorting, and rendering.

### Julia adjustment

```text
julia adjustment = registration bonus + monthly download score

registration bonus = 1 if a valid julia_id is collected, otherwise 0
monthly download score = min(6, max(0, ln(monthly_user_downloads / 2) - 1))
```

The monthly value is a JuliaPkgStats package-server user-request count. It is
not a count of all Julia ecosystem downloads.

### Citation adjustment

```text
citation adjustment = paper-record bonus
                    + lifetime citation score
                    + recent citation score

paper-record bonus = 1 when paper_id is present and collection succeeds
lifetime citation score = min(6, max(0, ln(cited_by_count / 2) - 1))
recent citation score = min(3, max(0, ln(recent_two_year_citations / 1.5)))
```

The current collector sums `cited_by_count` across all resolved DOI-backed
papers listed for a project. It also sums citation counts from the two most
recent years for those papers. A paper listed with an arXiv identifier can
receive the paper-record bonus, but does not receive DOI-backed OpenAlex
citation-count points.

This means the current formula does not award a separate point for each
publication, but multiple listed papers can increase the aggregate citation
score. Related papers can also cause double-counting when the same work cites
more than one paper. OpenAlex values are provider coverage, not universal
citation counts.

## Rounding and audit fields

The raw Julia and citation components are retained to three decimal places.
Their sum is rounded to an integer before it is added to the upstream integer
score. Generated history records `upstream_projectrank`, `julia_adjustment`,
`citation_adjustment`, `bestps_adjustment`, and the final `projectrank`.

The implementation is shared by generation and validation in
[`scripts/score_adjustments.py`](../scripts/score_adjustments.py),
[`scripts/best_of_score_extension.py`](../scripts/best_of_score_extension.py),
and [`scripts/validate_applied_scores.py`](../scripts/validate_applied_scores.py).

## Data collection limitations

Project data is collected from GitHub, package registries, JuliaPkgStats, and
OpenAlex where the relevant project metadata is configured. Coverage can be
incomplete for projects that are not primarily hosted or distributed through
those services. Provider definitions and snapshots can change between weekly
updates.
