# OpenClaw Runtime Bridge

This document defines the boundary between the local Python/Postgres control-plane scripts and the OpenClaw agent runtime.

## Why this bridge exists

`dispatch_case_research.py` can do all local work that only needs:
- Python
- PostgreSQL
- prompt assembly

It cannot directly call `sessions_spawn`, because `sessions_spawn` is an OpenClaw runtime tool, not a subprocess-available Python API.

That boundary is normal and should stay explicit.

## Recommended architecture

Treat dispatch as a **two-phase operation**.

### Phase 1 — local control-plane preparation
Owned by Python scripts in:
- `roles/orchestrator/pipeline-launch-procedure/initialize/scripts/`

Responsibilities:
1. select/open the case
2. set `markets.pipeline_status`
3. create one `research_runs` row per persona
4. build the exact researcher prompt text
5. emit a runtime dispatch manifest

Primary script:
- `dispatch_case_research.py`

### Phase 2 — OpenClaw runtime execution
Owned by the Orchestrator agent runtime.

Responsibilities:
1. iterate through the emitted run manifest
2. call `sessions_spawn` with each `spawn_payload`
3. capture returned subagent session metadata
4. patch the matching `research_runs` row using `update_research_run.py`
5. mark the run `running`

## Canonical runtime loop

The recommended runtime loop now runs through the thin wrapper:
- `roles/orchestrator/pipeline-launch-procedure/initialize/scripts/run_dispatch_runtime.py`

That wrapper uses:
- `runtime_execute_dispatch.py --action validate`
- `runtime_execute_dispatch.py --action prepare`
- `runtime_execute_dispatch.py --action build-patch`
- `runtime_execute_dispatch.py --action finalize-summary`

For each launchable run returned by the prepare step:

1. call `sessions_spawn` with:
   - `launchable_runs[i].spawn_payload`
2. capture returned metadata from the spawn result
3. build the filled DB patch payload for:
   - `launchable_runs[i].research_run_id`
4. fill these fields from the actual spawn result when available:
   - `notes.child_session_key`
   - `notes.spawn_run_id`
5. keep `workspace_note_path` equal to the planned primary artifact path
6. apply the patch through `update_research_run.py`
7. record a per-run launch result for final summary generation

If some runs launch and others fail:
- keep successful launches active
- return `launched_partial`
- retry only runs that still lack `notes.child_session_key`

## Why this pattern is recommended

This split preserves:
- **provenance** — Postgres preparation is explicit and inspectable
- **predictable behavior** — the spawn payload is generated once and executed literally
- **guardrails** — the runtime performs only the prepared spawn + patch steps

It also avoids faking OpenClaw tool calls from local subprocesses.

## Non-goal

Do not try to make local Python scripts call OpenClaw runtime tools directly unless OpenClaw later exposes an official supported local API for that purpose.

For now, the correct boundary is:
- Python scripts prepare
- OpenClaw agent runtime spawns
- Python scripts patch DB state

## One-line operating model

`dispatch_case_research.py` is the dispatch planner; the Orchestrator runtime is the dispatch executor.