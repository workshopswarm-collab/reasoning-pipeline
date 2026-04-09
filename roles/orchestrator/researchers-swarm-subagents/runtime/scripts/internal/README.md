# internal/ - Runtime plumbing

These scripts are part of the runtime implementation, but they are **not** the preferred operator-facing entrypoints.

## What belongs here

Lower-level pieces such as:
- topic bootstrap/materialization
- Gateway/session delivery bridge helpers
- DB state loading for idempotency
- runtime patch-building/replay helpers
- watchdog engine internals
- automatic parent finalization hooks

## Operator rule

Prefer using the top-level runtime scripts instead:
- `../prepare_headless_telegram_dispatch.py`
- `../launch_dispatch_with_stateful_posts.py`
- `../run_telegram_swarm_runtime_loop.py`
- `../update_research_run.py`
- `../reconcile_research_run_completion.py`

Reach into `internal/` only when:
- debugging the runtime
- testing a lower-level helper directly
- repairing a broken assumption in the launcher/loop path

## Current scripts

- `bootstrap_telegram_topics.py` — create/reuse Telegram topics and resolve topic/session metadata
- `load_dispatch_existing_state.py` — load current DB state for manifest idempotency/replay
- `openclaw_sessions_send.mjs` — materialize topic sessions and deliver via Gateway `sessions.send`
- `runtime_execute_dispatch.py` — internal planning/patch-building helper
- `run_dispatch_runtime.py` — legacy/low-level orchestration planning/replay helper
- `telegram_topic_create.py` — Telegram provider topic-create wrapper
- `watchdog_telegram_swarm_runs.py` — watchdog engine for completion/nudge/fail candidate detection
- `auto_finalize_case_after_terminal_run.py` — automatic parent-case/market finalization hook

## Design note

If a script here becomes part of the normal human/operator workflow, consider promoting it back to the top-level `scripts/` surface.
