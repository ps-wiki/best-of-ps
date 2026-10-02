import unittest
from unittest.mock import patch

from scripts.validate_generated_update import (
    changed_files,
    diff_reference,
    unexpected_diff_check_lines,
)


class DiffReferenceTests(unittest.TestCase):
    def test_committed_head_diff_uses_three_dot_range(self):
        self.assertEqual(
            diff_reference("origin/main", working_tree=False), "origin/main...HEAD"
        )

    def test_working_tree_diff_uses_base_revision(self):
        self.assertEqual(diff_reference("origin/main", working_tree=True), "origin/main")

    @patch("scripts.validate_generated_update.git_output")
    def test_working_tree_includes_untracked_files(self, git_output_mock):
        git_output_mock.side_effect = [
            "README.md\nlatest-changes.md\n",
            "history/2026-10-02_changes.md\nhistory/2026-10-02_projects.csv\n",
        ]

        self.assertEqual(
            changed_files("origin/main", working_tree=True),
            [
                "README.md",
                "history/2026-10-02_changes.md",
                "history/2026-10-02_projects.csv",
                "latest-changes.md",
            ],
        )


class DiffCheckCompatibilityTests(unittest.TestCase):
    def test_upstream_eof_blank_line_can_be_allowed(self):
        output = "history/2026-09-10_changes.md:20: new blank line at EOF.\n"

        self.assertEqual(
            unexpected_diff_check_lines(
                output,
                allow_upstream_eof_blank_line=True,
            ),
            [],
        )

    def test_upstream_eof_blank_line_is_rejected_without_flag(self):
        output = "latest-changes.md:20: new blank line at EOF.\n"

        self.assertEqual(
            unexpected_diff_check_lines(
                output,
                allow_upstream_eof_blank_line=False,
            ),
            [output.rstrip()],
        )

    def test_other_diff_check_errors_are_never_allowed(self):
        output = (
            "history/2026-09-10_changes.md:20: new blank line at EOF.\n"
            "README.md:4: trailing whitespace.\n"
        )

        self.assertEqual(
            unexpected_diff_check_lines(
                output,
                allow_upstream_eof_blank_line=True,
            ),
            ["README.md:4: trailing whitespace."],
        )


if __name__ == "__main__":
    unittest.main()
