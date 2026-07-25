#!/usr/bin/env python3
"""Preview local score adjustments from Julia and citation metadata."""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from pathlib import Path
from typing import Any


JULIA_REGISTRATION_BONUS = 1.0
JULIA_MONTHLY_DOWNLOAD_CAP = 6.0
PAPER_RECORD_BONUS = 1.0
CITATION_COUNT_CAP = 6.0
CITATION_RECENT_CAP = 3.0


def load_json(path: Path | None) -> dict[str, Any]:
    if path is None:
        return {"projects": []}
    data = json.loads(path.read_text())
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def load_history(path: Path) -> dict[str, dict[str, str]]:
    with path.open(newline="") as file:
        reader = csv.DictReader(file)
        return {row["name"]: row for row in reader if row.get("name")}


def latest_history_csv(history_dir: Path = Path("history")) -> Path:
    candidates = sorted(history_dir.glob("*_projects.csv"))
    if not candidates:
        raise ValueError(f"no *_projects.csv files found under {history_dir}")
    return candidates[-1]


def positive_log_score(count: Any, divisor: float, offset: float, cap: float) -> float:
    if count in (None, ""):
        return 0.0
    value = float(count)
    if value <= 0:
        return 0.0
    return min(cap, max(0.0, math.log(value / divisor) - offset))


def recent_citations(counts_by_year: Any, years: int = 2) -> int:
    if not isinstance(counts_by_year, list):
        return 0
    rows = [row for row in counts_by_year if isinstance(row, dict)]
    rows.sort(key=lambda row: int(row.get("year") or 0), reverse=True)
    total = 0
    for row in rows[:years]:
        count = row.get("cited_by_count")
        if isinstance(count, int):
            total += count
    return total


def project_recent_citations(citation: dict[str, Any]) -> int:
    papers = citation.get("papers")
    if isinstance(papers, list):
        return sum(
            recent_citations(paper.get("counts_by_year"))
            for paper in papers
            if isinstance(paper, dict) and not paper.get("errors")
        )
    return recent_citations(citation.get("counts_by_year"))


def index_by_name(payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    projects = payload.get("projects")
    if not isinstance(projects, list):
        return {}
    return {
        str(project["name"]): project
        for project in projects
        if isinstance(project, dict) and project.get("name")
    }


def preview(
    history: dict[str, dict[str, str]],
    julia_metrics: dict[str, dict[str, Any]],
    citation_metrics: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    names = sorted(set(julia_metrics) | set(citation_metrics))
    for name in names:
        history_row = history.get(name, {})
        base_score = float(history_row.get("projectrank") or 0.0)

        julia = julia_metrics.get(name, {})
        julia_bonus = JULIA_REGISTRATION_BONUS if julia.get("julia_id") and not julia.get("errors") else 0.0
        julia_download_score = positive_log_score(
            julia.get("monthly_user_downloads"),
            divisor=2.0,
            offset=1.0,
            cap=JULIA_MONTHLY_DOWNLOAD_CAP,
        )

        citation = citation_metrics.get(name, {})
        resolved_paper_count = int(citation.get("resolved_paper_count") or 0)
        arxiv_paper_count = int(citation.get("arxiv_paper_count") or 0)
        if resolved_paper_count == 0 and citation.get("paper_doi") and not citation.get("errors"):
            resolved_paper_count = 1
        citation_bonus = PAPER_RECORD_BONUS if resolved_paper_count > 0 or arxiv_paper_count > 0 else 0.0
        citation_count_score = positive_log_score(
            citation.get("cited_by_count"),
            divisor=2.0,
            offset=1.0,
            cap=CITATION_COUNT_CAP,
        )
        citation_recent_score = positive_log_score(
            project_recent_citations(citation),
            divisor=1.5,
            offset=0.0,
            cap=CITATION_RECENT_CAP,
        )

        adjustment = (
            julia_bonus
            + julia_download_score
            + citation_bonus
            + citation_count_score
            + citation_recent_score
        )
        rows.append(
            {
                "name": name,
                "base_projectrank": round(base_score, 3),
                "julia_adjustment": round(julia_bonus + julia_download_score, 3),
                "citation_adjustment": round(citation_bonus + citation_count_score + citation_recent_score, 3),
                "bestps_projectrank_preview": round(base_score + adjustment, 3),
            }
        )
    rows.sort(key=lambda row: row["bestps_projectrank_preview"], reverse=True)
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
        "bestps_projectrank_preview",
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
