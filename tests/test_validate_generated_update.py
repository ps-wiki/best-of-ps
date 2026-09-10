import unittest

from scripts.validate_generated_update import unexpected_diff_check_lines


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
