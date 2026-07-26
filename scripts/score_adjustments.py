#!/usr/bin/env python3
"""Shared scoring rules for Julia-package and paper-citation metadata."""

from __future__ import annotations

import json
import math
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


def index_by_name(payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    projects = payload.get("projects")
    if not isinstance(projects, list):
        return {}
    return {
        str(project["name"]): project
        for project in projects
        if isinstance(project, dict) and project.get("name")
    }


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
    return sum(
        int(row.get("cited_by_count") or 0)
        for row in rows[:years]
        if isinstance(row.get("cited_by_count"), int)
    )


def project_recent_citations(citation: dict[str, Any]) -> int:
    papers = citation.get("papers")
    if isinstance(papers, list):
        return sum(
            recent_citations(paper.get("counts_by_year"))
            for paper in papers
            if isinstance(paper, dict) and not paper.get("errors")
        )
    return recent_citations(citation.get("counts_by_year"))


def score_breakdown(
    julia: dict[str, Any] | None,
    citation: dict[str, Any] | None,
) -> dict[str, float | int]:
    julia = julia or {}
    citation = citation or {}

    julia_bonus = (
        JULIA_REGISTRATION_BONUS
        if julia.get("julia_id") and not julia.get("errors")
        else 0.0
    )
    julia_download_score = positive_log_score(
        julia.get("monthly_user_downloads"),
        divisor=2.0,
        offset=1.0,
        cap=JULIA_MONTHLY_DOWNLOAD_CAP,
    )

    paper_count = int(citation.get("paper_count") or 0)
    citation_bonus = (
        PAPER_RECORD_BONUS if paper_count > 0 and not citation.get("errors") else 0.0
    )
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

    julia_adjustment = julia_bonus + julia_download_score
    citation_adjustment = citation_bonus + citation_count_score + citation_recent_score
    raw_adjustment = julia_adjustment + citation_adjustment
    return {
        "julia_adjustment": round(julia_adjustment, 3),
        "citation_adjustment": round(citation_adjustment, 3),
        "raw_adjustment": round(raw_adjustment, 3),
        "applied_adjustment": round(raw_adjustment),
    }
