#!/usr/bin/env python3
"""Require complete, error-free metric collection before list generation."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import yaml

from score_adjustments import load_json


def load_projects(path: Path) -> list[dict[str, Any]]:
    data = yaml.safe_load(path.read_text())
    projects = data.get("projects") if isinstance(data, dict) else None
    if not isinstance(projects, list):
        raise ValueError(f"{path} must contain a projects list")
    return [project for project in projects if isinstance(project, dict)]


def rows_by_name(
    payload: dict[str, Any], source: str
) -> tuple[dict[str, Any], list[str]]:
    rows = payload.get("projects")
    if not isinstance(rows, list):
        return {}, [f"{source}: projects must be a list"]

    indexed: dict[str, Any] = {}
    errors: list[str] = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("name"):
            errors.append(f"{source}: every metric row must have a name")
            continue
        name = str(row["name"])
        if name in indexed:
            errors.append(f"{source}: duplicate metric row for {name}")
        indexed[name] = row
    return indexed, errors


def normalized_paper_ids(value: Any) -> set[str]:
    values = value if isinstance(value, list) else [value]
    return {str(item).strip().lower() for item in values if item}


def validate(
    projects: list[dict[str, Any]],
    julia_payload: dict[str, Any],
    citation_payload: dict[str, Any],
) -> list[str]:
    julia_rows, errors = rows_by_name(julia_payload, "Julia metrics")
    citation_rows, citation_errors = rows_by_name(citation_payload, "citation metrics")
    errors.extend(citation_errors)

    expected_julia = {
        str(project["name"]): str(project["julia_id"])
        for project in projects
        if project.get("name") and project.get("julia_id")
    }
    expected_citations = {
        str(project["name"]): normalized_paper_ids(project["paper_id"])
        for project in projects
        if project.get("name") and project.get("paper_id")
    }

    if set(julia_rows) != set(expected_julia):
        missing = sorted(set(expected_julia) - set(julia_rows))
        extra = sorted(set(julia_rows) - set(expected_julia))
        if missing:
            errors.append(f"Julia metrics: missing projects: {', '.join(missing)}")
        if extra:
            errors.append(f"Julia metrics: unexpected projects: {', '.join(extra)}")

    if set(citation_rows) != set(expected_citations):
        missing = sorted(set(expected_citations) - set(citation_rows))
        extra = sorted(set(citation_rows) - set(expected_citations))
        if missing:
            errors.append(f"citation metrics: missing projects: {', '.join(missing)}")
        if extra:
            errors.append(f"citation metrics: unexpected projects: {', '.join(extra)}")

    for name, julia_id in expected_julia.items():
        row = julia_rows.get(name)
        if not row:
            continue
        if str(row.get("julia_id") or "") != julia_id:
            errors.append(
                f"Julia metrics: {name} expected julia_id {julia_id}, "
                f"found {row.get('julia_id')}"
            )
        for error in row.get("errors") or []:
            errors.append(f"Julia metrics: {name}: {error}")

    for name, paper_ids in expected_citations.items():
        row = citation_rows.get(name)
        if not row:
            continue
        collected_ids = normalized_paper_ids(row.get("paper_id") or [])
        if collected_ids != paper_ids:
            errors.append(
                f"citation metrics: {name} identifiers differ "
                f"(expected {sorted(paper_ids)}, found {sorted(collected_ids)})"
            )
        for error in row.get("errors") or []:
            errors.append(f"citation metrics: {name}: {error}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--projects", type=Path, default=Path("projects.yaml"))
    parser.add_argument(
        "--julia-metrics",
        type=Path,
        default=Path("metadata/generated/julia_metrics.json"),
    )
    parser.add_argument(
        "--citation-metrics",
        type=Path,
        default=Path("metadata/generated/citation_metrics.json"),
    )
    args = parser.parse_args()

    try:
        projects = load_projects(args.projects)
        julia_payload = load_json(args.julia_metrics)
        citation_payload = load_json(args.citation_metrics)
        errors = validate(projects, julia_payload, citation_payload)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(
        "Validated collected metrics "
        f"({len(julia_payload['projects'])} Julia projects, "
        f"{len(citation_payload['projects'])} citation projects)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
