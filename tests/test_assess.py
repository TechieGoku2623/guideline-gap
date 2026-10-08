"""A note that names neither the action nor a refusal is unreadable, not a gap."""

from __future__ import annotations

import unittest

from guideline_gap import GapError, assess, summarize


class AssessTests(unittest.TestCase):
    def test_chart_span_is_concordant(self) -> None:
        row = assess("Order HbA1c.", "HbA1c 7.4% drawn yesterday.", "HbA1c")
        self.assertEqual(row["label"], "concordant")
        self.assertEqual(row["span"], "HbA1c")

    def test_documented_refusal_is_concordant(self) -> None:
        row = assess("Order HbA1c.", "Patient declined the draw.", "HbA1c")
        self.assertEqual(row["label"], "concordant")
        self.assertEqual(row["reason"], "documented_exception")

    def test_empty_chart_is_a_gap(self) -> None:
        row = assess("Order HbA1c.", "", "HbA1c")
        self.assertEqual(row["label"], "gap")
        self.assertIsNone(row["span"])

    def test_unrelated_note_abstains_and_is_excluded_from_the_rate(self) -> None:
        vague = assess("Order HbA1c.", "Patient seen and counseled today.", "HbA1c")
        self.assertEqual(vague["label"], "unreadable")
        totals = summarize(
            [
                assess("Order HbA1c.", "HbA1c 7.4%.", "HbA1c"),
                assess("Order HbA1c.", "", "HbA1c"),
                vague,
            ]
        )
        self.assertEqual(totals["unreadable"], 1)
        self.assertEqual(totals["gap_rate_excluding_abstentions"], 0.5)

    def test_blank_recommendation_raises(self) -> None:
        with self.assertRaises(GapError):
            assess("  ", "HbA1c", "HbA1c")


if __name__ == "__main__":
    unittest.main()
