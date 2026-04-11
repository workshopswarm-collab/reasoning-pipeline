# Synthesis Runtime Lane

This folder contains the **runtime-control** half of the synthesis subagent system.

## Canonical truth

Runtime owns everything that happens after synthesis-stage preparation artifacts exist for a dispatch.

## Current responsibilities

- validate stage readiness and sidecar completeness
- maintain `synthesis-stage-status.json` as the explicit stage-state ledger
- kick completed dispatches into synthesis-stage preparation
- enforce single-flight final synthesis launch so only one synthesis topic/executor is created per dispatch
- bootstrap or reuse the dedicated synthesis Telegram topic for the dispatch
- run the synthesis worker/subagent
- validate the worker JSON result
- render `syndicated-finding.md`
- write `syndicated-finding.runtime.json`
- write `decision-handoff.md`
- compute runtime-derived frontmatter/decision fields such as midpoint, edge, relation-to-market, and edge-quality
- apply normalization and repair logic when synthesis output is malformed, incomplete, or partially rendered

## Layout

- `scripts/` — runtime-control helpers

## Important scripts

- `scripts/kickoff_synthesis_after_swarm.py` — build/refresh synthesis-stage artifacts once a dispatch is ready
- `scripts/launch_synthesis_if_ready.py` — guarded single-flight launcher for the dedicated synthesis lane and final executor
- `scripts/bootstrap_synthesis_telegram_lane.py` — create or reuse the dedicated synthesis Telegram topic
- `scripts/run_synthesis_executor.py` — execute final synthesis, validate the model JSON, and render final artifacts
- `scripts/status.py` / `scripts/show_synthesis_stage_status.py` — read the stage ledger
- `scripts/runrepairs/reconcile_synthesis_from_artifacts.py` — infer truth from current stage artifacts/final outputs
- `scripts/runrepairs/finalize_synthesis_after_stage.py` — repair + advance synthesis when the stage is actually ready

## Boundary

Runtime enforces the artifact contract, state ledger, launch safety, and deterministic rendering.
Behavioral instructions belong in the planner prompt/contract layer, not in the runtime implementation itself.
