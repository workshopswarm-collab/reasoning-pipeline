# OpenClaw Runtime Bridge

This document defines the boundary between the local Python/Postgres control-plane scripts and the OpenClaw agent runtime.

## Why this bridge exists

`dispatch_case_research.py` can do all local work that only needs:
- Python
- PostgreSQL
- prompt assembly

But it cannot directly call `sessions_spawn`, because `sessions_spawn` is an OpenClaw runtime tool, not a subprocess-available Python API.

That split is normal.
It should be made explicit rather than hidden.

## Recommended architecture

Treat dispatch as a **two-phase operation**:

### Phase 1 — local control-plane preparation
Owned by Python scripts in:
- `roles/orchestrator/research-pipeline/initialize/scripts/`

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

For each run returned by `dispatch_case_research.py`:

1. call `sessions_spawn` with:
   - `runs[i].spawn.spawn_payload`
2. capture returned metadata from the spawn result
3. patch the DB row referenced by:
   - `runs[i].spawn.post_spawn_update_template.research_run_id`
4. fill these fields from the actual spawn result when available:
   - `notes.child_session_key`
   - `notes.spawn_run_id`
5. keep `workspace_note_path` equal to the planned primary artifact path
6. set `research_runs.status = running`

## Why this is the recommended pattern

This split preserves:
- **provenance** — Postgres preparation is explicit and inspectable
- **predictable behavior** — the spawn payload is generated once and then executed literally
- **guardrails** — the runtime only performs the exact spawn + patch steps on top of an already prepared plan

It also avoids trying to fake OpenClaw tool calls from local subprocesses.

## Non-goal

Do not try to make local Python scripts call OpenClaw runtime tools directly unless OpenClaw later exposes an official supported local API for that purpose.

For now, the correct boundary is:
- Python scripts prepare
- OpenClaw agent runtime spawns
- Python scripts patch DB state

## One-line operating model

`dispatch_case_research.py` is the dispatch planner; the Orchestrator runtime is the dispatch executor.