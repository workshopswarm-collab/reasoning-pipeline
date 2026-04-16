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

- Review note: `/Users/agent2/.openclaw/orchestrator/qualitative-db/50-learnings/case-reviews/case-20260414-4e668883/review.md`
- Signal packet: `/Users/agent2/.openclaw/orchestrator/qualitative-db/50-learnings/case-reviews/case-20260414-4e668883/signal-packet.json`
- Learning packet: `/Users/agent2/.openclaw/orchestrator/qualitative-db/50-learnings/case-reviews/case-20260414-4e668883/learning-packet.json`
- Evaluator durable memory: `/Users/agent2/.openclaw/evaluator/MEMORY.md`
- Evaluator daily memory for today (may not exist yet): `/Users/agent2/.openclaw/evaluator/memory/2026-04-14.md`

## Current review/index status

```json
{
  "review_path": "qualitative-db/50-learnings/case-reviews/case-20260414-4e668883/review.md",
  "packet_path": "qualitative-db/50-learnings/case-reviews/case-20260414-4e668883/learning-packet.json",
  "case_key": "case-20260414-4e668883",
  "case_db_id": "77accba2-6323-4628-a697-4654c7173dcf",
  "market_id": "388995c3-1866-46a6-9793-69442db90054",
  "contract_id": "yes",
  "status": "reviewed",
  "category": "polymarket-discovery",
  "platform": "polymarket",
  "resolution_status": "resolved",
  "resolved_value": 1.0,
  "resolved_at": "2026-04-14T13:20:02-04:00",
  "error_pattern": "underconfidence_on_nearby_touch_market",
  "latest_forecast_prob": 0.9825,
  "latest_brier_component": 0.00030625,
  "retrieval_tags": [
    "crypto-ethereum",
    "learning-case-review",
    "platform-polymarket",
    "polymarket",
    "polymarket-discovery",
    "resolved",
    "threshold-touch",
    "underconfidence",
    "underconfidence-on-nearby-touch-market"
  ],
  "source_paths": [
    "qualitative-db/40-research/cases/case-20260414-4e668883/case.md",
    "qualitative-db/40-research/cases/case-20260414-4e668883/decision-maker/artifacts/decision-maker-packet.json",
    "qualitative-db/40-research/cases/case-20260414-4e668883/researcher-swarm-current.md",
    "qualitative-db/40-research/cases/case-20260414-4e668883/synthesizer-agent/syndicated-finding.runtime.json",
    "qualitative-db/40-research/cases/case-20260414-4e668883/timeline.md"
  ],
  "review_frontmatter": {
    "type": "learning_note",
    "learning_type": "case_review",
    "learning_scope": "resolved_case",
    "case_key": "case-20260414-4e668883",
    "market_category": "polymarket-discovery",
    "domain": "crypto",
    "subdomain": "threshold_touch_markets",
    "entity": "ethereum",
    "topic": "Binance 1-minute high touch resolution near round-number resistance",
    "date_created": "2026-04-14",
    "resolution_date": "2026-04-14T13:20:02-04:00",
    "evaluation_scope": "resolved_case",
    "evaluation_target": "pipeline_case",
    "outcome_observed": "1.0",
    "decision_taken": "watch_only",
    "error_pattern": "underconfidence_on_nearby_touch_market",
    "intervention_status": "hold",
    "related_entities": [
      "ethereum",
      "binance",
      "polymarket"
    ],
    "related_drivers": [
      "threshold proximity",
      "touch-style settlement mechanics",
      "verification-surface caution"
    ],
    "upstream_inputs": [
      "qualitative-db/40-research/cases/case-20260414-4e668883/case.md",
      "qualitative-db/40-research/cases/case-20260414-4e668883/decision-maker/artifacts/decision-maker-packet.json",
      "qualitative-db/40-research/cases/case-20260414-4e668883/synthesizer-agent/syndicated-finding.runtime.json",
      "qualitative-db/40-research/cases/case-20260414-4e668883/timeline.md",
      "qualitative-db/40-research/cases/case-20260414-4e668883/researcher-swarm-current.md"
    ],
    "downstream_uses": [],
    "promotion_candidates": [],
    "tags": [
      "learning/case_review",
      "platform/polymarket",
      "crypto/ethereum",
      "threshold-touch",
      "underconfidence"
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
  },
  {
    "signal_kind": "false_signal",
    "signal_key": "misleading-input",
    "occurrence_count": 11,
    "case_count": 1
  },
  {
    "signal_kind": "source_performance",
    "signal_key": "high-signal-input",
    "occurrence_count": 11,
    "case_count": 1
  },
  {
    "signal_kind": "driver_pattern",
    "signal_key": "threshold-proximity",
    "occurrence_count": 1,
    "case_count": 1
  },
  {
    "signal_kind": "driver_pattern",
    "signal_key": "touch-style-settlement-mechanics",
    "occurrence_count": 1,
    "case_count": 1
  },
  {
    "signal_kind": "driver_pattern",
    "signal_key": "verification-surface-caution",
    "occurrence_count": 1,
    "case_count": 1
  },
  {
    "signal_kind": "source_performance",
    "signal_key": "the-market-implied-persona-explicitly-identified-the-key-rule",
    "occurrence_count": 1,
    "case_count": 1
  },
  {
    "signal_kind": "workflow_performance",
    "signal_key": "underconfidence-on-nearby-touch-market",
    "occurrence_count": 1,
    "case_count": 1
  }
]
```

## Task

Propose at most one daily candidate and at most one durable candidate.
Use the exact `signal_kind` and `signal_key` values from the recurrence statistics when anchoring a candidate.
The system will compute the actual importance score deterministically; focus on whether a candidate should exist at all and how it should be described.
If no candidate clearly clears the bar, return `null` for that slot.
Return only the final JSON object.
