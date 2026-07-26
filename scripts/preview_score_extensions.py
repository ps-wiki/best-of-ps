#!/usr/bin/env python3
"""Preview local score adjustments from Julia and citation metadata."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from typing import Any

from score_adjustments import index_by_name, load_json, score_breakdown


def latest_history_csv(history_dir: Path = Path("history")) -> Path:
    candidates = sorted(history_dir.glob("*_projects.csv"))
    if not candidates:
        raise ValueError(f"no *_projects.csv files found under {history_dir}")
    return candidates[-1]


def load_history(path: Path) -> dict[str, dict[str, str]]:
    with path.open(newline="") as file:
        reader = csv.DictReader(file)
        return {row["name"]: row for row in reader if row.get("name")}


def preview(
    history: dict[str, dict[str, str]],
    julia_metrics: dict[str, dict[str, Any]],
    citation_metrics: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    names = sorted(set(julia_metrics) | set(citation_metrics))
    for name in names:
        history_row = history.get(name, {})
        base_score = float(
            history_row.get("upstream_projectrank")
            or history_row.get("projectrank")
            or 0.0
        )

        julia = julia_metrics.get(name, {})
        citation = citation_metrics.get(name, {})
        breakdown = score_breakdown(julia, citation)
        rows.append(
            {
                "name": name,
                "base_projectrank": round(base_score, 3),
                "julia_adjustment": breakdown["julia_adjustment"],
                "citation_adjustment": breakdown["citation_adjustment"],
                "applied_adjustment": breakdown["applied_adjustment"],
                "bestps_projectrank": int(base_score)
                + int(breakdown["applied_adjustment"]),
            }
        )
    rows.sort(key=lambda row: row["bestps_projectrank"], reverse=True)
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--history", type=Path)
    parser.add_argument("--julia-metrics", type=Path)
    parser.add_argument("--citation-metrics", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        history_path = args.history or latest_history_csv()
        history = load_history(history_path)
        julia_metrics = index_by_name(load_json(args.julia_metrics))
        citation_metrics = index_by_name(load_json(args.citation_metrics))
        rows = preview(history, julia_metrics, citation_metrics)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    fieldnames = [
        "name",
        "base_projectrank",
        "julia_adjustment",
        "citation_adjustment",
        "applied_adjustment",
        "bestps_projectrank",
    ]
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
    else:
        writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
