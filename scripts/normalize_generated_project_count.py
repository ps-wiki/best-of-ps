#!/usr/bin/env python3
"""Safely repair a stale generated README project count."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path


PROJECT_SUMMARY_RE = re.compile(
    r"This curated list contains (?P<projects>\d+) open-source projects "
    r"with a total of .* grouped into (?P<categories>\d+) categories\."
)
PROJECT_BADGE_RE = re.compile(
    r"https://img\.shields\.io/badge/projects-(?P<projects>\d+)-blue\.svg\?color=5ac4bf"
)
CONTENTS_RE = re.compile(
    r"^- \[[^\]]+\]\([^\n]+\) _(?P<count>\d+) projects_$",
    re.MULTILINE,
)


def latest_history_csv(history_dir: Path) -> Path:
    candidates = sorted(history_dir.glob("*_projects.csv"))
    if not candidates:
        raise ValueError(f"no *_projects.csv files found under {history_dir}")
    return candidates[-1]


def history_project_count(path: Path) -> int:
    with path.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
    if not rows:
        raise ValueError(f"{path} contains no project rows")
    return len(rows)


def normalize_project_count(readme: str, expected_count: int) -> tuple[str, bool]:
    summary_matches = list(PROJECT_SUMMARY_RE.finditer(readme))
    badge_matches = list(PROJECT_BADGE_RE.finditer(readme))
    if len(summary_matches) != 1:
        raise ValueError(
            "README.md must contain exactly one generated project summary, "
            f"found {len(summary_matches)}"
        )
    if len(badge_matches) != 1:
        raise ValueError(
            "README.md must contain exactly one project-count badge, "
            f"found {len(badge_matches)}"
        )

    summary = summary_matches[0]
    badge = badge_matches[0]
    summary_count = int(summary.group("projects"))
    badge_count = int(badge.group("projects"))
    if summary_count != badge_count:
        raise ValueError(
            "README.md project summary and badge disagree: "
            f"{summary_count} versus {badge_count}"
        )

    contents_counts = [int(match.group("count")) for match in CONTENTS_RE.finditer(readme)]
    if not contents_counts:
        raise ValueError("README.md has no generated category counts")
    if sum(contents_counts) != expected_count:
        raise ValueError(
            "refusing to normalize project count because README category totals "
            f"sum to {sum(contents_counts)}, history CSV contains {expected_count}"
        )

    if summary_count == expected_count:
        return readme, False

    replacements = [
        (summary.start("projects"), summary.end("projects")),
        (badge.start("projects"), badge.end("projects")),
    ]
    normalized = readme
    for start, end in sorted(replacements, reverse=True):
        normalized = normalized[:start] + str(expected_count) + normalized[end:]
    return normalized, True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--readme", type=Path, default=Path("README.md"))
    parser.add_argument("--history", type=Path)
    parser.add_argument("--history-dir", type=Path, default=Path("history"))
    args = parser.parse_args()

    try:
        history_path = args.history or latest_history_csv(args.history_dir)
        expected_count = history_project_count(history_path)
        readme = args.readme.read_text(encoding="utf-8")
        normalized, changed = normalize_project_count(readme, expected_count)
        if changed:
            args.readme.write_text(normalized, encoding="utf-8")
            print(
                f"Normalized README project count to {expected_count} "
                f"using {history_path}."
            )
        else:
            print(f"README project count already matches {history_path}.")
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
