"""Unreadable notes are abstentions. They are not counted as gaps."""

from __future__ import annotations

EXCEPTIONS = ("declined", "contraindicated", "not indicated", "patient refused")


class GapError(ValueError):
    """The recommendation or the action term is empty."""


def assess(recommendation: str, chart: str, action: str) -> dict[str, object]:
    recommendation = recommendation.strip()
    action = action.strip()
    if not recommendation or not action:
        raise GapError("recommendation and action are required")
    chart_fold = chart.lower()
    action_fold = action.lower()
    if action_fold in chart_fold:
        return _label("concordant", "action", recommendation, _slice(chart, chart_fold, action_fold))
    for phrase in EXCEPTIONS:
        if phrase in chart_fold:
            return _label(
                "concordant",
                "documented_exception",
                recommendation,
                _slice(chart, chart_fold, phrase),
            )
    if len(chart.strip()) < 12:
        return _label("gap", "absent", recommendation, None)
    return _label("unreadable", "note_does_not_support", recommendation, None)


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    counts = {"concordant": 0, "gap": 0, "unreadable": 0}
    for row in rows:
        label = str(row["label"])
        counts[label] += 1
    decided = counts["concordant"] + counts["gap"]
    rate = None if decided == 0 else round(counts["gap"] / decided, 3)
    return {**counts, "gap_rate_excluding_abstentions": rate}


def format_report(rows: list[dict[str, object]]) -> str:
    totals = summarize(rows)
    lines = ["guideline-gap", ""]
    for row in rows:
        span = row["span"] if row["span"] else "none"
        lines.append(f"{row['label']:12}  {row['recommendation']}")
        lines.append(f"             span: {span}")
    lines.append("")
    lines.append(
        f"concordant {totals['concordant']}   gap {totals['gap']}   unreadable {totals['unreadable']}"
    )
    lines.append(f"gap rate, abstentions excluded: {totals['gap_rate_excluding_abstentions']}")
    lines.append("")
    lines.append("not a care-quality score")
    return "\n".join(lines)


def _label(label: str, reason: str, recommendation: str, span: str | None) -> dict[str, object]:
    return {
        "label": label,
        "reason": reason,
        "recommendation": recommendation,
        "span": span,
    }


def _slice(chart: str, folded: str, needle: str) -> str:
    start = folded.index(needle)
    return chart[start : start + len(needle)]
