# Runtime Lane

This folder contains the **runtime-control** half of the pipeline launch procedure.

## Canonical truth

Runtime owns everything that happens **after** a dispatch manifest has been prepared.

That includes:
- validating/preparing launchable runs
- delivering research assignments into fresh Telegram topics
- emitting visible Telegram kickoff sends alongside internal handoffs
- patching `research_runs` to `running`
- reconciling completion/failure back into `research_runs`
- auto-posting visible completion markers on successful completion
- auto-attempting parent case/market finalization after terminal run updates
- emitting watchdog diagnostics for stalled Telegram runs
- providing artifact-vs-DB repair helpers
- supporting headless TUI -> Telegram handoff flows
- keeping the active manifest queue tidy

## Layout

- `scripts/` — runtime-control helpers
- `dispatch-manifests/` — active manifest queue/history and archive tree

## Canonical scripts

- `scripts/load_dispatch_existing_state.py`
- `scripts/runtime_execute_dispatch.py`
- `scripts/run_dispatch_runtime.py`
- `scripts/update_research_run.py`
- `scripts/auto_finalize_case_after_terminal_run.py`
- `scripts/reconcile_research_run_completion.py`
- `scripts/reconcile_dispatch_from_artifacts.py`
- `scripts/finalize_dispatch_after_swarm.py`
- `scripts/prepare_headless_telegram_dispatch.py`
- `scripts/bootstrap_telegram_topics.py`
- `scripts/telegram_topic_create.py`
- `scripts/watchdog_telegram_swarm_runs.py`
- `scripts/list_pending_dispatch_manifests.py`
- `scripts/archive_dispatch_manifests.py`

## Visible lane message format

Expected by the canonical planner handoff:
- `STARTING RESEARCH | market=<market title> | persona=<persona> | research_run_id=<id>`
- `FINISHED RESEARCH | market=<market title> | persona=<persona> | research_run_id=<id> | agent_finding_path=<path>`

These are best-effort lane messages, not transport-level guarantees.

## Runtime surface

Telegram forum topics are the intended runtime surface.
The current architecture creates one fresh controller topic per case and one fresh persona topic per persona per case, then routes work into those topic sessions with `sessions_send`.

Important nuance:
- the `sessions_send` handoff is internal session delivery
- it may not itself appear as a visible kickoff post in Telegram
- visible lane activity should come from the persona topic after it receives the assignment

## Routing/config

Canonical runtime config lives in:
- `roles/orchestrator/pipeline-launch-procedure/runtime/telegram-runtime-config.json`
