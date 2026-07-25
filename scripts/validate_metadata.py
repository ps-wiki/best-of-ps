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
ARXIV_RE = re.compile(r"^arxiv:(\d{4}\.\d{4,5})(v\d+)?$", re.IGNORECASE)


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

    paper_id = project.get("paper_id")
    if paper_id is not None:
        paper_ids = paper_id if isinstance(paper_id, list) else [paper_id]
        if not isinstance(paper_id, (str, list)):
            errors.append(f"{name}: paper_id must be a string or a list of strings")
        elif not paper_ids:
            errors.append(f"{name}: paper_id list must not be empty")
        else:
            seen_ids: set[str] = set()
            for paper_index, identifier in enumerate(paper_ids, start=1):
                if not isinstance(identifier, str):
                    errors.append(f"{name}: paper_id[{paper_index}] must be a string")
                    continue
                normalized = identifier.strip().lower()
                if not DOI_RE.match(normalized) and not ARXIV_RE.match(normalized):
                    errors.append(
                        f"{name}: paper_id[{paper_index}] must look like a DOI or arXiv id, "
                        "e.g. 10.xxxx/yyyy or arXiv:2405.12762"
                    )
                    continue
                if normalized in seen_ids:
                    errors.append(f"{name}: paper_id[{paper_index}] duplicates another paper identifier")
                seen_ids.add(normalized)

    julia_id = project.get("julia_id")
    if julia_id is not None:
        if not isinstance(julia_id, str) or not julia_id.strip():
            errors.append(f"{name}: julia_id must be a non-empty string")
        elif "/" in julia_id:
            errors.append(f"{name}: julia_id should be the registry package name, not a URL or owner/name path")

    return errors


def summarize(projects: list[dict[str, Any]]) -> str:
    julia_count = sum(1 for project in projects if project.get("julia_id"))
    paper_metadata_count = sum(1 for project in projects if project.get("paper_id"))
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
