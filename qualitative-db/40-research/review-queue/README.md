---
type: research_review_queue_index
domain: research
status: active
last_updated: 2026-04-14
owner: orchestrator
tags: [research/review-queue, qualitative-db/40-research, review]
---

# Review Queue

This folder is the **research-layer handoff surface** for items that should be reviewed by the Orchestrator before any stable-layer change is made.

The queue exists so researchers can surface:
- proposed canon changes
- durable lesson candidates
- drivers candidates
- linkage-repair candidates

without directly editing stable layers.

## Why this lives in `40-research/`

The vault's policy is:
- new evidence belongs in research first
- canon updates should be proposed before they are applied
- researchers normally write to `40-research/`, not to stable layers
## Subfolders

### `canonical-update-proposals/`

Use for proposed updates to:
- canonical entity notes in `20-entities/`
- canonical domain overviews in `10-domains/`
- durable driver notes in `30-drivers/`

These are review artifacts only.
They are not canon.

### `durable-lesson-candidates/`

Use for potentially reusable lessons that emerged during current research but have **not yet** been accepted into stable layers.

Examples:
- likely cross-case driver lessons
- source-selection lessons
- weighting lessons
- recurring failure-mode observations
- methodology improvements

These may later be:
- rejected as case-specific noise
- routed into `50-learnings/`
- promoted into `30-drivers/`, `10-domains/`, `20-entities/`, or `00-system/` guidance

### `drivers-candidates/`

Use for proposed market drivers when:
- no existing driver seems like a good fit
- existing driver coverage seems too weak or too coarse
- a repeatedly relevant mechanism appears missing from `30-drivers/`

These are review artifacts, not new canonical drivers.

Operational note:
- top-level index: `qualitative-db/40-research/review-queue/drivers-candidates/generated-index.md`
- generated raw candidate notes now live in `qualitative-db/40-research/review-queue/drivers-candidates/candidate-notes/` with filenames like `generated-driver-candidate-<slug>.md`
- LLM-assisted family review outputs live in `qualitative-db/40-research/review-queue/drivers-candidates/surfaced-family-review/`
  - top-level LLM family index: `qualitative-db/40-research/review-queue/drivers-candidates/surfaced-family-review/LLM-proposed-family-index.md`
  - markdown review notes: `qualitative-db/40-research/review-queue/drivers-candidates/surfaced-family-review/review-notes/`
  - JSON input packets: `qualitative-db/40-research/review-queue/drivers-candidates/surfaced-family-review/inputs/`
- generated notes aggregate recurring `proposed_drivers` across case artifacts to help promotion review
- manually-authored review notes may still coexist alongside generated notes when a human wants to add interpretation or promotion rationale

### `linkage-repair-candidates/`

Use for proposed graph/navigation repairs such as:
- missing `related_entities`
- missing `related_drivers`
- reciprocal-link gaps
- structurally important underlinked neighborhoods

## Researcher authority

Researchers may write here.

Researchers should use this folder to **propose**, not to bypass stable-layer review.

## Orchestrator authority

The Orchestrator reviews queue items and decides whether to:
- keep them in research only
- promote them into canon
- turn them into structured learning notes
- reject them as transient or weakly supported

## Naming guidance

Prefer filenames that preserve case context and intent.

Examples:
- `2026-03-29-us-election-polling-driver-update-candidate.md`
- `2026-03-29-openai-product-linkage-repair-candidate.md`
- `2026-03-29-fed-cut-timing-durable-lesson-candidate.md`

## Rule of thumb

If you think, "this may deserve a stable-layer change," but you are not explicitly authorized to make that change directly, put it here.