# Planner Lane

This folder contains the **planner/control-plane** half of the pipeline launch procedure.

## Purpose

Planner scripts do deterministic local preparation work:
- select the next market
- open or fetch the case
- set `markets.pipeline_status`
- create queued `research_runs`
- build persona-specific prompts
- emit the canonical dispatch manifest

Planner scripts do **not** call OpenClaw runtime tools directly.

## Layout

- `prompts/` — researcher base contract + persona prompt files
- `scripts/` — planner/control-plane helpers

## Canonical scripts

- `scripts/select_next_market.py`
- `scripts/open_case.py`
- `scripts/set_market_pipeline_status.py`
- `scripts/create_research_run.py`
- `scripts/build_researcher_prompt.py`
- `scripts/dispatch_case_research.py`

## Boundary

Planner output is the dispatch manifest.
Execution, channel handoff, and runtime-state reconciliation belong to the sibling `../runtime/` lane.
