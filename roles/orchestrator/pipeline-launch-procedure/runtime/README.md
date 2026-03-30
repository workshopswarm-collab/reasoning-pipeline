# Runtime Lane

This folder contains the **runtime-control** half of the pipeline launch procedure.

## Canonical truth

Runtime owns everything that happens **after** a dispatch manifest has been prepared.

That includes:
- validating/preparing launchable runs
- delivering research assignments into fixed Discord persona channels
- patching `research_runs` to `running`
- reconciling completion/failure back into `research_runs`
- auto-attempting parent case/market finalization after terminal run updates
- providing artifact-vs-DB repair helpers
- supporting headless TUI -> Discord handoff flows
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
- `scripts/prepare_headless_discord_dispatch.py`
- `scripts/list_pending_dispatch_manifests.py`
- `scripts/archive_dispatch_manifests.py`

## Visible lane message format

Expected by the canonical planner handoff:
- `STARTING RESEARCH | market=<market title> | persona=<persona> | research_run_id=<id>`
- `FINISHED RESEARCH | market=<market title> | persona=<persona> | research_run_id=<id> | agent_finding_path=<path>`

These are best-effort lane messages, not transport-level guarantees.

## Runtime surface

Discord is the intended runtime surface.
The current architecture uses fixed Discord persona channels as the researcher lanes and routes work into them with `sessions_send`.

Important nuance:
- the `sessions_send` handoff is internal session delivery
- it may not itself appear as a visible kickoff post in Discord
- visible lane activity should come from the persona lane after it receives the assignment

## Routing map

Canonical routing lives in:
- `roles/orchestrator/pipeline-launch-procedure/runtime/persona-channel-map.json`
