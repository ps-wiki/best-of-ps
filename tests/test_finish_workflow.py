import unittest
from pathlib import Path


WORKFLOW = (
    Path(__file__).resolve().parents[1]
    / ".github"
    / "workflows"
    / "finish-best-of-update.yml"
).read_text()
UPDATE_WORKFLOW = (
    Path(__file__).resolve().parents[1]
    / ".github"
    / "workflows"
    / "update-best-of-list.yml"
).read_text()


class FinishWorkflowTests(unittest.TestCase):
    def test_reviewed_checkout_precedes_trusted_checkout(self):
        reviewed = WORKFLOW.index("- name: Checkout reviewed repository")
        trusted = WORKFLOW.index("- name: Checkout trusted workflow repository")

        self.assertLess(reviewed, trusted)
        self.assertIn("path: trusted", WORKFLOW[trusted:])

    def test_automatic_finalization_runs_seven_hours_after_update(self):
        self.assertIn('cron: "0 1 * * 5"', WORKFLOW)
        self.assertIn('cron: "0 18 * * 4"', UPDATE_WORKFLOW)

    def test_automatic_finalization_does_not_hold_runner(self):
        self.assertNotIn("workflow_run", WORKFLOW)
        self.assertNotIn("Wait for two-hour review window", WORKFLOW)
        self.assertNotIn('sleep "$remaining"', WORKFLOW)
        self.assertNotIn("SKIP_FINISH", WORKFLOW)

    def test_workflows_pin_ubuntu_runner_image(self):
        self.assertIn("runs-on: ubuntu-24.04", WORKFLOW)
        self.assertIn("runs-on: ubuntu-24.04", UPDATE_WORKFLOW)
        self.assertNotIn("runs-on: ubuntu-latest", WORKFLOW)
        self.assertNotIn("runs-on: ubuntu-latest", UPDATE_WORKFLOW)

    def test_scheduled_finalization_discovers_current_update(self):
        schedule = WORKFLOW.index('cron: "0 1 * * 5"')
        section = WORKFLOW[schedule:]

        self.assertIn('today="$(date -u \'+%Y.%m.%d\')"', section)
        self.assertIn('yesterday="$(date -u -d \'1 day ago\' \'+%Y.%m.%d\')"', section)
        self.assertIn('two_days_ago="$(date -u -d \'2 days ago\' \'+%Y.%m.%d\')"', section)
        self.assertIn("gh pr list", section)
        self.assertIn("headRefOid", section)
        self.assertIn('select(.headRefName == ("update/" + .version))', section)
        self.assertIn("No recent open update PR found", section)
        self.assertIn("exit 1", section)


if __name__ == "__main__":
    unittest.main()
