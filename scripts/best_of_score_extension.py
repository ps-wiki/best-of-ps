#!/usr/bin/env python3
"""Inject best-of-ps metadata adjustments into best-of-generator scoring."""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any
from urllib.parse import quote


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


class JuliaPackageIntegration:
    name = "julia"

    def __init__(self, metrics: dict[str, dict[str, Any]]) -> None:
        self.metrics = metrics

    def update_project_info(self, project_info: Any) -> None:
        julia_id = project_info.get("julia_id")
        if not julia_id:
            return
        project_info["julia_url"] = "https://juliahub.com/ui/Packages/General/" + quote(
            str(julia_id), safe=""
        )
        metric = self.metrics.get(str(project_info.get("name") or ""), {})
        project_info["julia_monthly_downloads"] = metric.get("monthly_user_downloads")
        project_info["julia_total_downloads"] = metric.get("total_user_downloads")

    def generate_md_details(self, project: Any, configuration: Any) -> str:
        julia_id = project.get("julia_id")
        if not julia_id:
            return ""

        from best_of import utils

        url = project.get("julia_url") or (
            "https://juliahub.com/ui/Packages/General/" + quote(str(julia_id), safe="")
        )
        metrics = ""
        if project.get("julia_monthly_downloads"):
            metrics = (
                " (📥 "
                + str(utils.simplify_number(project["julia_monthly_downloads"]))
                + " / month)"
            )
        separator = ":" if configuration.generate_install_hints else ""
        details = f"- [Julia]({url}){metrics}{separator}\n"
        if configuration.generate_install_hints:
            details += '\t```\n\timport Pkg; Pkg.add("{julia_id}")\n\t```\n'
        return details.format(julia_id=julia_id)


class PaperIntegration:
    name = "paper"

    def __init__(self, metrics: dict[str, dict[str, Any]]) -> None:
        self.metrics = metrics

    def update_project_info(self, project_info: Any) -> None:
        if not project_info.get("paper_id"):
            return
        metric = self.metrics.get(str(project_info.get("name") or ""), {})
        project_info["paper_cited_by_count"] = metric.get("cited_by_count")

    @staticmethod
    def paper_link(identifier: str) -> str:
        if identifier.lower().startswith("arxiv:"):
            arxiv_id = identifier.split(":", 1)[1]
            url = "https://arxiv.org/abs/" + quote(arxiv_id, safe=".")
        else:
            url = "https://doi.org/" + quote(identifier, safe="/:")
        return f"[{identifier}]({url})"

    def generate_md_details(self, project: Any, configuration: Any) -> str:
        paper_id = project.get("paper_id")
        if not paper_id:
            return ""
        identifiers = paper_id if isinstance(paper_id, list) else [paper_id]
        links = ", ".join(
            self.paper_link(str(identifier)) for identifier in identifiers
        )
        metrics = ""
        cited_by_count = project.get("paper_cited_by_count")
        if cited_by_count:
            suffix = "citation" if int(cited_by_count) == 1 else "citations"
            metrics = f" (📚 {int(cited_by_count)} {suffix})"
        label = "Paper" if len(identifiers) == 1 else "Papers"
        return f"- {label}{metrics}: {links}\n"


def install() -> None:
    from best_of import integrations, projects_collection

    if getattr(projects_collection, "_bestps_score_extension_installed", False):
        return

    julia_metrics = index_by_name(load_json(JULIA_METRICS))
    citation_metrics = index_by_name(load_json(CITATION_METRICS))
    installed_integrations = {
        integration.name for integration in integrations.AVAILABLE_PACKAGE_MANAGER
    }
    if "julia" not in installed_integrations:
        integrations.AVAILABLE_PACKAGE_MANAGER.append(
            JuliaPackageIntegration(julia_metrics)
        )
    if "paper" not in installed_integrations:
        integrations.AVAILABLE_PACKAGE_MANAGER.append(
            PaperIntegration(citation_metrics)
        )
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
        f"{len(citation_metrics)} citation projects) "
        "with Julia and paper links."
    )


install()
