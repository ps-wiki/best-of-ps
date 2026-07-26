#!/usr/bin/env python3
"""Verify that generated history contains the expected score adjustments."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from typing import Any

from score_adjustments import index_by_name, load_json, score_breakdown


REQUIRED_COLUMNS = {
    "upstream_projectrank",
    "julia_adjustment",
    "citation_adjustment",
    "bestps_adjustment",
    "projectrank",
}


def latest_history_csv(history_dir: Path) -> Path:
    candidates = sorted(history_dir.glob("*_projects.csv"))
    if not candidates:
        raise ValueError(f"no *_projects.csv files found under {history_dir}")
    return candidates[-1]


def load_history(path: Path) -> tuple[list[dict[str, str]], set[str]]:
    with path.open(newline="") as file:
        reader = csv.DictReader(file)
        return list(reader), set(reader.fieldnames or [])


def is_true(value: Any) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes"}


def validate(
    rows: list[dict[str, str]],
    columns: set[str],
    julia_metrics: dict[str, dict[str, Any]],
    citation_metrics: dict[str, dict[str, Any]],
) -> list[str]:
    errors: list[str] = []
    missing_columns = sorted(REQUIRED_COLUMNS - columns)
    if missing_columns:
        return [
            "generated history is missing score-extension columns: "
            + ", ".join(missing_columns)
        ]

    seen_names: set[str] = set()
    for row in rows:
        name = row.get("name") or ""
        if not name:
            errors.append("generated history contains a row without a name")
            continue
        if name in seen_names:
            errors.append(f"generated history duplicates {name}")
        seen_names.add(name)

        if is_true(row.get("resource")):
            continue

        breakdown = score_breakdown(
            julia_metrics.get(name),
            citation_metrics.get(name),
        )
        try:
            upstream = int(float(row["upstream_projectrank"]))
            projectrank = int(float(row["projectrank"]))
            julia_adjustment = float(row["julia_adjustment"])
            citation_adjustment = float(row["citation_adjustment"])
            applied_adjustment = int(float(row["bestps_adjustment"]))
        except (KeyError, TypeError, ValueError):
            errors.append(f"{name}: generated score-extension values are invalid")
            continue

        expected_applied = int(breakdown["applied_adjustment"])
        if applied_adjustment != expected_applied:
            errors.append(
                f"{name}: expected applied adjustment {expected_applied}, "
                f"found {applied_adjustment}"
            )
        if abs(julia_adjustment - float(breakdown["julia_adjustment"])) > 0.001:
            errors.append(f"{name}: Julia adjustment differs from collected metrics")
        if abs(citation_adjustment - float(breakdown["citation_adjustment"])) > 0.001:
            errors.append(f"{name}: citation adjustment differs from collected metrics")
        if projectrank != upstream + expected_applied:
            errors.append(
                f"{name}: projectrank {projectrank} does not equal upstream "
                f"{upstream} plus adjustment {expected_applied}"
            )

    expected_names = set(julia_metrics) | set(citation_metrics)
    missing_projects = sorted(expected_names - seen_names)
    if missing_projects:
        errors.append(
            "generated history is missing applicable projects: "
            + ", ".join(missing_projects)
        )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--history", type=Path)
    parser.add_argument("--history-dir", type=Path, default=Path("history"))
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
        history_path = args.history or latest_history_csv(args.history_dir)
        rows, columns = load_history(history_path)
        julia_metrics = index_by_name(load_json(args.julia_metrics))
        citation_metrics = index_by_name(load_json(args.citation_metrics))
        errors = validate(
            rows,
            columns,
            julia_metrics,
            citation_metrics,
        )
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    adjusted = sum(
        1
        for row in rows
        if not is_true(row.get("resource"))
        and int(float(row.get("bestps_adjustment") or 0)) > 0
    )
    print(
        f"Validated applied scores in {history_path} "
        f"({adjusted} adjusted projects)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
