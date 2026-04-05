---
type: system_guide
domain: templates
status: active
last_updated: 2026-03-26
owner: orchestrator
tags: [templates/guide, qualitative-db/00-system/templates]
---

# Templates

This README is subordinate to `qualitative-db/00-system/README.md`. If there is any conflict, follow `qualitative-db/00-system/`.

Fresh-instance shortcut:
- read `qualitative-db/00-system/START-HERE.md` first
- read this folder only when you are about to create or substantially rewrite a note
- read only the specific template that matches the note you are writing
- within a single run, read the matching template once per artifact type, then reuse that structure unless confusion or a major change requires reopening it

Terminology note:
- in this vault, a **dossier** means a canonical entity note in `qualitative-db/20-entities/`
- research-layer notes are not dossiers

These templates support the quant-research pipeline:

1. researchers create source notes, findings, assumption notes, evidence maps, investigations, product notes, and syntheses in `40-research/`
2. the orchestrator consolidates research and presents it to the decision-maker
3. the decision-maker may write a final recommendation artifact when a persistent decision record is actually needed
4. resolved cases are reviewed in `50-retrospectives/`
5. durable lessons may later be promoted into stable layers by authorized roles

## Primary folder-to-template map

### `qualitative-db/40-research/`

Canonical live structure:
- `cases/<case-key>/source-notes/` -> `source-note-template.md`
- `cases/<case-key>/analyses/<YYYY-MM-DD>/<dispatch-id>/personas/` -> `agent-finding-template.md`
- `cases/<case-key>/analyses/<YYYY-MM-DD>/<dispatch-id>/assumptions/` -> `assumption-note-template.md`
- `cases/<case-key>/analyses/<YYYY-MM-DD>/<dispatch-id>/evidence/` -> `evidence-map-template.md`
- `product-notes/` -> `product-note-template.md`
- `review-queue/` -> proposal/review artifacts; use the matching candidate/proposal template

Compatibility / legacy flat surfaces may still exist during migration:
- `source-notes/`
- `agent-findings/`
- `assumption-notes/`
- `evidence-maps/`

Conceptual / optional artifact types:
- `investigations/` -> `investigation-template.md`
- `syntheses/` -> `synthesis-template.md`

Note: `investigations/` and `syntheses/` remain supported artifact types, but they are not currently present as live top-level folders under `qualitative-db/40-research/` in this repo snapshot.

### `qualitative-db/50-retrospectives/`

- all current retrospective subfolders -> `retrospective-note-template.md`

Current retrospective subfolders covered by the shared template:
- `agent-performance/`
- `false-signals/`
- `input-quality/`
- `methodology-adjustments/`
- `missed-signals/`
- `source-performance/`

## Stable-layer and supporting templates

These templates are useful outside the default `40-research/` and `50-retrospectives/` folder map.

### Stable-layer templates

- `domain-overview-template.md`
  - canonical overview template for `qualitative-db/10-domains/**/00-overview.md`

- `driver-overview-template.md`
  - canonical driver template for `qualitative-db/30-drivers/*.md`

- `entity-overview-template.md`
  - stable canonical entity template for `20-entities/`

### Supporting governance / decision templates

- `decision-note-template.md`
  - for a persistent decision-maker recommendation artifact
  - use only when the pipeline actually needs to preserve a final recommendation in file form
  - no default vault folder is required yet

- `canonical-entity-update-proposal-template.md`
  - for proposing updates to canonical entity notes in `qualitative-db/20-entities/`
  - use when research reveals a stable-layer issue but you do not want to rewrite canon directly
  - default home can be alongside the related research thread or handoff material
  - preferred review-queue home: `qualitative-db/40-research/review-queue/canonical-update-proposals/`

- `durable-lesson-candidate-template.md`
  - for surfacing potentially reusable lessons discovered during research before they are promoted into stable layers
  - default home: `qualitative-db/40-research/review-queue/durable-lesson-candidates/`

- `driver-candidate-template.md`
  - for proposing a missing or underbuilt market driver when existing `30-drivers/` coverage does not fit well
  - default home: `qualitative-db/40-research/review-queue/drivers-candidates/`

## Template roles

- `source-note-template.md`
  - capture what a source said and why it may matter
- `agent-finding-template.md`
  - capture a research role's directional interpretation
- `assumption-note-template.md`
  - isolate explicit assumptions so they can be audited later
- `evidence-map-template.md`
  - organize support, contradiction, conflict, and update logic around a question
- `investigation-template.md`
  - track multi-pass research threads that stay open across time
- `product-note-template.md`
  - track versioned or release-specific product observations that are too time-bound for canon
- `synthesis-template.md`
  - main orchestrator consolidation layer before handoff to the decision-maker
- `decision-note-template.md`
  - final decision-maker recommendation template when a persistent decision record is needed
- `retrospective-note-template.md`
  - evaluate what worked, what failed, and what durable lessons emerged after resolution
- `domain-overview-template.md`
  - standardize canonical domain overviews in `10-domains/`
- `driver-overview-template.md`
  - standardize reusable causal mechanism notes in `30-drivers/`
- `entity-overview-template.md`
  - stable canonical entity template for `20-entities/`
- `canonical-entity-update-proposal-template.md`
  - propose updates to canonical entity notes without rewriting canon directly
- `durable-lesson-candidate-template.md`
  - propose potentially reusable lessons before promotion into stable layers
- `driver-candidate-template.md`
  - propose a missing or underbuilt market driver for review before any canonical driver is created
- `researcher-task-brief-template.md`
  - reusable delegation scaffold for research-swarm subagents so role, permissions, read path, and output expectations are explicit

## Rule

Use the research templates for case work first. Use canonical templates only when the stable-layer threshold has been met.

Lightweight operating rule:
- before creating or substantially rewriting a real vault artifact, read the matching template
- do this once per artifact type per run, not before every single note
- do not apply this rule to scratch reasoning, chat replies, or lightweight status updates

For canonical entity notes, remember the maintenance distinction:
- body prose is stable canon and should stay higher-bar
- linkage fields such as `related_entities` and `related_drivers` are curated graph metadata and may be revised more fluidly when navigation or retrieval improves
