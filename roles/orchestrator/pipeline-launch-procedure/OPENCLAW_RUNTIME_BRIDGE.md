# OpenClaw Runtime Bridge

## Purpose

Describe the boundary between:
- planner-side local Python scripts
- runtime-side OpenClaw tool execution

## Canonical model

Planner emits a manifest.
Runtime consumes that manifest.
Runtime owns delivery and lifecycle reconciliation.

In the current architecture:
- planner emits fixed-channel handoff payloads
- runtime delivers them with `sessions_send`
- runtime patches run state after successful delivery
- runtime reconciles terminal completion/failure back into `research_runs`
- runtime auto-attempts parent case/market finalization when the swarm becomes fully terminal

## What local Python can do

Planner/local Python can:
- read/write Postgres through `psql`
- select the next market
- open/fetch the case
- create queued run rows
- build prompts
- write the canonical dispatch manifest

Planner/local Python cannot call OpenClaw runtime tools directly.

## What OpenClaw runtime does

The OpenClaw runtime owns operational execution:
1. read the manifest
2. load existing DB state for idempotency
3. determine which runs are still launchable (`status = queued`)
4. call `sessions_send` into each mapped persona channel
5. patch successful handoffs to `running`
6. reconcile terminal completion/failure updates back into `research_runs`
7. auto-attempt manifest reconciliation + parent case/market closure when the swarm becomes fully terminal
8. report concise delivery summaries

## Runtime inputs

### Manifest
Produced by:
- `planner/scripts/dispatch_case_research.py`

### Existing run-state map
Produced by:
- `runtime/scripts/load_dispatch_existing_state.py`

### Runtime plan
Produced by:
- `runtime/scripts/run_dispatch_runtime.py`
- `runtime/scripts/runtime_execute_dispatch.py`

## Canonical handoff primitive

The current handoff primitive is:
- `sessions_send`

Not:
- `sessions_spawn`
- thread-bound Discord launch logic

Each run carries:
- `handoff.target`
- `handoff.handoff_payload`
- `handoff.post_handoff_update_template`

## DB patch rule

After a successful `sessions_send`, the runtime should apply the matching DB patch through:
- `runtime/scripts/update_research_run.py`

That post-handoff patch should set:
- `status = running`
- `started_at` if missing
- `notes.dispatch_stage = persona_channel_running`
- `notes.delivery_target_session_key`
- `notes.delivery_target_channel_id`

Important nuance:
- `sessions_send` confirms internal session delivery
- it does not by itself guarantee a visible kickoff post in Discord
- visible STARTING/FINISHED posts should be emitted by the persona lane after it receives the assignment when possible

## Completion model

Because fixed persona channels are persistent lanes, completion should resolve by:
- `research_run_id`

Not by:
- a unique child subagent session id

Canonical completion path:
1. persona lane finishes work
2. runtime-side helper updates the matching `research_runs` row
3. `update_research_run.py` auto-attempts `auto_finalize_case_after_terminal_run.py`
4. if all sibling runs are terminal, parent `cases.status` and `markets.pipeline_status` are closed automatically

## Manual backstop

If reconciliation is missed, run:
- `runtime/scripts/finalize_dispatch_after_swarm.py --file <manifest> --apply`
