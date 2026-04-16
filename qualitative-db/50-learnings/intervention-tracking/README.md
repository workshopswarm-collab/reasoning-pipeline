---
type: system_guide
domain: learnings
status: active
last_updated: 2026-04-15
owner: evaluator
tags: [learnings/interventions, qualitative-db/50-learnings, recursive-improvement]
---

# Intervention Tracking

This folder holds the canonical markdown notes for explicit pipeline interventions.

Use one intervention per file.
Pair each markdown note with an optional JSON sidecar when the intervention needs structured selector/payload/metric fields for deterministic runtime use.

## Status folders

- `draft/` = candidate interventions under review; may be indexed, but should not directly affect runtime behavior
- `active/` = approved interventions that deterministic code may apply
- `paused/` = temporarily disabled interventions retained for possible reactivation
- `retired/` = previously active interventions intentionally ended
- `rejected/` = interventions judged not worth adopting

## File shape

Recommended note path:

```text
qualitative-db/50-learnings/intervention-tracking/<status>/intervention-<key>.md
```

Optional structured sidecar:

```text
qualitative-db/50-learnings/intervention-tracking/<status>/intervention-<key>.json
```

Use `qualitative-db/00-system/templates/learning-note-template.md` as the base note shape.

Recommended extra frontmatter fields for intervention notes:
- `intervention_key`
- `intervention_status`
- `application_surface`
- `change_kind`
- `hypothesis`

## Structured sidecar contract

When an intervention needs deterministic runtime application, prefer a JSON sidecar like:

```json
{
  "artifact_type": "learning_intervention",
  "schema_version": "v1",
  "intervention_key": "verify-primary-source-for-authoritative-with-fallback",
  "application_surface": "researcher_prompt",
  "change_kind": "verification_rule",
  "target_selector": {},
  "change_payload": {},
  "hypothesis": "...",
  "metric_definition": {},
  "evidence_paths": []
}
```

## Registry / logging scripts

Evaluator-owned registry helpers live under `roles/evaluator/runtime/scripts/`:
- `upsert_learning_interventions.py`
- `log_learning_intervention_application.py`

Research-runtime hook:
- `roles/orchestrator/researchers-swarm-subagents/runtime/scripts/launch_dispatch_with_stateful_posts.py` now calls `log_learning_intervention_application.py` after successful persona handoff whenever the run notes contain intervention metadata (`learning_intervention_keys` and/or `learning_intervention_paths`).

DB schema lives under:
- `roles/evaluator/sql/012_learning_interventions.sql`
- `roles/evaluator/sql/013_learning_intervention_applications.sql`

## Hard rules

- Only `active/` interventions may directly affect runtime behavior.
- Interventions should map to structured deterministic behavior, not arbitrary raw prompt text insertion.
- Interventions may influence retrieval and evaluation, but they do **not** directly create live causal-map canon outside the causal lifecycle policy.
- Every intervention should have a clear hypothesis and a later evaluation path.
- Application logging matters: if an intervention is applied to a case, log it so the effect can later be measured.
