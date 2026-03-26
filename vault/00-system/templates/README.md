---
type: system_guide
domain: templates
status: active
last_updated: 2026-03-25
owner: orchestrator
tags: [templates/guide, vault/00-system/templates]
---

# Templates

This README is subordinate to `vault/00-system/README.md`. If there is any conflict, follow `vault/00-system/`.

Fresh-instance shortcut:
- read `vault/00-system/START-HERE.md` first
- read this folder only when you are about to create or substantially rewrite a note
- read only the specific template that matches the note you are writing

Terminology note:
- in this vault, a **dossier** means a canonical entity note in `vault/20-entities/`
- research-layer notes are not dossiers

These templates support the quant-research pipeline:

1. researchers create source notes, findings, evidence maps, investigations, and syntheses in `40-research/`
2. the orchestrator consolidates research and presents it to the decision-maker
3. the decision-maker writes the final recommendation
4. resolved cases are reviewed in `50-retrospectives/`
5. durable lessons may later be promoted into stable layers by authorized roles

## Template roles

- `source-note-template.md`
  - capture what a source said and why it may matter
- `agent-finding-template.md`
  - capture a research role's directional interpretation
- `evidence-map-template.md`
  - organize support, contradiction, conflict, and update logic around a question
- `investigation-template.md`
  - track multi-pass research threads that stay open across time
- `synthesis-template.md`
  - main orchestrator consolidation layer before handoff to the decision-maker
- `decision-note-template.md`
  - final decision-maker recommendation template
- `retrospective-note-template.md`
  - evaluate what worked, what failed, and what durable lessons emerged
- `entity-overview-template.md`
  - stable canonical entity template for `20-entities/`
- `dossier-update-proposal-template.md`
  - propose updates to canonical entity notes without rewriting canon directly

## Rule

Use the research templates for case work first. Use canonical templates only when the stable-layer threshold has been met.

For canonical entity notes, remember the maintenance distinction:
- body prose is stable canon and should stay higher-bar
- linkage fields such as `related_entities` and `related_drivers` are curated graph metadata and may be revised more fluidly when navigation or retrieval improves