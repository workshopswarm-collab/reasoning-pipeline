# Evaluator workflow (initial implementation)

This documents the first evaluator implementation slice.

## Current implemented pieces

- `runtime/lib/paths.py`
  - canonical evaluator path helpers for case-review artifacts
- `runtime/lib/io.py`
  - lightweight markdown/json parsing helpers
- `runtime/lib/case_artifacts.py`
  - discovery helpers for upstream case artifacts
- `runtime/lib/db.py`
  - evaluator-side Postgres execution helper / db-url resolution
- `runtime/lib/quant_truth.py`
  - quant truth lookup for case / forecast / resolution / snapshot surfaces
- `runtime/scripts/build_case_event_timeline.py`
  - builds a structured evaluator event timeline from current case artifacts
- `runtime/scripts/compile_learning_packet.py`
  - compiles a learning packet that now attempts to merge file provenance with quant truth
- `runtime/scripts/draft_case_review.py`
  - drafts a markdown review note from a compiled learning packet
- `runtime/scripts/upsert_learning_case_review_index.py`
  - builds a deterministic case-review index record and persists it when `learning_case_reviews` exists
- `runtime/scripts/extract_learning_signals.py`
  - extracts deterministic structured signals from a review note and writes `signal-packet.json`, persisting them when `learning_signal_occurrences` exists
- `runtime/scripts/materialize_case_review_bundle.py`
  - one-command materializer that writes canonical `learning-packet.json`, `review.md`, `signal-packet.json`, and `provenance.json` into `qualitative-db/50-learnings/case-reviews/<case-key>/`
- `runtime/scripts/backfill_case_review_bundles.py`
  - materializes canonical evaluator bundles in batch for resolved cases, optionally with `--agent-review`
- `runtime/scripts/run_evaluator_review.py`
  - sends a review/refinement prompt to `agent:evaluator:main`, validates the returned markdown, writes canonical `review.md`, and re-persists the resulting index/signal rows
- `runtime/scripts/run_evaluator_memory_upgrade.py`
  - asks `agent:evaluator:main` for memory-upgrade candidates, then computes a hybrid deterministic importance score (review status + signal kind + recurrence + review richness + agent-authored-review bonus + similar-rule penalty) before gating daily vs durable memory writeback into `~/.openclaw/evaluator/`
- `runtime/scripts/aggregate_learning_patterns.py`
  - generates cross-case pattern indexes from persisted learning signals
- `sql/010_learning_case_reviews.sql`
  - evaluator table for indexed case-review rows
- `sql/011_learning_signal_occurrences.sql`
  - evaluator table for extracted signal rows

## Initial operating sequence

### Fast path: materialize a canonical bundle

Deterministic scaffold only:

```bash
python3 roles/evaluator/runtime/scripts/materialize_case_review_bundle.py --case-key <case-key>
```

Deterministic scaffold + agent-written canonical review:

```bash
python3 roles/evaluator/runtime/scripts/materialize_case_review_bundle.py --case-key <case-key> --agent-review
```

Importance-gated evaluator memory upgrade after a reviewed case:

```bash
python3 roles/evaluator/runtime/scripts/run_evaluator_memory_upgrade.py --case-key <case-key>
```

### Manual path

1. Build a timeline

```bash
python3 roles/evaluator/runtime/scripts/build_case_event_timeline.py --case-key <case-key>
```

2. Compile a learning packet

```bash
python3 roles/evaluator/runtime/scripts/compile_learning_packet.py --case-key <case-key>
```

3. Draft a review note

```bash
python3 roles/evaluator/runtime/scripts/draft_case_review.py --case-key <case-key>
```

## Current limitations

- Quant-db / Postgres resolution and forecast ingestion is now partially wired into the packet, but richer score reporting and cohort metrics are still minimal.
- Market-path reconstruction is still shallow.
- Causal attribution is intentionally conservative and mostly unpopulated.
- Draft reviews are bridge-driven scaffolds, not final evaluator judgments.

## Intended next steps

- add structured market/action timeline reconstruction
- backfill more resolved cases into the evaluator corpus
- refine aggregate signal quality and promotion rules
- consider whether agent-review + memory-upgrade should become the default for single-case evaluator materialization
- generate LMD bundles for runtime reuse
