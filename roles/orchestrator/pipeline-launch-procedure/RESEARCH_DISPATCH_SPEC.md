# Research Dispatch Spec

## Purpose

Define the dispatch/state contract for the current **fixed Discord persona-channel** architecture.

This system connects:
- market/case state in Postgres
- planner-side prompt generation
- fixed Discord persona lanes as the runtime surface
- durable research artifacts in `qualitative-db/40-research/`

## Core model

### Market queue
Markets waiting for work are represented by:
- `markets.pipeline_status = pending_research`

### Active market
When a case is selected and dispatch planning begins:
- `markets.pipeline_status = researching`

### Research runs
Each selected case produces one `research_runs` row per persona.

Current personas:
- `base-rate`
- `market-implied`
- `variant-view`
- `risk-manager`
- `catalyst-hunter`

## Runtime surface

The runtime surface is **not** auto-created Discord threads.

The current runtime surface is:
- one fixed Discord channel per persona
- one controller channel for orchestration/monitoring

Routing metadata is stored in:
- `runtime/persona-channel-map.json`

## Required fields per run

At minimum each run should track:
- `case_id`
- `run_label`
- `agent_label`
- `runtime`
- `status`
- `started_at` (actual handoff/start time, not row creation)
- `workspace_note_path`
- `notes.dispatch_id`
- `notes.dispatch_stage`
- `notes.delivery_target_session_key`
- `notes.delivery_target_channel_id`

## Dispatch stages

Current expected stages:
- `awaiting_persona_channel_handoff`
- `persona_channel_running`
- `completed`
- `terminated`

## Lifecycle rules

### Planner side
`dispatch_case_research.py` must:
1. ensure the market is `researching`
2. create one queued `research_runs` row per persona
3. generate one prompt per persona
4. emit one fixed-channel handoff payload per persona
5. emit one post-handoff DB patch template per persona

### Runtime side
`run_dispatch_runtime.py` / `runtime_execute_dispatch.py` must:
1. validate the manifest
2. consult current DB state for idempotency
3. skip non-queued runs
4. emit one `sessions_send` handoff step per still-queued run
5. build one post-handoff DB patch per successful delivery
6. summarize delivery status as `delivered_all`, `delivered_partial`, or `delivery_failed`

### Persona-lane behavior
Each persona lane assignment should require visible lane updates in this standardized format:
- `STARTING RESEARCH | market=<market title> | persona=<persona> | research_run_id=<id>`
- `FINISHED RESEARCH | market=<market title> | persona=<persona> | research_run_id=<id> | agent_finding_path=<path>`

Those visible messages come from the lane after it receives the assignment. The original `sessions_send` handoff itself is internal and may not be visible in Discord.

## Running-state rule

A run becomes `running` only after:
- its handoff message is successfully delivered into the mapped persona channel session
- and the DB patch is applied

That patch should set:
- `status = running`
- `started_at = NOW()` (if not already set)
- `notes.dispatch_stage = persona_channel_running`
- `notes.delivery_target_session_key`
- `notes.delivery_target_channel_id`

## Completion rule

A run becomes `completed` or `failed` only when a runtime-side helper updates the corresponding `research_runs` row.

For the fixed-channel model, the stable join key should be:
- `research_run_id`

`delivery_target_session_key` is useful metadata, but it is not a unique long-term completion join key because persona channels are persistent lanes reused across runs.

Safety net:
- if the primary artifact exists but the DB row is still `queued`/`running`, use `runtime/scripts/reconcile_dispatch_from_artifacts.py`

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
