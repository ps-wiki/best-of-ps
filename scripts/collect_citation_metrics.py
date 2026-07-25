#!/usr/bin/env python3
"""Collect OpenAlex citation metrics for projects with `paper_doi`."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

try:
    import yaml
except ImportError:  # pragma: no cover - exercised only when env is missing deps.
    print(
        "error: PyYAML is required. Run with `conda run -n bestps python scripts/collect_citation_metrics.py`.",
        file=sys.stderr,
    )
    raise SystemExit(2)


OPENALEX_WORKS = "https://api.openalex.org/works"
USER_AGENT = "best-of-ps metadata collector"


def load_projects(path: Path) -> list[dict[str, Any]]:
    data = yaml.safe_load(path.read_text())
    projects = data.get("projects") if isinstance(data, dict) else None
    if not isinstance(projects, list):
        raise ValueError(f"{path} must contain a projects list")
    return [project for project in projects if isinstance(project, dict)]


def normalize_doi(doi: str) -> str:
    doi = doi.strip()
    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
        if doi.lower().startswith(prefix):
            return doi[len(prefix) :]
    return doi


def fetch_openalex(doi: str, timeout: float) -> dict[str, Any] | None:
    work_id = f"https://doi.org/{normalize_doi(doi)}"
    url = f"{OPENALEX_WORKS}/{quote(work_id, safe=':/')}?mailto=best-of-ps@example.org"
    try:
        request = Request(url, headers={"User-Agent": USER_AGENT})
        with urlopen(request, timeout=timeout) as response:
            payload = response.read().decode("utf-8")
    except HTTPError as exc:
        if exc.code == 404:
            return None
        raise
    data = json.loads(payload)
    if not isinstance(data, dict):
        raise ValueError(f"expected JSON object from {url}")
    return data


def collect(projects: list[dict[str, Any]], timeout: float) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for project in projects:
        paper_doi = project.get("paper_doi")
        if not paper_doi:
            continue
        name = str(project.get("name", paper_doi))
        doi = normalize_doi(str(paper_doi))
        row: dict[str, Any] = {
            "name": name,
            "paper_doi": doi,
            "source": "openalex",
            "openalex_id": None,
            "title": None,
            "publication_year": None,
            "cited_by_count": None,
            "counts_by_year": [],
            "errors": [],
        }
        try:
            data = fetch_openalex(doi, timeout)
            if data is None:
                row["errors"].append("openalex: DOI not found")
            else:
                row.update(
                    {
                        "openalex_id": data.get("id"),
                        "title": data.get("title") or data.get("display_name"),
                        "publication_year": data.get("publication_year"),
                        "cited_by_count": data.get("cited_by_count"),
                        "counts_by_year": data.get("counts_by_year") or [],
                    }
                )
        except (HTTPError, URLError, TimeoutError, ValueError) as exc:
            row["errors"].append(f"openalex: {exc}")
        rows.append(row)
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--projects", default="projects.yaml", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--timeout", default=20.0, type=float)
    args = parser.parse_args()

    try:
        projects = load_projects(args.projects)
        metrics = collect(projects, args.timeout)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": "https://api.openalex.org/works",
        "metric_notes": [
            "cited_by_count is OpenAlex coverage, not a universal citation count.",
            "paper_doi should point to the core software, method, or philosophy paper recommended by the project.",
        ],
        "projects": metrics,
    }
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
