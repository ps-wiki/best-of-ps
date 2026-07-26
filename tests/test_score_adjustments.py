import json
import os
import sys
import tempfile
import types
import unittest
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from score_adjustments import positive_log_score, score_breakdown  # noqa: E402
from validate_applied_scores import (  # noqa: E402
    validate as validate_applied_scores,
)
from validate_collected_metrics import validate  # noqa: E402


class ScoreAdjustmentTests(unittest.TestCase):
    def test_empty_metadata_has_no_adjustment(self):
        self.assertEqual(score_breakdown({}, {})["applied_adjustment"], 0)

    def test_adjustment_combines_julia_and_citations(self):
        julia = {
            "julia_id": "Example",
            "monthly_user_downloads": 200,
            "errors": [],
        }
        citation = {
            "paper_count": 1,
            "resolved_paper_count": 1,
            "arxiv_paper_count": 0,
            "cited_by_count": 100,
            "papers": [
                {
                    "counts_by_year": [
                        {"year": 2026, "cited_by_count": 20},
                        {"year": 2025, "cited_by_count": 10},
                    ],
                    "errors": [],
                }
            ],
        }
        breakdown = score_breakdown(julia, citation)
        self.assertGreater(breakdown["julia_adjustment"], 1)
        self.assertGreater(breakdown["citation_adjustment"], 1)
        self.assertEqual(
            breakdown["applied_adjustment"],
            round(breakdown["raw_adjustment"]),
        )

    def test_log_score_is_bounded(self):
        self.assertEqual(positive_log_score(0, 2, 1, 6), 0)
        self.assertEqual(positive_log_score(10**20, 2, 1, 6), 6)

    def test_unresolved_doi_keeps_only_paper_record_bonus(self):
        citation = {
            "paper_count": 1,
            "resolved_paper_count": 0,
            "arxiv_paper_count": 0,
            "cited_by_count": 0,
            "errors": [],
        }
        breakdown = score_breakdown({}, citation)
        self.assertEqual(breakdown["citation_adjustment"], 1)
        self.assertEqual(breakdown["applied_adjustment"], 1)


class CollectedMetricValidationTests(unittest.TestCase):
    def test_complete_metric_payloads_pass(self):
        projects = [
            {"name": "Julia project", "julia_id": "JuliaProject"},
            {
                "name": "Paper project",
                "paper_id": ["10.1000/example", "arXiv:2401.00001"],
            },
        ]
        julia = {
            "projects": [
                {
                    "name": "Julia project",
                    "julia_id": "JuliaProject",
                    "errors": [],
                }
            ]
        }
        citations = {
            "projects": [
                {
                    "name": "Paper project",
                    "paper_id": ["10.1000/example", "arXiv:2401.00001"],
                    "errors": [],
                }
            ]
        }
        self.assertEqual(validate(projects, julia, citations), [])

    def test_provider_errors_fail_validation(self):
        projects = [{"name": "Julia project", "julia_id": "JuliaProject"}]
        julia = {
            "projects": [
                {
                    "name": "Julia project",
                    "julia_id": "JuliaProject",
                    "errors": ["monthly_downloads: timeout"],
                }
            ]
        }
        errors = validate(projects, julia, {"projects": []})
        self.assertTrue(any("timeout" in error for error in errors))


class GeneratorExtensionTests(unittest.TestCase):
    def test_extension_adjusts_before_upstream_filtering_once(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            julia_path = temp / "julia.json"
            citation_path = temp / "citation.json"
            julia_path.write_text(
                json.dumps(
                    {
                        "projects": [
                            {
                                "name": "Example",
                                "julia_id": "Example",
                                "monthly_user_downloads": 200,
                                "errors": [],
                            }
                        ]
                    }
                )
            )
            citation_path.write_text(json.dumps({"projects": []}))

            calls = []
            projects_collection = types.ModuleType("best_of.projects_collection")

            def upstream_apply_filters(project, _configuration):
                calls.append(project["projectrank"])

            projects_collection.apply_filters = upstream_apply_filters
            best_of = types.ModuleType("best_of")
            best_of.projects_collection = projects_collection

            old_best_of = sys.modules.get("best_of")
            old_collection = sys.modules.get("best_of.projects_collection")
            old_julia = os.environ.get("BESTPS_JULIA_METRICS")
            old_citation = os.environ.get("BESTPS_CITATION_METRICS")
            try:
                sys.modules["best_of"] = best_of
                sys.modules["best_of.projects_collection"] = projects_collection
                os.environ["BESTPS_JULIA_METRICS"] = str(julia_path)
                os.environ["BESTPS_CITATION_METRICS"] = str(citation_path)

                spec = spec_from_file_location(
                    "best_of_score_extension_test",
                    SCRIPTS / "best_of_score_extension.py",
                )
                module = module_from_spec(spec)
                assert spec and spec.loader
                spec.loader.exec_module(module)

                project = {
                    "name": "Example",
                    "projectrank": 20,
                    "resource": False,
                }
                expected = score_breakdown(
                    {
                        "julia_id": "Example",
                        "monthly_user_downloads": 200,
                        "errors": [],
                    },
                    {},
                )["applied_adjustment"]
                projects_collection.apply_filters(project, {})
                projects_collection.apply_filters(project, {})

                self.assertEqual(project["upstream_projectrank"], 20)
                self.assertEqual(project["projectrank"], 20 + expected)
                self.assertEqual(calls, [20 + expected, 20 + expected])
            finally:
                if old_best_of is None:
                    sys.modules.pop("best_of", None)
                else:
                    sys.modules["best_of"] = old_best_of
                if old_collection is None:
                    sys.modules.pop("best_of.projects_collection", None)
                else:
                    sys.modules["best_of.projects_collection"] = old_collection
                if old_julia is None:
                    os.environ.pop("BESTPS_JULIA_METRICS", None)
                else:
                    os.environ["BESTPS_JULIA_METRICS"] = old_julia
                if old_citation is None:
                    os.environ.pop("BESTPS_CITATION_METRICS", None)
                else:
                    os.environ["BESTPS_CITATION_METRICS"] = old_citation


class AppliedScoreValidationTests(unittest.TestCase):
    def test_generated_score_columns_match_breakdown(self):
        julia = {
            "Example": {
                "name": "Example",
                "julia_id": "Example",
                "monthly_user_downloads": 200,
                "errors": [],
            }
        }
        breakdown = score_breakdown(julia["Example"], {})
        applied = int(breakdown["applied_adjustment"])
        rows = [
            {
                "name": "Example",
                "resource": "False",
                "upstream_projectrank": "20",
                "julia_adjustment": str(breakdown["julia_adjustment"]),
                "citation_adjustment": "0",
                "bestps_adjustment": str(applied),
                "projectrank": str(20 + applied),
            }
        ]
        columns = set(rows[0])
        self.assertEqual(
            validate_applied_scores(rows, columns, julia, {}),
            [],
        )

    def test_missing_extension_columns_fail(self):
        errors = validate_applied_scores(
            [{"name": "Example"}],
            {"name"},
            {},
            {},
        )
        self.assertTrue(any("missing score-extension columns" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
