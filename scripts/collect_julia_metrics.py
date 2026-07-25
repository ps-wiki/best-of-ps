#!/usr/bin/env python3
"""Collect Julia package-server download metrics for projects with `julia_id`."""

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
        "error: PyYAML is required. Run with `conda run -n bestps python scripts/collect_julia_metrics.py`.",
        file=sys.stderr,
    )
    raise SystemExit(2)


API_BASE = "https://juliapkgstats.com/api/v2"
USER_AGENT = "best-of-ps metadata collector"


def load_projects(path: Path) -> list[dict[str, Any]]:
    data = yaml.safe_load(path.read_text())
    projects = data.get("projects") if isinstance(data, dict) else None
    if not isinstance(projects, list):
        raise ValueError(f"{path} must contain a projects list")
    return [project for project in projects if isinstance(project, dict)]


def fetch_json(url: str, timeout: float) -> dict[str, Any]:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=timeout) as response:
        payload = response.read().decode("utf-8")
    data = json.loads(payload)
    if not isinstance(data, dict):
        raise ValueError(f"expected JSON object from {url}")
    return data


def fetch_metric(package_name: str, endpoint: str, timeout: float) -> int | None:
    url = f"{API_BASE}/{endpoint}/{quote(package_name)}"
    try:
        data = fetch_json(url, timeout)
    except HTTPError as exc:
        if exc.code == 404:
            return None
        raise
    value = data.get("total_requests")
    if isinstance(value, int):
        return value
    if isinstance(value, str) and value.isdigit():
        return int(value)
    return None


def collect(projects: list[dict[str, Any]], timeout: float) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for project in projects:
        julia_id = project.get("julia_id")
        if not julia_id:
            continue
        name = str(project.get("name", julia_id))
        package_name = str(julia_id)
        row: dict[str, Any] = {
            "name": name,
            "julia_id": package_name,
            "source": "juliapkgstats",
            "monthly_user_downloads": None,
            "total_user_downloads": None,
            "errors": [],
        }
        for endpoint, key in (
            ("monthly_downloads", "monthly_user_downloads"),
            ("total_downloads", "total_user_downloads"),
        ):
            try:
                row[key] = fetch_metric(package_name, endpoint, timeout)
            except (HTTPError, URLError, TimeoutError, ValueError) as exc:
                row["errors"].append(f"{endpoint}: {exc}")
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
        "source": "https://juliapkgstats.com/api",
        "metric_notes": [
            "monthly_user_downloads and total_user_downloads are Julia package-server user requests.",
            "They are not total Julia ecosystem downloads because users can bypass public package servers.",
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
