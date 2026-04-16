# Planner Lane

This folder contains the **planner/control-plane** half of the researchers swarm subagents system.

## Canonical truth

Planner owns deterministic local preparation work.
Planner does **not** call OpenClaw runtime tools directly.

Planner is responsible for:
- selecting the next market
- opening/fetching the case
- setting `markets.pipeline_status`
- creating queued `research_runs`
- building persona-specific prompts
- emitting the canonical dispatch manifest

## Layout

- `prompts/` — researcher base contract + persona prompt files
- `scripts/` — planner/control-plane helpers

## Canonical scripts

- `scripts/select_next_market.py`
- `scripts/open_case.py`
- `scripts/set_market_pipeline_status.py`
- `scripts/create_research_run.py`
- `scripts/build_researcher_prompt.py`
- `scripts/generate_qmd_bundle.py`
- `scripts/generate_lmd_bundle.py`
- `scripts/dispatch_case_research.py`
  - supports `--dry-run` to preview rerun/lane/fingerprint behavior without writing DB state or creating run attempts
  - now generates both `qmd-bundle.json` and `lmd-bundle.json` during dispatch preparation
  - `build_researcher_prompt.py` now renders LMD after QMD for treatment-arm bundles and promotes LMD required checks into the case completion checklist
  - `generate_lmd_bundle.py` can now consult `lmd_candidate_stats`, `causal_edge_stats`, and `causal_node_stats` when a DB URL is available; the current Phase 11 slice uses those stats plus live-family crowding / trust-tier signals to order live causal context, exposes explicit score breakdowns in bundle debug output, and now normalizes the learned bonuses against the actual live stats distributions instead of assuming fixed raw score ranges
  - `generate_lmd_bundle.py` now also supports `--phase11-policy-path` and `--phase11-disable-learned-policy` so evaluator-side reporting can compare default normalized priors vs learned overrides on identical case inputs
  - live-graph LMD recall is now lifecycle-aware: `active` items recall by default, while `trial` items only enter explicit treatment / trial modes and are labeled as experimental in prompt rendering
  - blocks reruns on closed cases by default; requires `--allow-closed-case-rerun` to intentionally relaunch historical cases
  - now hardens rerun dispatch preflight with canonical case-artifact integrity checks, compact per-dispatch `gate_status` reporting, and an explicit active-rerun override path (`--allow-active-case-rerun` + `--rerun-override-reason`) instead of silent same-case bypasses

## Boundary

Planner output is the dispatch manifest.
Execution, Telegram topic/session delivery, run-state reconciliation, lifecycle posting, and finalization belong to the sibling `../runtime/` lane.
