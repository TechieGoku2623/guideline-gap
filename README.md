<div align="center">

# guideline-gap

**The distance between what a guideline says and what the record shows was done.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Status:** problem brief. The question and the measurement are written here. An implementation is not in this repository yet.

</div>

---

## The problem

A guideline can be clear and the practice can still diverge: the recommended first test was not ordered, a contraindicated drug appears anyway, or the note cites a recommendation the chart does not follow. Calling every divergence a care failure is how this measurement gets dishonest. Some gaps are documentation. Some are a justified exception. Some are the gap the guideline was written to close.

If the tool cannot tell those apart, it will publish a compliance score that a clinician cannot use.

## The measurement I would trust

One recommendation, one patient record, one of three labels.

| Label | Meaning |
| --- | --- |
| Concordant | The record shows the recommended action, or a documented reason not to take it |
| Gap | The action is absent and no reason is recorded |
| Unreadable | The note does not support either claim, so the tool abstains |

Every label points at the recommendation sentence and the chart span that justified it. A percentage with no spans is not a gap analysis. An abstention counted as a failure is not a gap analysis.

## What this repository is

That labeling rule, stated before any extractor is trusted with it. The nearest running system in this portfolio is [Sentinel-RAG](https://github.com/TechieGoku2623/Sentinal_RAG), which answers from a protocol and flags a draft it cannot ground. This repository is not a medical device and not an audit of a real health system.

## Author

**Choppa Devasai Pranatheswar** · [LinkedIn](https://www.linkedin.com/in/devasai-pranatheswar)
