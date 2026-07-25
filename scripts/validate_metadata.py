#!/usr/bin/env python3
"""Validate best-of-ps project metadata conventions."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - exercised only when env is missing deps.
    print(
        "error: PyYAML is required. Run with `conda run -n bestps python scripts/validate_metadata.py`.",
        file=sys.stderr,
    )
    raise SystemExit(2)


DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$", re.IGNORECASE)


def load_projects(path: Path) -> list[dict[str, Any]]:
    data = yaml.safe_load(path.read_text())
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML mapping")
    projects = data.get("projects")
    if not isinstance(projects, list):
        raise ValueError(f"{path} must contain a projects list")
    return projects


def validate_project(project: dict[str, Any], index: int) -> list[str]:
    errors: list[str] = []
    name = project.get("name", f"project #{index}")

    paper_doi = project.get("paper_doi")
    if paper_doi is not None:
        if not isinstance(paper_doi, str) or not DOI_RE.match(paper_doi.strip()):
            errors.append(f"{name}: paper_doi must look like a DOI, e.g. 10.xxxx/yyyy")

    paper_dois = project.get("paper_dois")
    if paper_dois is not None:
        if not isinstance(paper_dois, list):
            errors.append(f"{name}: paper_dois must be a list of DOI strings")
        else:
            seen_dois = {paper_doi.strip().lower()} if isinstance(paper_doi, str) else set()
            for doi_index, doi in enumerate(paper_dois, start=1):
                if not isinstance(doi, str) or not DOI_RE.match(doi.strip()):
                    errors.append(f"{name}: paper_dois[{doi_index}] must look like a DOI, e.g. 10.xxxx/yyyy")
                    continue
                normalized = doi.strip().lower()
                if normalized in seen_dois:
                    errors.append(f"{name}: paper_dois[{doi_index}] duplicates another DOI")
                seen_dois.add(normalized)

    julia_id = project.get("julia_id")
    if julia_id is not None:
        if not isinstance(julia_id, str) or not julia_id.strip():
            errors.append(f"{name}: julia_id must be a non-empty string")
        elif "/" in julia_id:
            errors.append(f"{name}: julia_id should be the registry package name, not a URL or owner/name path")

    return errors


def summarize(projects: list[dict[str, Any]]) -> str:
    julia_count = sum(1 for project in projects if project.get("julia_id"))
    paper_metadata_count = sum(1 for project in projects if project.get("paper_doi") or project.get("paper_dois"))
    return (
        f"Validated {len(projects)} projects "
        f"({julia_count} julia_id, {paper_metadata_count} paper citation metadata)."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default="projects.yaml", type=Path)
    args = parser.parse_args()

    try:
        projects = load_projects(args.path)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    errors: list[str] = []
    for index, project in enumerate(projects, start=1):
        if not isinstance(project, dict):
            errors.append(f"project #{index}: entry must be a YAML mapping")
            continue
        errors.extend(validate_project(project, index))

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(summarize(projects))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
