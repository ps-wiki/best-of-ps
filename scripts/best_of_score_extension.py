#!/usr/bin/env python3
"""Inject best-of-ps metadata adjustments into best-of-generator scoring."""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from score_adjustments import index_by_name, load_json, score_breakdown  # noqa: E402


JULIA_METRICS = Path(
    os.environ.get(
        "BESTPS_JULIA_METRICS",
        "metadata/generated/julia_metrics.json",
    )
)
CITATION_METRICS = Path(
    os.environ.get(
        "BESTPS_CITATION_METRICS",
        "metadata/generated/citation_metrics.json",
    )
)


def install() -> None:
    from best_of import projects_collection

    if getattr(projects_collection, "_bestps_score_extension_installed", False):
        return

    julia_metrics = index_by_name(load_json(JULIA_METRICS))
    citation_metrics = index_by_name(load_json(CITATION_METRICS))
    original_apply_filters = projects_collection.apply_filters
    adjusted_objects: set[int] = set()

    def apply_filters(project_info: Any, configuration: Any) -> None:
        object_id = id(project_info)
        if object_id not in adjusted_objects and not project_info.get("resource"):
            name = str(project_info.get("name") or "")
            breakdown = score_breakdown(
                julia_metrics.get(name),
                citation_metrics.get(name),
            )
            upstream_projectrank = int(project_info.get("projectrank") or 0)
            project_info["upstream_projectrank"] = upstream_projectrank
            project_info["julia_adjustment"] = breakdown["julia_adjustment"]
            project_info["citation_adjustment"] = breakdown["citation_adjustment"]
            project_info["bestps_adjustment"] = breakdown["applied_adjustment"]
            project_info["projectrank"] = (
                upstream_projectrank + breakdown["applied_adjustment"]
            )
            adjusted_objects.add(object_id)
        original_apply_filters(project_info, configuration)

    projects_collection.apply_filters = apply_filters
    projects_collection._bestps_score_extension_installed = True
    print(
        "Installed best-of-ps score extension "
        f"({len(julia_metrics)} Julia projects, "
        f"{len(citation_metrics)} citation projects)."
    )


install()
