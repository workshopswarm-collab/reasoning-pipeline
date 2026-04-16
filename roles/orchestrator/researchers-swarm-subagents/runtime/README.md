# Runtime Lane

This folder contains the **runtime-control** half of the researchers swarm subagents system.

## Canonical truth

Runtime owns everything that happens **after** a dispatch manifest has been prepared.

That includes:
- validating/preparing launchable runs
- creating/reusing Telegram controller/persona topics and materializing their canonical session keys
- delivering research assignments into those topic sessions
- patching `research_runs` to `running`
- auto-posting visible `STARTING RESEARCH` markers on successful start transitions
- reconciling completion/failure back into `research_runs`
- auto-posting visible completion markers on successful completion
- auto-attempting dispatch finalization only when the active dispatch is actually terminal
- kicking completed dispatches into synthesis-stage preparation and launch
- supervising active Telegram runs with the runtime loop/watchdog
- providing artifact-vs-DB repair helpers
- supporting headless TUI -> Telegram handoff flows
- keeping the active manifest queue tidy

## Layout

- `scripts/` — runtime-control helpers
- `dispatch-manifests/` — active manifest queue/history and archive tree

## Runtime scripts

- `scripts/internal/load_dispatch_existing_state.py`
- `scripts/internal/runtime_execute_dispatch.py`
- `scripts/internal/run_dispatch_runtime.py`
- `scripts/update_research_run.py`
- `scripts/internal/auto_finalize_case_after_terminal_run.py`
- `scripts/reconcile_research_run_completion.py`
- `scripts/runrepairs/reconcile_dispatch_from_artifacts.py`
- `scripts/runrepairs/finalize_dispatch_after_swarm.py`
- `scripts/prepare_headless_telegram_dispatch.py`
- `scripts/internal/bootstrap_telegram_topics.py`
- `scripts/internal/telegram_topic_create.py`
- `scripts/internal/watchdog_telegram_swarm_runs.py`
  - checks running Telegram-forum lanes for completion candidates, stalls, and hard failures
  - with `--apply-completions`, auto-reconciles stale `running` rows when the assigned primary artifact exists and has gone idle past the completion grace window
- `scripts/run_telegram_swarm_runtime_loop.py`
  - periodic runtime loop around the internal watchdog
  - auto-completes stale finished lanes, sends internal nudges through `sessions.send`, and can optionally fail hard-stalled runs
  - exits automatically when there are no active `running` Telegram swarm lanes left (unless explicitly kept alive)
  - runs quietly in the background by default; routine stdout/stderr is suppressed and only errors are written to `.runtime-state/telegram_swarm_runtime_loop.error.json`
- `scripts/runrepairs/list_pending_dispatch_manifests.py`
- `scripts/runrepairs/archive_dispatch_manifests.py`

## Visible lane message format

Expected by the canonical planner handoff:
- `STARTING RESEARCH | market=<market title> | persona=<persona> | research_run_id=<id>`
- `FINISHED RESEARCH | market=<market title> | persona=<persona> | research_run_id=<id> | agent_finding_path=<path>`

Lifecycle rule:
- start marker should be posted automatically when a run is patched from `queued` to `running`
- finish marker should be posted automatically when a run is patched to `completed`
- visible lifecycle posts should be idempotent and keyed off stored delivery metadata in `research_runs.notes`
- the preferred launch wrapper is `runtime/scripts/launch_dispatch_with_stateful_posts.py`, which bootstraps topics, delivers handoffs via `runtime/scripts/internal/openclaw_sessions_send.mjs`, immediately patches successful deliveries to `running`, lets `update_research_run.py` post visible start markers automatically, ensures the Telegram swarm runtime loop is running once research begins, logs dispatch-level proposed-causal shadow matches once per dispatch when an `lmd-bundle.json` includes `shadow_evaluation`, logs dispatch-level proposed-causal trial exposures once per dispatch when an `lmd-bundle.json` includes `trial_overlay.selected_candidates` (including whether the overlay was preview-only or treatment-injected), logs learning-intervention applications when the run notes include intervention metadata, and logs LMD bundle exposures when the run notes indicate an active injected `lmd-bundle.json` (`lmd_used=true`)
- `runtime/scripts/internal/openclaw_sessions_send.mjs` uses the confirmed Gateway RPC method `sessions.send` through OpenClaw's bundled Gateway client helper, so no manual CLI bridge input is required
- persona handoffs should include an exact terminal-state helper command using `runtime/scripts/reconcile_research_run_completion.py`; do not rely on vague references like "runtime DB helper"

## Runtime surface

Telegram forum topics are the intended runtime surface.
The current architecture uses one controller topic per case and one persona topic per persona per case for the researcher swarm. Once the swarm is truly terminal, synthesis promotion creates one dedicated synthesis topic for that dispatch. Research and synthesis lanes are both delivered through canonical topic sessions with `sessions.send`, but synthesis launch is guarded as a single-flight action so only one process can create/use the synthesis topic for a dispatch.

Operational helpers now include:
- `scripts/sweep_orphaned_research_runs.py` for stale queued / stranded researching-case repair
- `scripts/pipeline_anomaly_report.py` for read-only anomaly counts before or during automation
- `scripts/prepare_and_launch_headless_telegram_dispatch.py` for the safe combined prepare→launch headless path without brittle ad hoc manifest parsing

Important nuance:
- the `sessions.send` handoff is internal session delivery into the canonical topic session
- it may not itself appear as a visible kickoff post in Telegram
- visible `STARTING RESEARCH` / `FINISHED RESEARCH` lines are emitted by `update_research_run.py` on state transitions
- visible lane activity after that is optional progress chatter from the persona topic

## Routing/config

Canonical runtime config lives in:
- `roles/orchestrator/researchers-swarm-subagents/runtime/telegram-runtime-config.json`

## Canonical headless operational path

For normal live automation, prefer:
- `scripts/prepare_and_launch_headless_telegram_dispatch.py`

This is the canonical combined **prepare -> launch** entrypoint.
It safely sequences:
1. planner/runtime preparation
2. a dry-run planner preflight to catch prompt/planner regressions before live DB mutation
3. manifest resolution
4. live launch through `launch_dispatch_with_stateful_posts.py`

For manual debugging/control without enabling unattended automation, use:
- `scripts/manual_batch_controller.py`

This exposes explicit subcommands such as:
- `status`
- `select-next`
- `launch-next`
- `launch-case --case-id <uuid>`
- `launch-market --market-id <market-uuid>`
- `inspect-case --case-ref <uuid|case-key>`
- `repair-preview`
- `repair-apply`

Lower-level scripts remain available for debugging, inspection, or repair:
- `scripts/prepare_headless_telegram_dispatch.py` = prepare only, no launch
- `scripts/launch_dispatch_with_stateful_posts.py` = launch an already-prepared manifest
