import unittest

from scripts.normalize_generated_project_count import normalize_project_count


README = """<img src=\"https://img.shields.io/badge/projects-170-blue.svg?color=5ac4bf\">\n
This curated list contains 170 open-source projects with a total of 58K stars grouped into 16 categories.\n
## Contents\n
- [Power-System Data](#power-system-data) _171 projects_\n"""


class NormalizeGeneratedProjectCountTests(unittest.TestCase):
    def test_normalizes_matching_stale_summary_and_badge(self):
        normalized, changed = normalize_project_count(README, 171)

        self.assertTrue(changed)
        self.assertIn("projects-171-blue.svg", normalized)
        self.assertIn("contains 171 open-source projects", normalized)

    def test_leaves_already_matching_count_unchanged(self):
        matching = README.replace("170", "171")
        normalized, changed = normalize_project_count(matching, 171)

        self.assertFalse(changed)
        self.assertEqual(normalized, matching)

    def test_refuses_when_category_totals_disagree(self):
        with self.assertRaisesRegex(ValueError, "category totals"):
            normalize_project_count(README, 172)

    def test_refuses_when_summary_and_badge_disagree(self):
        with self.assertRaisesRegex(ValueError, "disagree"):
            normalize_project_count(README.replace("projects-170", "projects-169"), 171)


if __name__ == "__main__":
    unittest.main()
