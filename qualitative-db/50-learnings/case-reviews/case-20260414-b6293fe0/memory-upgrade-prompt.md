You are proposing importance-gated memory upgrades for Evaluator.

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


## Files to read before answering

- Review note: `/Users/agent2/.openclaw/orchestrator/qualitative-db/50-learnings/case-reviews/case-20260414-b6293fe0/review.md`
- Signal packet: `/Users/agent2/.openclaw/orchestrator/qualitative-db/50-learnings/case-reviews/case-20260414-b6293fe0/signal-packet.json`
- Learning packet: `/Users/agent2/.openclaw/orchestrator/qualitative-db/50-learnings/case-reviews/case-20260414-b6293fe0/learning-packet.json`
- Evaluator durable memory: `/Users/agent2/.openclaw/evaluator/MEMORY.md`
- Evaluator daily memory for today (may not exist yet): `/Users/agent2/.openclaw/evaluator/memory/2026-04-14.md`

## Current review/index status

```json
{
  "review_path": "qualitative-db/50-learnings/case-reviews/case-20260414-b6293fe0/review.md",
  "packet_path": "qualitative-db/50-learnings/case-reviews/case-20260414-b6293fe0/learning-packet.json",
  "case_key": "case-20260414-b6293fe0",
  "case_db_id": "e878f082-b3fa-47f4-91d4-406c79a1e23a",
  "market_id": "4a2bb987-a875-4a0f-b389-5062f570e7ab",
  "contract_id": "yes",
  "status": "draft",
  "category": "polymarket-discovery",
  "platform": "polymarket",
  "resolution_status": "resolved",
  "resolved_value": 1.0,
  "resolved_at": "2026-04-13T21:38:35-04:00",
  "error_pattern": "resolved_case_review_pending",
  "latest_forecast_prob": 0.98,
  "latest_brier_component": 0.0004,
  "retrieval_tags": [
    "evaluator-draft",
    "learning-case-review",
    "platform-polymarket",
    "polymarket",
    "polymarket-discovery",
    "resolved",
    "resolved-case-review-pending"
  ],
  "source_paths": [
    "qualitative-db/40-research/cases/case-20260414-b6293fe0/case.md",
    "qualitative-db/40-research/cases/case-20260414-b6293fe0/decision-maker/artifacts/decision-maker-packet.json",
    "qualitative-db/40-research/cases/case-20260414-b6293fe0/researcher-swarm-current.md",
    "qualitative-db/40-research/cases/case-20260414-b6293fe0/synthesizer-agent/syndicated-finding.runtime.json",
    "qualitative-db/40-research/cases/case-20260414-b6293fe0/timeline.md"
  ],
  "review_frontmatter": {
    "type": "learning_note",
    "learning_type": "case_review",
    "learning_scope": "resolved_case",
    "case_key": "case-20260414-b6293fe0",
    "market_category": "polymarket-discovery",
    "domain": [],
    "subdomain": [],
    "entity": [],
    "topic": [],
    "question": "Will Bitcoin reach $74,000 April 13-19?",
    "date_created": [],
    "resolution_date": "2026-04-13T21:38:35-04:00",
    "evaluation_scope": "resolved_case",
    "evaluation_target": "pipeline_case",
    "outcome_observed": "1.0",
    "decision_taken": "watch_only",
    "error_pattern": "resolved_case_review_pending",
    "intervention_status": "candidate",
    "related_entities": [],
    "related_drivers": [],
    "upstream_inputs": [
      "qualitative-db/40-research/cases/case-20260414-b6293fe0/case.md",
      "qualitative-db/40-research/cases/case-20260414-b6293fe0/decision-maker/artifacts/decision-maker-packet.json",
      "qualitative-db/40-research/cases/case-20260414-b6293fe0/synthesizer-agent/syndicated-finding.runtime.json"
    ],
    "downstream_uses": [],
    "promotion_candidates": [],
    "tags": [
      "learning/case_review",
      "evaluator/draft",
      "platform/polymarket"
    ]
  },
  "sections_present": [
    "Driver and mechanism takeaways",
    "Error-pattern classification",
    "How this should be reused later",
    "Outcome and scoring evidence",
    "Promotion candidates for stable layers",
    "Proposed intervention or hold decision",
    "Source / input / workflow takeaways",
    "What happened in reality",
    "What the pipeline believed or did",
    "What was being evaluated",
    "What was missing",
    "Which inputs were high signal",
    "Which inputs were misleading"
  ]
}
```

## Recurrence statistics for this case's signal keys

```json
[
  {
    "signal_kind": "missed_signal",
    "signal_key": "missing-input-or-check",
    "occurrence_count": 48,
    "case_count": 17
  },
  {
    "signal_kind": "false_signal",
    "signal_key": "base-rate",
    "occurrence_count": 17,
    "case_count": 17
  },
  {
    "signal_kind": "false_signal",
    "signal_key": "catalyst-hunter",
    "occurrence_count": 17,
    "case_count": 17
  },
  {
    "signal_kind": "false_signal",
    "signal_key": "market-implied",
    "occurrence_count": 17,
    "case_count": 17
  },
  {
    "signal_kind": "false_signal",
    "signal_key": "risk-manager",
    "occurrence_count": 17,
    "case_count": 17
  },
  {
    "signal_kind": "false_signal",
    "signal_key": "variant-view",
    "occurrence_count": 17,
    "case_count": 17
  },
  {
    "signal_kind": "source_performance",
    "signal_key": "base-rate",
    "occurrence_count": 17,
    "case_count": 17
  },
  {
    "signal_kind": "source_performance",
    "signal_key": "catalyst-hunter",
    "occurrence_count": 17,
    "case_count": 17
  },
  {
    "signal_kind": "source_performance",
    "signal_key": "market-implied",
    "occurrence_count": 17,
    "case_count": 17
  },
  {
    "signal_kind": "source_performance",
    "signal_key": "risk-manager",
    "occurrence_count": 17,
    "case_count": 17
  },
  {
    "signal_kind": "source_performance",
    "signal_key": "variant-view",
    "occurrence_count": 17,
    "case_count": 17
  },
  {
    "signal_kind": "workflow_performance",
    "signal_key": "resolved-case-review-pending",
    "occurrence_count": 9,
    "case_count": 9
  }
]
```

## Task

Propose at most one daily candidate and at most one durable candidate.
Use the exact `signal_kind` and `signal_key` values from the recurrence statistics when anchoring a candidate.
The system will compute the actual importance score deterministically; focus on whether a candidate should exist at all and how it should be described.
If no candidate clearly clears the bar, return `null` for that slot.
Return only the final JSON object.
