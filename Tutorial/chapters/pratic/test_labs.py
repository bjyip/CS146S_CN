import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from action_items import list_items, preview, save
from agent_lab import run_lab


class AgentLabTests(unittest.TestCase):
    def test_normal_path_checks_numeric_order(self):
        status, trace = run_lab()
        self.assertEqual(status, "verified")
        self.assertEqual(trace, [("read", 1), ("edit", "applied"), ("test", [10, 9, 8, 3])])

    def test_conflict_changes_next_action(self):
        status, trace = run_lab(budget=5, conflict=True)
        self.assertEqual(status, "verified")
        self.assertEqual(trace[:3], [("read", 1), ("edit", "version_conflict"), ("read", 2)])
        self.assertEqual(trace[3:], [("edit", "applied"), ("test", [10, 9, 8, 3])])

    def test_budget_prevents_another_edit(self):
        status, trace = run_lab(budget=3, conflict=True)
        self.assertEqual(status, "budget_exhausted")
        self.assertEqual(trace, [("read", 1), ("edit", "version_conflict"), ("read", 2)])


class ActionItemsTests(unittest.TestCase):
    def test_preview_and_fallback_do_not_create_a_db(self):
        with tempfile.TemporaryDirectory() as workspace:
            db = Path(workspace) / "tasks.sqlite3"
            script = Path(__file__).with_name("action_items.py")
            for flags in ([], ["--simulate-failure"]):
                result = subprocess.run(
                    [sys.executable, "-X", "utf8", str(script), "--db", str(db), "preview", *flags],
                    capture_output=True,
                    check=True,
                    encoding="utf-8",
                )
                self.assertIn("fixture_rule" if flags else "fixture_model", result.stdout)
                self.assertFalse(db.exists())
            self.assertIsNone(preview()["error"])
            self.assertEqual(preview(True)["error"], "simulated_timeout")

    def test_confirmation_then_reopen_preserves_user_revision(self):
        with tempfile.TemporaryDirectory() as workspace:
            db = Path(workspace) / "tasks.sqlite3"
            with self.assertRaises(ValueError):
                save(db, "明天检查日志")
            with self.assertRaises(ValueError):
                save(db, "   ", confirmed=True)
            self.assertFalse(db.exists())
            item_id = save(db, "明天检查登录日志", confirmed=True)
            self.assertEqual(list_items(db), [{"id": item_id, "text": "明天检查登录日志"}])
