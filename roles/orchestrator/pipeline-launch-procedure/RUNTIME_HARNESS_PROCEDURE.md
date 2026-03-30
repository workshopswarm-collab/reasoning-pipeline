# Runtime Harness Procedure

Use this procedure when the Orchestrator wants to launch a prepared dispatch manifest end-to-end from the OpenClaw runtime.

## Goal

Provide a thin runtime harness that:
- accepts a planner-emitted dispatch manifest
- validates it
- determines which runs are launchable vs already launched
- executes `sessions_spawn` for launchable runs
- patches `research_runs` with returned runtime metadata
- returns a final launch summary

This is the runtime half of the dispatch architecture.

See also:
- `roles/orchestrator/pipeline-launch-procedure/OPENCLAW_RUNTIME_BRIDGE.md`
- `roles/orchestrator/pipeline-launch-procedure/DISPATCH_LIVE_SWARM.md`
- `roles/orchestrator/pipeline-launch-procedure/initialize/scripts/run_dispatch_runtime.py`
- `roles/orchestrator/pipeline-launch-procedure/initialize/scripts/runtime_execute_dispatch.py`

## Core operating model

- planner scripts prepare the manifest
- the OpenClaw runtime harness executes the launch loop
- the harness does not redesign the plan; it executes it literally
- partial launch success is allowed and should produce `launched_partial`
- retries should only relaunch runs that still lack `notes.child_session_key`

## Inputs required by the harness

1. one dispatch manifest JSON object from:
   - `roles/orchestrator/pipeline-launch-procedure/initialize/scripts/dispatch_case_research.py`
2. current per-run runtime state keyed by `research_run_id` for idempotency
   - at minimum, whether `notes.child_session_key` already exists

## Required runtime sequence

### Step 1 — validate + prepare

Call:
- `roles/orchestrator/pipeline-launch-procedure/initialize/scripts/run_dispatch_runtime.py`

This returns:
- manifest validation result
- launchable runs
- skipped runs
- the exact runtime tool loop

### Step 2 — execute launchable runs

For each `launchable_run` in order:
1. call `sessions_spawn` with `launchable_run.spawn_payload`
2. if spawn succeeds:
   - capture returned `child_session_key`
   - capture returned `spawn_run_id` if available
3. if spawn fails:
   - record the failure
   - continue to the next launchable run

### Step 3 — patch DB after each successful spawn

For each successful spawn:
1. call `run_dispatch_runtime.py --spawn-results-json ...` or `runtime_execute_dispatch.py --action build-patch` logic to obtain the filled patch payload
2. apply the patch via:
   - `roles/orchestrator/pipeline-launch-procedure/initialize/scripts/update_research_run.py`
3. if DB patching fails after spawn succeeds:
   - record this as a failed run for summary purposes
   - preserve returned runtime metadata in the failure record for recovery

### Step 4 — finalize summary

After all launch attempts complete:
- finalize the summary through `run_dispatch_runtime.py --spawn-results-json ...`

Expected overall statuses:
- `launched_all`
- `launched_partial`
- `launch_failed`
- `skipped_all`

## Partial failure rule

If, for example, 3 of 5 runs launch successfully and 2 fail:
- keep the 3 successful runs active
- mark the 2 failed runs as failed launch attempts
- return overall status `launched_partial`
- on retry, re-run the prepare step with fresh idempotency state so only failed/unlaunched runs remain launchable

## Idempotency rule

Before launching a run, check whether that run already has:
- `research_runs.notes.child_session_key`

If present:
- do not relaunch by default
- mark the run `skipped_existing`

## Default runtime profile

Unless explicitly overridden by the planner, the swarm should launch with:
- `model: codex`
- `thinking: medium`

These values should be preserved in the runtime patch notes.

## Can Orchestrator call this end-to-end?

Yes.

The intended model is:
- Orchestrator calls the planner script to produce the manifest
- Orchestrator then runs the runtime harness sequence inside the same OpenClaw session
- the OpenClaw session performs the actual `sessions_spawn` calls
- the OpenClaw session applies the resulting DB patches and obtains the final launch summary

In other words:
- yes, Orchestrator can drive the whole launch end-to-end
- but the OpenClaw tool loop still occurs inside the runtime session, not inside plain Python

## One-line operating model

The runtime harness is a thin executor: validate, prepare, spawn, patch, summarize, and retry only the runs that never acquired a child session key.
