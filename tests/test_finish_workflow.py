import unittest
from pathlib import Path


WORKFLOW = (
    Path(__file__).resolve().parents[1]
    / ".github"
    / "workflows"
    / "finish-best-of-update.yml"
).read_text()


class FinishWorkflowTests(unittest.TestCase):
    def test_reviewed_checkout_precedes_trusted_checkout(self):
        reviewed = WORKFLOW.index("- name: Checkout reviewed repository")
        trusted = WORKFLOW.index("- name: Checkout trusted workflow repository")

        self.assertLess(reviewed, trusted)
        self.assertIn("path: trusted", WORKFLOW[trusted:])


if __name__ == "__main__":
    unittest.main()
