# Planner Lane

This folder contains the **planner/control-plane** half of the pipeline launch procedure.

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
- `scripts/dispatch_case_research.py`

## Boundary

Planner output is the dispatch manifest.
Execution, Telegram topic/session delivery, run-state reconciliation, lifecycle posting, and finalization belong to the sibling `../runtime/` lane.
