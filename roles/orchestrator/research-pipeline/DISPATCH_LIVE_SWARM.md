# Live Swarm Dispatch Procedure

Use this procedure when launching the real 5-agent swarm from the OpenClaw agent runtime.

## Goal

Launch the full case swarm using the generated prompt text from `roles/orchestrator/research-pipeline/initialize/scripts/build_researcher_prompt.py` rather than a hand-written task string.

This is a **two-phase** process:
- local Python/Postgres scripts prepare the dispatch plan
- the OpenClaw runtime executes the actual `sessions_spawn` calls

See also:
- `roles/orchestrator/research-pipeline/OPENCLAW_RUNTIME_BRIDGE.md`

## Required order

### Phase 1 — prepare the dispatch plan

1. Load case + market context.
2. Set `markets.pipeline_status = researching`.
3. Create one `research_runs` row per persona.
4. For each persona, call `roles/orchestrator/research-pipeline/initialize/scripts/build_researcher_prompt.py` with:
   - `agent_label`
   - `case_id`
   - `case_key`
   - `market_id`
   - `external_market_id`
   - `slug`
   - `title`
   - `description`
   - `current_price`
   - `closes_at`
   - `resolves_at`
   - `metadata`
   - `workspace_note_path`
   - optional exact artifact-path overrides if needed
5. Emit one runtime `spawn_payload` plus one post-spawn DB patch template per persona.

Primary planner:
- `roles/orchestrator/research-pipeline/initialize/scripts/dispatch_case_research.py`

### Phase 2 — execute the dispatch plan in OpenClaw runtime

6. Use each emitted `spawn_payload` as the literal input to `sessions_spawn`.
7. After each spawn, patch the matching `research_runs` row using the emitted post-spawn update template.
8. Fill `research_runs.notes` with runtime metadata from the actual spawn result, especially:
   - `child_session_key`
   - `spawn_run_id`
   - optional `model`
   - optional `thinking`
9. Mark the run `running`.

## Default artifact path rules

### Primary finding
`qualitative-db/40-research/agent-findings/<persona>/<case_key>-<slug>.md`

### Source notes
Directory:
`qualitative-db/40-research/source-notes/by-market/`

Filename prefix:
`<case_key>-<persona>-`

### Assumption note
`qualitative-db/40-research/assumption-notes/<case_key>-<persona>-assumptions.md`

### Evidence map
`qualitative-db/40-research/evidence-maps/<case_key>-<persona>-evidence-map.md`

## Rule

Do not handwrite persona dispatch prompts when `roles/orchestrator/research-pipeline/initialize/scripts/build_researcher_prompt.py` is available. The generated prompt is the source of truth because it reflects the latest researcher contract and artifact path rules.

Do not try to make local subprocess Python call `sessions_spawn` directly. The correct pattern is:
- planner scripts prepare the dispatch manifest
- the OpenClaw runtime executes the spawn payloads
- planner scripts patch DB state using the returned runtime metadata
