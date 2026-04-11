# Research Dispatch Spec

## Purpose

Define the canonical state model and dispatch contract for the current **Telegram-topic researcher swarm plus dedicated synthesis-topic** architecture.

This spec connects:
- market/case state in Postgres
- planner-side prompt generation
- Telegram forum topics as the runtime surface for both researcher and synthesis phases
- durable research artifacts in `qualitative-db/40-research/`

## Canonical truth

- Runtime surface: Telegram forum topics
- Handoff primitive: Gateway RPC `sessions.send` (wrapped by the runtime bridge/helper)
- Stable completion key: `research_run_id`
- Primary completion path: runtime-side terminal updates
- Lifecycle markers: emitted by `update_research_run.py` on `running` / `completed` transitions
- Parent finalization policy: close the case/market once all sibling runs are terminal
- Manual repair path: manifest finalizer

## State model

### Market state
- `markets.pipeline_status = pending_research`
  - waiting for work
- `markets.pipeline_status = researching`
  - selected and actively in flight
- `markets.pipeline_status = needs_intervention`
  - swarm is terminal but did not complete cleanly; human/runtime intervention is needed
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

The current researcher-swarm model is:
- one controller topic per case
- one persona topic per persona per case
- reruns create new attempt rows but should reuse those existing case/persona lanes whenever prior lane metadata exists

The current post-swarm synthesis model is:
- once the active dispatch is truly terminal, synthesis promotion creates one dedicated synthesis topic for that dispatch
- synthesis launch must be treated as a single-flight action so only one process can create/use that topic and spawn the final synthesis executor

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
`internal/run_dispatch_runtime.py` / `runtime_execute_dispatch.py` must:
1. validate the manifest
2. consult current DB state for idempotency
3. skip non-queued runs
4. emit one canonical topic-session handoff step per still-queued run
5. build one post-handoff DB patch per successful delivery
6. summarize delivery as `delivered_all`, `delivered_partial`, or `delivery_failed`

### Persona-lane responsibilities
Each persona lane should:
- do the research work in its assigned Telegram topic session
- write the required artifacts to the assigned paths
- optionally post sparse progress updates in-topic when useful
- reconcile completion/failure through the runtime helper when possible

Canonical visible lifecycle lines are still:
- `STARTING RESEARCH | market=<market title> | persona=<persona> | research_run_id=<id>`
- `FINISHED RESEARCH | market=<market title> | persona=<persona> | research_run_id=<id> | agent_finding_path=<path>`

Important nuance:
- those visible lines are emitted by `update_research_run.py` on state transitions
- the original `sessions.send` handoff is internal and is not itself the visible kickoff post

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

For the persistent-lane / per-attempt model, the stable completion join key is:
- `research_run_id`

Lane continuity should come from case/persona topic reuse, not from overwriting old attempt rows.

`delivery_target_session_key` is useful metadata, but it is **not** the canonical completion key because topic/session transport metadata should remain replaceable without changing the durable run identity.

Terminal run updates should flow through:
- `runtime/scripts/update_research_run.py`
- `runtime/scripts/reconcile_research_run_completion.py`

Those helpers now auto-attempt:
1. a guarded terminality check so dispatch finalization only runs when the active dispatch has no queued/running siblings
2. manifest-level reconciliation plus synthesis promotion through `runtime/scripts/runrepairs/finalize_dispatch_after_swarm.py`
3. parent closure when all sibling runs are terminal

## Parent-finalization policy

Current policy:
- close the case/market only when all runs are `completed`
- if all runs are terminal but one or more did not complete cleanly, set `markets.pipeline_status = needs_intervention` and keep the case open for intervention

## Safety nets

### Artifact-vs-DB lag
If the primary artifact exists but the DB row is still `queued` or `running`, use:
- `runtime/scripts/runrepairs/reconcile_dispatch_from_artifacts.py`

### Manual manifest-level repair
If automatic finalization is missed, run:
- `runtime/scripts/runrepairs/finalize_dispatch_after_swarm.py --file <manifest> --apply`

## Default artifact paths

### Primary finding
`qualitative-db/40-research/cases/<case-key>/researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/personas/<persona>.md`

### Source notes
Directory:
`qualitative-db/40-research/cases/<case-key>/researcher-source-notes/`

### Assumption note
`qualitative-db/40-research/cases/<case-key>/researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/assumptions/<persona>.md`

### Evidence map
`qualitative-db/40-research/cases/<case-key>/researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/evidence/<persona>.md`

### Per-analysis summary
`qualitative-db/40-research/cases/<case-key>/researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/summary.md`
