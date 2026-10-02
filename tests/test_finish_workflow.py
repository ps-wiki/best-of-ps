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

    def test_automatic_finalization_retries_after_three_hour_delay(self):
        for schedule in (
            'cron: "17 21 * * 4"',
            'cron: "17 22 * * 4"',
            'cron: "17 23 * * 4"',
            'cron: "17 0 * * 5"',
            'cron: "17 1 * * 5"',
        ):
            self.assertIn(schedule, WORKFLOW)
        self.assertIn('cron: "17 18 * * 4"', UPDATE_WORKFLOW)
        self.assertNotIn('cron: "0 18 * * 4"', UPDATE_WORKFLOW)

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

    def test_updater_normalizes_and_validates_before_publishing(self):
        normalization = UPDATE_WORKFLOW.index("- name: normalize generated project count")
        validation = UPDATE_WORKFLOW.index("- name: validate generated weekly update")
        publishing = UPDATE_WORKFLOW.index("- name: push-update")
        section = UPDATE_WORKFLOW[validation:publishing]

        self.assertLess(normalization, validation)
        self.assertLess(validation, publishing)
        self.assertIn("normalize_generated_project_count.py", UPDATE_WORKFLOW[normalization:validation])
        self.assertIn("scripts/validate_generated_update.py", section)
        self.assertIn("--working-tree", section)
        self.assertIn("--allow-upstream-eof-blank-line", section)

    def test_scheduled_finalization_discovers_current_update(self):
        schedule = WORKFLOW.index('cron: "17 21 * * 4"')
        section = WORKFLOW[schedule:]

        self.assertIn('today="$(date -u \'+%Y.%m.%d\')"', section)
        self.assertIn('yesterday="$(date -u -d \'1 day ago\' \'+%Y.%m.%d\')"', section)
        self.assertIn('two_days_ago="$(date -u -d \'2 days ago\' \'+%Y.%m.%d\')"', section)
        self.assertIn("gh pr list", section)
        self.assertIn("headRefOid", section)
        self.assertIn('select(.headRefName == ("update/" + .version))', section)
        self.assertIn("No recent open or merged update PR found", section)
        self.assertIn('finalize_mode="complete"', section)
        self.assertIn('finalize_mode="already-merged"', section)
        self.assertIn("Confirm already finalized update", section)
        self.assertIn("exit 1", section)


if __name__ == "__main__":
    unittest.main()
