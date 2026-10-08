"""Label one recommendation against one chart: concordant, gap, or unreadable."""

from .engine import GapError, assess, summarize

__all__ = ["GapError", "assess", "summarize"]
