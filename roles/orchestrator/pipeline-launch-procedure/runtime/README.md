# Runtime Lane

This folder contains the **runtime-control** half of the pipeline launch procedure.

## Purpose

Runtime scripts own execution and lifecycle reconciliation after a dispatch manifest has been prepared.

This includes:
- validating/preparing launchable runs
- delivering research assignments into fixed Discord persona channels
- patching `research_runs` to `running`
- supporting completion reconciliation and run-state helpers
- auto-attempting case/market finalization after terminal run updates
- artifact-vs-DB safety-net reconciliation
- headless TUI -> Discord handoff support
- manifest retention/archive hygiene

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
- `scripts/prepare_headless_discord_dispatch.py`

Visible lane message format expected by the canonical planner handoff:
- `STARTING RESEARCH | market=<market title> | persona=<persona> | research_run_id=<id>`
- `FINISHED RESEARCH | market=<market title> | persona=<persona> | research_run_id=<id> | agent_finding_path=<path>`
- `scripts/list_pending_dispatch_manifests.py`
- `scripts/archive_dispatch_manifests.py`

## Runtime surface

Discord is the intended runtime surface.
The current architecture uses fixed Discord persona channels as the researcher lanes and routes work into them with `sessions_send`.

Important nuance:
- the `sessions_send` handoff is internal session delivery
- it may not itself appear as a visible kickoff post in Discord
- visible lane activity should come from the persona lane after it receives the assignment

The canonical routing map lives in:
- `roles/orchestrator/pipeline-launch-procedure/runtime/persona-channel-map.json`
