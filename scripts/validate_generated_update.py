#!/usr/bin/env python3
"""Validate the generated files in a best-of weekly update."""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path


HISTORY_RE = re.compile(r"^history/(\d{4}-\d{2}-\d{2})_(changes|projects)\.(md|csv)$")
ALLOWED_STATIC_FILES = {"README.md", "latest-changes.md"}
CONFLICT_RE = re.compile(r"^(<<<<<<<|=======|>>>>>>>)")
REQUIRED_HISTORY_COLUMNS = {"name", "resource", "projectrank"}


def git_output(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def changed_files(base_ref: str) -> list[str]:
    return [
        path
        for path in git_output("diff", "--name-only", f"{base_ref}...HEAD").splitlines()
        if path
    ]


def validate_changed_files(files: list[str]) -> list[str]:
    errors: list[str] = []
    history_files: dict[str, set[str]] = {}

    for path in files:
        if path in ALLOWED_STATIC_FILES:
            continue
        match = HISTORY_RE.fullmatch(path)
        if not match:
            errors.append(f"unexpected changed file: {path}")
            continue
        date, kind, extension = match.groups()
        history_files.setdefault(date, set()).add(f"{kind}.{extension}")

    if "README.md" not in files:
        errors.append("generated update must modify README.md")
    if "latest-changes.md" not in files:
        errors.append("generated update must modify latest-changes.md")

    if len(history_files) != 1:
        errors.append(
            "generated update must contain exactly one history date, "
            f"found {sorted(history_files) or 'none'}"
        )
    else:
        date, generated = next(iter(history_files.items()))
        expected = {"changes.md", "projects.csv"}
        if generated != expected:
            errors.append(
                f"history/{date} must contain exactly changes.md and projects.csv, "
                f"found {sorted(generated)}"
            )

    return errors


def validate_text_files(files: list[str]) -> list[str]:
    errors: list[str] = []
    for path_string in files:
        path = Path(path_string)
        if not path.is_file():
            errors.append(f"changed file is missing at HEAD: {path_string}")
            continue
        text = path.read_text(encoding="utf-8")
        conflict_lines = [
            f"{index}: {line}"
            for index, line in enumerate(text.splitlines(), start=1)
            if CONFLICT_RE.match(line)
        ]
        if conflict_lines:
            errors.append(f"{path_string} contains merge-conflict markers: {conflict_lines[0]}")

    readme = Path("README.md").read_text(encoding="utf-8")
    if "Popular Open Source Libraries for Power System Analysis" not in readme:
        errors.append("README.md is missing the generated project title")
    if "## Contents" not in readme or "## Explanation" not in readme:
        errors.append("README.md is missing generated Contents or Explanation sections")

    latest_changes = Path("latest-changes.md").read_text(encoding="utf-8")
    if not re.search(r"^##\s+", latest_changes, re.MULTILINE):
        errors.append("latest-changes.md has no Markdown section headings")

    return errors


def validate_history_csv(files: list[str]) -> list[str]:
    errors: list[str] = []
    history_csvs = [path for path in files if HISTORY_RE.fullmatch(path) and path.endswith("_projects.csv")]
    if len(history_csvs) != 1:
        return errors

    path = Path(history_csvs[0])
    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        columns = set(reader.fieldnames or [])
        missing_columns = sorted(REQUIRED_HISTORY_COLUMNS - columns)
        if missing_columns:
            return [
                f"{path} is missing required columns: {', '.join(missing_columns)}"
            ]

        rows = list(reader)

    if not rows:
        errors.append(f"{path} contains no project rows")
        return errors

    seen_names: set[str] = set()
    for index, row in enumerate(rows, start=2):
        name = (row.get("name") or "").strip()
        if not name:
            errors.append(f"{path}:{index} has no project name")
        elif name in seen_names:
            errors.append(f"{path}:{index} duplicates project {name}")
        seen_names.add(name)

        resource = (row.get("resource") or "").strip().lower() in {"1", "true", "yes"}
        if not resource:
            projectrank = (row.get("projectrank") or "").strip()
            try:
                float(projectrank)
            except ValueError:
                errors.append(f"{path}:{index} has an invalid projectrank: {projectrank!r}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-ref", default="origin/main")
    args = parser.parse_args()

    try:
        files = changed_files(args.base_ref)
        errors = [] if files else ["generated update has no changed files"]
        errors.extend(validate_changed_files(files))
        errors.extend(validate_text_files(files))
        errors.extend(validate_history_csv(files))

        diff_check = subprocess.run(
            ["git", "diff", "--check", f"{args.base_ref}...HEAD"],
            capture_output=True,
            text=True,
        )
        if diff_check.returncode:
            errors.append("git diff --check failed:\n" + diff_check.stdout + diff_check.stderr)
    except (OSError, subprocess.CalledProcessError, UnicodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"Validated generated weekly update ({len(files)} changed files).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
