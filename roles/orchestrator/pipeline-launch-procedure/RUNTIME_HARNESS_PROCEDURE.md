# Runtime Harness Procedure

Use this procedure when the TUI/main runtime wants to deliver a prepared dispatch manifest into the fixed Discord persona channels.

## Goal

Turn a planner-emitted manifest into:
- one `sessions_send` step per still-queued persona run
- DB patches for the successfully delivered runs
- a concise delivery summary

## Required helpers

- `runtime/scripts/load_dispatch_existing_state.py`
- `runtime/scripts/run_dispatch_runtime.py`
- `runtime/scripts/runtime_execute_dispatch.py`
- `runtime/scripts/update_research_run.py`

## Procedure

### Step 1 — prepare idempotent launch state
1. load the manifest
2. load current DB state for the referenced `research_runs`
3. pass that state into `run_dispatch_runtime.py`
4. obtain:
   - validation result
   - launchable runs
   - skipped runs
   - one `sessions_send` payload per launchable run

### Step 2 — execute handoffs
For each launchable run in order:
1. call `sessions_send` with `launchable_run.handoff_payload`
2. if delivery succeeds:
   - record the known target session key from the payload/target map
   - treat this as internal delivery into the persona session, not necessarily as a visible Discord kickoff post
3. if delivery fails:
   - record the error
   - continue so partial success can be preserved

### Step 3 — build/apply DB patches
For each successful delivery:
1. call `run_dispatch_runtime.py` replay mode with the collected handoff results
2. obtain the per-run patch payloads / update commands
3. apply each patch via `update_research_run.py`
4. verify the row now shows:
   - `status = running`
   - `started_at` set
   - `notes.dispatch_stage = persona_channel_running`
   - `notes.delivery_target_session_key`
   - `notes.delivery_target_channel_id`

### Step 4 — summarize
Use the runtime summary object to report:
- `delivered_all`
- `delivered_partial`
- or `delivery_failed`

### Step 5 — repair stale artifact/DB mismatches when needed
If a lane produced its assigned primary artifact but failed to mark the run completed:
- use `runtime/scripts/reconcile_dispatch_from_artifacts.py`
- this should be treated as a safety net, not the normal completion path

## Retry rule

Retries should only re-deliver runs that are still:
- `status = queued`

The fixed-channel runtime should skip any run already marked:
- `running`
- `completed`
- `failed`

## Important note

The runtime harness no longer depends on:
- legacy thread-binding machinery
- subagent session creation
- unique per-run child-session routing metadata

The handoff surface is now the fixed Discord persona-channel session map.
