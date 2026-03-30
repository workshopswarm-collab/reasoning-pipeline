# OpenClaw Runtime Bridge

## Purpose

Describe the boundary between:
- planner-side local Python scripts
- runtime-side OpenClaw tool execution

In the current architecture, the bridge is:
- planner emits a manifest with fixed-channel handoff payloads
- runtime executes those payloads with `sessions_send`
- runtime patches DB state after successful delivery

## What local Python can do

Planner/local Python can:
- read/write Postgres through `psql`
- select the next market
- open the case
- create queued run rows
- build prompts
- write the canonical dispatch manifest

Planner/local Python cannot call OpenClaw runtime tools directly.

## What OpenClaw runtime does

The OpenClaw runtime does the operational delivery work:
1. read the manifest
2. load existing DB state for idempotency
3. determine which runs are still launchable (`status = queued`)
4. call `sessions_send` into each mapped persona channel
5. patch successful handoffs to `running`
6. report concise delivery summaries

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
- the old `sessions_spawn` thread-bound launch path

Each run now carries:
- `handoff.target`
- `handoff.handoff_payload`
- `handoff.post_handoff_update_template`

## DB patch rule

After a successful `sessions_send`, the runtime should apply the corresponding DB patch through:
- `runtime/scripts/update_research_run.py`

That post-handoff patch should set:
- `status = running`
- `started_at` (if not already set)
- `notes.dispatch_stage = persona_channel_running`
- `notes.delivery_target_session_key`
- `notes.delivery_target_channel_id`

Important nuance:
- `sessions_send` confirms internal session delivery
- it does not by itself guarantee a visible kickoff post in Discord
- visible STARTING/FINISHED posts should be emitted by the persona lane after it receives the assignment when possible

## Completion note

Because the fixed persona channels are persistent lanes, completion should eventually resolve by:
- `research_run_id`

not by a unique child subagent session id.
