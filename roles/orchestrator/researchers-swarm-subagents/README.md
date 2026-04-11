# Researchers Swarm Subagents

This folder is the launch control-plane for the researcher swarm subagents.

## Canonical truth

- Runtime surface: **Telegram forum topics**
- Research-swarm lane pattern: one controller topic per case plus one persona topic per persona per case
- Post-swarm synthesis pattern: once the active dispatch is truly terminal, promote into **one dedicated synthesis topic per dispatch**
- Handoff primitive: Gateway RPC `sessions.send` (normally invoked through the runtime bridge/helper)
- Stable completion key: `research_run_id`
- Lifecycle owner for visible STARTING/FINISHED researcher markers: `runtime/scripts/update_research_run.py`
- Runtime supervision path: `runtime/scripts/run_telegram_swarm_runtime_loop.py`
- Automatic terminal promotion path: terminal researcher completion updates -> guarded parent finalization -> manifest finalizer -> synthesis kickoff -> single-flight synthesis launch
- Manual repair path: `runtime/scripts/runrepairs/finalize_dispatch_after_swarm.py --file <manifest> --apply`

## End-to-end flow

1. Planner prepares market/case state, prompts, queued `research_runs`, and a dispatch manifest.
2. Runtime creates/reuses one controller topic plus one persona topic per case/persona lane, materializes the corresponding topic sessions, and turns the manifest into one `sessions.send` handoff per still-queued persona attempt.
3. Successful handoffs patch the matching `research_runs` rows to `running`.
4. `update_research_run.py` treats that `queued -> running` patch as the canonical start transition and auto-posts the visible `STARTING RESEARCH` marker in Telegram.
5. Persona topics do the actual research work and may post sparse progress updates in-topic when useful.
6. Completion/failure reconciles back into `research_runs` by `research_run_id`, either from the lane helper or from the runtime watchdog/loop.
7. `update_research_run.py` treats the `running -> completed` patch as the canonical finish transition and auto-posts the visible `FINISHED RESEARCH` marker.
8. Terminal run updates auto-attempt dispatch-level finalization only once the active dispatch is actually terminal (`queued == 0` and `running == 0`), which reduces pre-terminal fan-out.
9. Once the swarm is fully completed, the manifest finalizer kicks off synthesis-stage preparation and then hands the status file into the synthesis launcher.
10. The synthesis launcher uses a single-flight claim so only one process can create/use the dedicated synthesis topic and spawn the final synthesis executor for that dispatch.
11. Parent case/market closure happens only when the full swarm has completed cleanly; partial-terminal swarms move to `needs_intervention`.
12. The Telegram swarm runtime loop supervises active `running` lanes, auto-completes stale finished work, sends nudges when needed, and exits automatically once the swarm is done.
13. If automatic reconciliation is missed, use the manual finalizer as a repair/backstop step.

## Important nuance

- `sessions.send` confirms **internal OpenClaw session delivery** into the canonical topic session.
- Visible `STARTING RESEARCH` / `FINISHED RESEARCH` lines are emitted by `update_research_run.py` on state transitions, not as a separate manual kickoff path.
- Persona topics may still post sparse progress updates after assignment receipt, but lifecycle markers are now state-driven.

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
- materialize Telegram topic sessions and deliver one `sessions.send` handoff per launchable lane
- patch runs to `running` after successful handoff
- reconcile completion/failure state
- auto-attempt dispatch finalization only when the active dispatch is terminal
- promote completed dispatches into synthesis-stage preparation and single-flight final synthesis launch
- auto-finalize parent case/market when all runs are terminal and clean
- provide runtime-loop supervision, manual repair helpers, and manifest hygiene

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

### Runtime (preferred operator path)
- `runtime/scripts/prepare_and_launch_headless_telegram_dispatch.py`
- `runtime/scripts/manual_batch_controller.py`
- `runtime/scripts/run_telegram_swarm_runtime_loop.py`
- `runtime/scripts/update_research_run.py`
- `runtime/scripts/reconcile_research_run_completion.py`

### Runtime (lower-level / repair helpers)
- `runtime/scripts/prepare_headless_telegram_dispatch.py`
- `runtime/scripts/launch_dispatch_with_stateful_posts.py`
- `runtime/scripts/internal/openclaw_sessions_send.mjs`
- `runtime/scripts/internal/auto_finalize_case_after_terminal_run.py`
- `runtime/scripts/internal/load_dispatch_existing_state.py`
- `runtime/scripts/internal/run_dispatch_runtime.py`
- `runtime/scripts/internal/runtime_execute_dispatch.py`
- `runtime/scripts/internal/bootstrap_telegram_topics.py`
- `runtime/scripts/internal/telegram_topic_create.py`
- `runtime/scripts/internal/watchdog_telegram_swarm_runs.py`
- `runtime/scripts/runrepairs/reconcile_dispatch_from_artifacts.py`
- `runtime/scripts/runrepairs/finalize_dispatch_after_swarm.py`
- `runtime/scripts/runrepairs/list_pending_dispatch_manifests.py`
- `runtime/scripts/runrepairs/archive_dispatch_manifests.py`

## Routing map

Telegram runtime config lives in:
- `runtime/telegram-runtime-config.json`

Current personas:
- `base-rate`
- `market-implied`
- `variant-view`
- `risk-manager`
- `catalyst-hunter`

Each case creates one controller topic plus one persona topic per persona lane.

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
- `runtime/scripts/runrepairs/reconcile_dispatch_from_artifacts.py`

If you need full manifest-level repair/audit, use:
- `runtime/scripts/runrepairs/finalize_dispatch_after_swarm.py --file <manifest> --apply`

## Headless wrapper

Preferred headless path:
- `runtime/scripts/prepare_and_launch_headless_telegram_dispatch.py`

That path:
1. selects/opens a case when needed
2. emits the canonical manifest
3. resolves the manifest from prepare output or dispatch id
4. bootstraps or reuses the controller/persona Telegram topics through internal helpers
5. materializes topic sessions and delivers the handoff payloads
6. patches successful deliveries to `running`
7. auto-posts visible `STARTING RESEARCH` markers through `update_research_run.py`
8. ensures the runtime loop is running once research begins

Use the lower-level two-step path only when you intentionally want to inspect or repair the prepared manifest before launch:
- `runtime/scripts/prepare_headless_telegram_dispatch.py`
- `runtime/scripts/launch_dispatch_with_stateful_posts.py`

Lower-level bootstrap-only step (debugging / repair use):
- `runtime/scripts/internal/bootstrap_telegram_topics.py`

## Canonical live prepare/launch path

For headless live operation, the default combined entrypoint is:
- `runtime/scripts/prepare_and_launch_headless_telegram_dispatch.py`

Treat this as the normal automation-facing **prepare + launch** step.
Treat `runtime/scripts/prepare_headless_telegram_dispatch.py` and `runtime/scripts/launch_dispatch_with_stateful_posts.py` as lower-level building blocks and debugging/repair tools.

For manual stepwise operation before enabling unattended automation, use:
- `runtime/scripts/manual_batch_controller.py`

That harness keeps the current architecture but gives an explicit control loop surface without turning the pipeline into a daemon or cron-driven service.
