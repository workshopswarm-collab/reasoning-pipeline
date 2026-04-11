# Runtime Harness Procedure

Use this procedure when the TUI/main runtime needs to deliver a prepared dispatch manifest into Telegram forum topics.

## Goal

Turn a planner-emitted manifest into:
- one canonical `sessions.send` delivery step per still-queued persona run
- DB patches for successfully delivered runs
- a concise delivery summary

## Required helpers

- `runtime/scripts/internal/load_dispatch_existing_state.py`
- `runtime/scripts/internal/run_dispatch_runtime.py`
- `runtime/scripts/internal/runtime_execute_dispatch.py`
- `runtime/scripts/update_research_run.py`
- `runtime/scripts/internal/auto_finalize_case_after_terminal_run.py`
- `runtime/scripts/runrepairs/finalize_dispatch_after_swarm.py`

## Happy path

### Step 1 — load idempotent state
1. load the manifest
2. load current DB state for the referenced `research_runs`
3. pass that state into `internal/run_dispatch_runtime.py`
4. obtain:
   - validation result
   - launchable runs
   - skipped runs
   - one canonical topic-session handoff payload per launchable run

### Step 2 — bootstrap topics and execute handoffs
For each launchable run in order:
1. create/reuse the controller topic once for the dispatch and create/reuse one fresh persona topic per queued run
2. resolve each persona topic to its Telegram topic session key
3. after bootstrap, materialize the canonical topic session if needed, call `sessions.send` with the now-resolved `launchable_run.handoff_payload`, and fan out the persona handoffs in parallel where practical
4. if delivery succeeds:
   - immediately build the corresponding DB patch payload
   - immediately apply that patch via `update_research_run.py`
   - treat the `queued -> running` DB patch as the canonical lifecycle transition
   - let `update_research_run.py` auto-post the visible Telegram `STARTING RESEARCH` marker from stored delivery metadata
5. if delivery fails:
   - record the error
   - do not patch the run to `running`
   - continue so partial success can be preserved

### Step 3 — verify lifecycle patching
For each successful delivery/patch:
1. verify the row now shows:
   - `status = running`
   - `started_at` set
   - `notes.dispatch_stage = persona_topic_running`
   - `notes.delivery_target_session_key`
   - `notes.delivery_target_chat_id`
   - `notes.delivery_target_topic_id`
   - `notes.visible_start_posted_at` when visible start posting succeeds
2. treat missing `visible_start_posted_at` as a launch-path problem to repair, not as expected behavior

### Step 4 — summarize delivery
Use the runtime summary object to report one of:
- `delivered_all`
- `delivered_partial`
- `delivery_failed`

## Completion/finalization behavior

### Primary path
- persona lanes reconcile completion/failure through `update_research_run.py`
- successful completion auto-posts the visible Telegram finish marker
- terminal run updates auto-attempt `auto_finalize_case_after_terminal_run.py`
- that helper now stays quiet until the active dispatch is actually terminal (`queued == 0` and `running == 0`)
- if the swarm is fully completed, that helper:
  - runs manifest reconciliation
  - prepares synthesis-stage artifacts
  - hands off to the single-flight synthesis launcher so one dedicated synthesis topic/executor is created for the dispatch
  - closes the parent case
  - closes the parent market pipeline state
- if the swarm is terminal but not fully completed, the market moves to `needs_intervention`

### Manual backstop
Use:
- `runtime/scripts/runrepairs/finalize_dispatch_after_swarm.py --file <manifest> --apply`

Use the manual finalizer when:
- artifacts exist but DB state still lags
- you are repairing older runs created before the auto-finalizer existed
- you want an explicit post-run audit of terminal counts

## Retry rule

Retries should only re-deliver runs that are still:
- `status = queued`

The fixed-channel runtime should skip any run already marked:
- `running`
- `completed`
- `failed`

## Non-goals

The runtime harness no longer depends on:
- legacy Discord/thread-binding machinery
- subagent session creation
- unique per-run child-session routing metadata

The handoff surface is the Telegram topic session created or reused for each queued persona run.
