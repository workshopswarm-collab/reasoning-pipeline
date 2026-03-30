# Pipeline Launch Procedure

This folder contains the launch control-plane for the research swarm.

## Current architecture

The canonical runtime surface is now **fixed Discord persona channels**, not auto-created Discord threads.

The flow is:
1. planner scripts prepare the case, prompts, `research_runs`, and manifest
2. runtime helpers turn that manifest into one `sessions_send` handoff per persona channel
3. TUI/main runtime delivers those handoffs into the mapped Discord sessions
4. successful handoffs patch the corresponding `research_runs` rows to `running`
5. persona lanes do the actual research work, post visible STARTING/FINISHED updates in their Discord channels when possible, and later mark runs `completed` / `failed`
6. terminal run updates now auto-attempt the standard finalizer and close the parent case/market when the swarm becomes fully terminal; the manual finalizer remains the safety-net backstop if reconciliation is missed

Important nuance:
- the `sessions_send` handoff itself is an internal OpenClaw session delivery, not a guaranteed visible kickoff post in the Discord channel
- visible lane activity should come from the persona lane after it receives the assignment

## Folder map

### Planner lane
- `planner/scripts/`
- `planner/prompts/`
- `planner/README.md`

Planner owns deterministic preparation work:
- select market
- open case
- set market status
- create queued research runs
- build persona prompts
- emit dispatch manifest

### Runtime lane
- `runtime/scripts/`
- `runtime/dispatch-manifests/`
- `runtime/persona-channel-map.json`
- `runtime/README.md`

Runtime owns operational delivery work:
- validate manifest
- load existing run state for idempotency
- prepare one `sessions_send` handoff per persona lane
- patch runs to `running` after successful handoff
- support completion-state helpers and manifest hygiene

## Canonical docs

- `RESEARCH_DISPATCH_SPEC.md` — dispatch/state contract for the fixed-channel model
- `OPENCLAW_RUNTIME_BRIDGE.md` — planner/runtime boundary for fixed-channel handoff
- `RUNTIME_HARNESS_PROCEDURE.md` — exact TUI/runtime handoff loop
- `DISPATCH_LIVE_SWARM.md` — operator runbook for live launches

## Canonical scripts

### Planner
- `planner/scripts/select_next_market.py`
- `planner/scripts/open_case.py`
- `planner/scripts/set_market_pipeline_status.py`
- `planner/scripts/create_research_run.py`
- `planner/scripts/build_researcher_prompt.py`
- `planner/scripts/dispatch_case_research.py`

### Runtime
- `runtime/scripts/load_dispatch_existing_state.py`
- `runtime/scripts/run_dispatch_runtime.py`
- `runtime/scripts/runtime_execute_dispatch.py`
- `runtime/scripts/update_research_run.py`
- `runtime/scripts/auto_finalize_case_after_terminal_run.py`
- `runtime/scripts/reconcile_research_run_completion.py`
- `runtime/scripts/reconcile_dispatch_from_artifacts.py`
- `runtime/scripts/finalize_dispatch_after_swarm.py`
- `runtime/scripts/prepare_headless_discord_dispatch.py`
- `runtime/scripts/list_pending_dispatch_manifests.py`
- `runtime/scripts/archive_dispatch_manifests.py`

## Runtime routing map

Fixed persona-channel routing lives in:
- `runtime/persona-channel-map.json`

Current personas:
- `base-rate`
- `market-implied`
- `variant-view`
- `risk-manager`
- `catalyst-hunter`

Each persona maps to one Discord channel session key.

## Status model

### Market level
- `pending_research` → queued for future work
- `researching` → active case in flight
- `closed` → no longer actively in-flight in the pipeline

### Run level
- `queued` → row created, not yet handed off
- `running` → handoff delivered to the persona channel and run started
- `completed` / `failed` → terminal

Important note:
- `started_at` should reflect the actual handoff/start transition, not row creation time
- if a lane writes its agent-finding artifact but fails to update the DB, use `runtime/scripts/reconcile_dispatch_from_artifacts.py` as the safety-net reconciler

## Headless TUI wrapper

Use:
- `runtime/scripts/prepare_headless_discord_dispatch.py`

It:
1. selects/open cases when needed
2. emits the canonical manifest
3. loads existing run state for idempotency
4. prepares the runtime handoff plan
5. returns one ready-to-send `sessions_send` step per persona lane

