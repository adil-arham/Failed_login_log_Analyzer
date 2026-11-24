import os
import tempfile
import unittest

from log_analyzer import THRESHOLD, count_failures, find_flagged_users, load_entries


class TestLogAnalyzer(unittest.TestCase):
    def test_count_failures_ignores_success(self):
        entries = [("bob", "FAILED"), ("bob", "SUCCESS"), ("amy", "FAILED")]
        self.assertEqual(count_failures(entries), {"bob": 1, "amy": 1})

    def test_threshold_is_three(self):
        self.assertEqual(THRESHOLD, 3)

    def test_three_failures_are_flagged(self):
        self.assertEqual(find_flagged_users({"bob": 3}), ["bob"])

    def test_two_failures_are_not_flagged(self):
        self.assertEqual(find_flagged_users({"dave": 2}), [])

    def test_load_entries_skips_bad_lines(self):
        text = "2026-11-20 08:00:00 amy FAILED\n\nthis is junk\n"
        with tempfile.NamedTemporaryFile("w", suffix=".log", delete=False) as f:
            f.write(text)
        try:
            entries, skipped = load_entries(f.name)
        finally:
            os.remove(f.name)
        self.assertEqual(entries, [("amy", "FAILED")])
        self.assertEqual(skipped, 2)


if __name__ == "__main__":
    unittest.main()
