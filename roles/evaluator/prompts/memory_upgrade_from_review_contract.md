# Evaluator importance-gated memory-upgrade contract

Return **only** one valid JSON object and nothing else.

## Goal

Propose at most:
- one **daily memory** upgrade candidate
- one **durable memory** upgrade candidate

based on a reviewed evaluator case review, its extracted signal packet, current evaluator memory files, and recurrence statistics.

## JSON schema

```json
{
  "daily_candidate": {
    "summary": "string",
    "duplicate_guard": "string",
    "tags": ["string"],
    "why": "string",
    "anchor_signal_kind": "string",
    "anchor_signal_key": "string"
  },
  "durable_candidate": {
    "summary": "string",
    "duplicate_guard": "string",
    "tags": ["string"],
    "why": "string",
    "anchor_signal_kind": "string",
    "anchor_signal_key": "string"
  }
}
```

You may return `null` for either candidate.

The system computes the actual importance score deterministically; do **not** provide an `importance` field.

## Important doctrine

- Prefer **no memory upgrade** over a weak or noisy one.
- Daily memory can capture a high-value single-case lesson.
- Durable memory should only be proposed for:
  - recurring patterns,
  - evaluator operating rules,
  - or broadly reusable high-value lessons.
- Do not propose durable memory for a one-off anecdote.
- Do not restate facts already clearly present in current memory unless the new wording is materially better.
- Make summaries compact, operational, and reusable.
- Preserve uncertainty when recurrence is weak.

## Quality bar

Good memory upgrades are:
- specific
- reusable
- behavior-changing
- not tied to one transient detail unless that detail points to a wider rule

Bad memory upgrades are:
- generic retrospectives
- restating the obvious
- duplicating current memory
- speculative causal stories without support
