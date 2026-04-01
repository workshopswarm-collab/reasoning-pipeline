# Pipeline Launch Procedure

This folder is the launch control-plane for the research swarm.

## Canonical truth

- Runtime surface: **fresh Telegram topics**
- Handoff primitive: `sessions_send`
- Stable completion key: `research_run_id`
- Primary completion path: terminal `update_research_run.py` updates auto-attempt parent finalization
- Manual repair path: `runtime/scripts/finalize_dispatch_after_swarm.py --file <manifest> --apply`

Do **not** treat persistent persona lanes as part of the current model.

## End-to-end flow

1. Planner prepares market/case state, prompts, queued `research_runs`, and a dispatch manifest.
2. Runtime creates/reuses one controller topic plus one fresh persona topic per queued run, then turns the manifest into one `sessions_send` handoff per still-queued persona topic.
3. Successful handoffs patch the matching `research_runs` rows to `running`.
4. Persona topics do the actual research work and, when possible, post visible STARTING/FINISHED lines in Telegram.
5. Persona lanes reconcile completion/failure back into `research_runs`.
6. Runtime sends visible Telegram kickoff posts and internal topic-session handoffs as separate launch actions.
7. Successful completion auto-posts the visible finish marker.
8. Terminal run updates auto-attempt manifest reconciliation.
9. Parent case/market closure happens only when the full swarm has completed cleanly; partial-terminal swarms move to `needs_intervention`.
10. If automatic reconciliation is missed, use the manual finalizer as a repair/backstop step.

## Important nuance

- `sessions_send` confirms **internal OpenClaw session delivery**.
- It does **not** guarantee a visible kickoff post in Telegram.
- Visible topic activity should come from the persona topic after it receives the assignment.

## Folder map

### Planner lane
- `planner/scripts/`
- `planner/prompts/`
- `planner/README.md`

Planner owns deterministic preparation work:
- select market
- open/fetch case
- set market pipeline state
- create queued research runs
- build persona prompts
- emit dispatch manifest

### Runtime lane
- `runtime/scripts/`
- `runtime/dispatch-manifests/`
- `runtime/telegram-runtime-config.json`
- `runtime/README.md`

Runtime owns operational execution work:
- validate manifests
- load current run state for idempotency
- prepare one `sessions_send` handoff per launchable lane
- patch runs to `running` after successful handoff
- reconcile completion/failure state
- auto-finalize parent case/market when all runs are terminal
- provide manual repair helpers and manifest hygiene

## Canonical docs

- `RESEARCH_DISPATCH_SPEC.md` — state model and dispatch contract
- `OPENCLAW_RUNTIME_BRIDGE.md` — planner/runtime boundary
- `RUNTIME_HARNESS_PROCEDURE.md` — exact TUI/runtime handoff loop
- `DISPATCH_LIVE_SWARM.md` — live operator runbook

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
- `runtime/scripts/prepare_headless_telegram_dispatch.py`
- `runtime/scripts/bootstrap_telegram_topics.py`
- `runtime/scripts/list_pending_dispatch_manifests.py`
- `runtime/scripts/archive_dispatch_manifests.py`

## Routing map

Telegram runtime config lives in:
- `runtime/telegram-runtime-config.json`

Current personas:
- `base-rate`
- `market-implied`
- `variant-view`
- `risk-manager`
- `catalyst-hunter`

Each case creates one fresh Telegram topic per persona plus one controller topic.

## Status model

### Market/case level
- `markets.pipeline_status = pending_research` → queued for future work
- `markets.pipeline_status = researching` → active case in flight
- `markets.pipeline_status = closed` → no longer actively in-flight
- `cases.status = open` → case is active
- `cases.status = closed` → case has been finalized

### Run level
- `queued` → row exists, not yet handed off
- `running` → handoff delivered and run started
- `completed` / `failed` → terminal

### Timestamp rule
- `started_at` must reflect actual handoff/start, not row creation

## Safety net

If a lane writes artifacts but fails to reconcile DB state, use:
- `runtime/scripts/reconcile_dispatch_from_artifacts.py`

If you need full manifest-level repair/audit, use:
- `runtime/scripts/finalize_dispatch_after_swarm.py --file <manifest> --apply`

## Headless wrapper

Use:
- `runtime/scripts/prepare_headless_telegram_dispatch.py`
- `runtime/scripts/bootstrap_telegram_topics.py`

They:
1. select/open a case when needed
2. emit the canonical manifest
3. load existing run state for idempotency
4. prepare the runtime bootstrap + handoff plan
5. create or reuse the controller/persona Telegram topics
6. return one ready-to-send `sessions_send` payload per persona topic
7. include an optional manual finalizer backstop command
