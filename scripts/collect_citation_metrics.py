#!/usr/bin/env python3
"""Collect OpenAlex citation metrics for projects with `paper_doi` or `paper_dois`."""

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


def project_dois(project: dict[str, Any]) -> list[str]:
    dois: list[str] = []
    paper_doi = project.get("paper_doi")
    if paper_doi:
        dois.append(normalize_doi(str(paper_doi)))
    paper_dois = project.get("paper_dois")
    if isinstance(paper_dois, list):
        dois.extend(normalize_doi(str(doi)) for doi in paper_dois if doi)

    seen: set[str] = set()
    unique_dois: list[str] = []
    for doi in dois:
        key = doi.lower()
        if key in seen:
            continue
        seen.add(key)
        unique_dois.append(doi)
    return unique_dois


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
        dois = project_dois(project)
        if not dois:
            continue
        name = str(project.get("name", dois[0]))
        papers: list[dict[str, Any]] = []
        errors: list[str] = []
        for doi in dois:
            paper: dict[str, Any] = {
                "paper_doi": doi,
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
                    paper["errors"].append("openalex: DOI not found")
                else:
                    paper.update(
                        {
                            "openalex_id": data.get("id"),
                            "title": data.get("title") or data.get("display_name"),
                            "publication_year": data.get("publication_year"),
                            "cited_by_count": data.get("cited_by_count"),
                            "counts_by_year": data.get("counts_by_year") or [],
                        }
                    )
            except (HTTPError, URLError, TimeoutError, ValueError) as exc:
                paper["errors"].append(f"openalex: {exc}")
            errors.extend(f"{doi}: {error}" for error in paper["errors"])
            papers.append(paper)
        resolved_papers = [paper for paper in papers if paper.get("openalex_id") and not paper.get("errors")]
        row: dict[str, Any] = {
            "name": name,
            "paper_doi": dois[0],
            "paper_dois": dois,
            "source": "openalex",
            "paper_count": len(papers),
            "resolved_paper_count": len(resolved_papers),
            "cited_by_count": sum(int(paper.get("cited_by_count") or 0) for paper in resolved_papers),
            "papers": papers,
            "errors": errors,
        }
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
            "paper_doi should point to the primary core paper; paper_dois can list additional official core papers.",
            "Project-level cited_by_count sums resolved papers and can double-count citing works across related papers.",
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
