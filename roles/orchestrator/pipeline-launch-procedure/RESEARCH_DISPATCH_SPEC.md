# Research Dispatch Spec

## Purpose

Define the canonical state model and dispatch contract for the **fresh Telegram topic** architecture.

This spec connects:
- market/case state in Postgres
- planner-side prompt generation
- fresh Telegram topics as the runtime surface
- durable research artifacts in `qualitative-db/40-research/`

## Canonical truth

- Runtime surface: fresh Telegram topics
- Handoff primitive: `sessions_send`
- Stable completion key: `research_run_id`
- Primary completion path: runtime-side terminal updates
- Parent finalization policy: close the case/market once all sibling runs are terminal
- Manual repair path: manifest finalizer

## State model

### Market state
- `markets.pipeline_status = pending_research`
  - waiting for work
- `markets.pipeline_status = researching`
  - selected and actively in flight
- `markets.pipeline_status = closed`
  - no longer actively in the pipeline

### Case state
- `cases.status = open`
  - active case
- `cases.status = closed`
  - parent case finalized

### Run state
- `queued`
  - run row exists but has not been handed off yet
- `running`
  - handoff delivered and start recorded
- `completed`
  - terminal success
- `failed`
  - terminal failure

### Dispatch-stage notes
Expected `notes.dispatch_stage` values:
- `awaiting_topic_creation`
- `awaiting_topic_handoff`
- `persona_topic_running`
- `completed`
- `terminated`

## Runtime surface

The runtime surface is **Telegram forum topics**.

The current model is:
- one fresh controller topic per case
- one fresh persona topic per persona per case

Routing/config metadata lives in:
- `runtime/telegram-runtime-config.json`

## Required fields per run

At minimum each run should track:
- `case_id`
- `run_label`
- `agent_label`
- `runtime`
- `status`
- `started_at`
- `workspace_note_path`
- `notes.dispatch_id`
- `notes.dispatch_stage`
- `notes.delivery_target_session_key`
- `notes.delivery_target_chat_id`
- `notes.delivery_target_topic_id`
- `notes.delivery_target_topic_title`

Rule:
- `started_at` must reflect actual handoff/start time, not row creation time

## Lifecycle contract

### Planner responsibilities
`dispatch_case_research.py` must:
1. ensure the market is `researching`
2. create one queued `research_runs` row per persona
3. generate one prompt per persona
4. emit one logical Telegram topic target per persona
5. emit one post-handoff DB patch template per persona

### Runtime responsibilities
`run_dispatch_runtime.py` / `runtime_execute_dispatch.py` must:
1. validate the manifest
2. consult current DB state for idempotency
3. skip non-queued runs
4. emit one `sessions_send` handoff step per still-queued run
5. build one post-handoff DB patch per successful delivery
6. summarize delivery as `delivered_all`, `delivered_partial`, or `delivery_failed`

### Persona-lane responsibilities
Each persona lane should, when possible, emit visible lifecycle lines in this exact format:
- `STARTING RESEARCH | market=<market title> | persona=<persona> | research_run_id=<id>`
- `FINISHED RESEARCH | market=<market title> | persona=<persona> | research_run_id=<id> | agent_finding_path=<path>`

Important nuance:
- those visible lines come from the lane after assignment receipt
- the original `sessions_send` handoff is internal and may not be visible in Discord

## Running-state rule

A run becomes `running` only after:
1. the handoff message is successfully delivered into the mapped persona session
2. the DB patch is applied

That patch should set:
- `status = running`
- `started_at = NOW()` if missing
- `notes.dispatch_stage = persona_topic_running`
- `notes.delivery_target_session_key`
- `notes.delivery_target_chat_id`
- `notes.delivery_target_topic_id`
- `notes.delivery_target_topic_title`

## Completion rule

A run becomes `completed` or `failed` only when a runtime-side helper updates the corresponding `research_runs` row.

For the fresh-topic model, the stable join key is:
- `research_run_id`

`delivery_target_session_key` is useful metadata, but it is **not** the canonical completion key because topic/session transport metadata should remain replaceable without changing the durable run identity.

Terminal run updates should flow through:
- `runtime/scripts/update_research_run.py`
- `runtime/scripts/reconcile_research_run_completion.py`

Those helpers now auto-attempt:
1. manifest-level reconciliation through `runtime/scripts/finalize_dispatch_after_swarm.py`
2. parent closure when all sibling runs are terminal

## Parent-finalization policy

Current policy:
- close the case/market only when all runs are `completed`
- if some runs fail, keep the parent case/market open for intervention rather than auto-closing it as a successful swarm completion

## Safety nets

### Artifact-vs-DB lag
If the primary artifact exists but the DB row is still `queued` or `running`, use:
- `runtime/scripts/reconcile_dispatch_from_artifacts.py`

### Manual manifest-level repair
If automatic finalization is missed, run:
- `runtime/scripts/finalize_dispatch_after_swarm.py --file <manifest> --apply`

## Default artifact paths

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
