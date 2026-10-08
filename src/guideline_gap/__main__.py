"""Label three designed charts. One abstains."""

from __future__ import annotations

from .engine import assess, format_report

CASES = [
    (
        "Order HbA1c before intensifying therapy.",
        "HbA1c 7.4% was drawn two days ago.",
        "HbA1c",
    ),
    (
        "Order HbA1c before intensifying therapy.",
        "Seen in clinic.",
        "HbA1c",
    ),
    (
        "Order HbA1c before intensifying therapy.",
        "Patient declined the lab draw after counseling.",
        "HbA1c",
    ),
]


def main() -> int:
    rows = [assess(recommendation, chart, action) for recommendation, chart, action in CASES]
    print(format_report(rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
