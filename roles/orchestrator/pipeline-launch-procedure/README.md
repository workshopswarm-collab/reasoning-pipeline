# Pipeline Launch Procedure

This folder contains the launch control-plane for starting research-swarm case work from the Orchestrator side.

It bridges:
- market/case state in Postgres
- prompt generation and run planning in local scripts
- actual `sessions_spawn` calls in the OpenClaw runtime
- DB status reconciliation after spawn and completion

## What this folder is for

Use this folder when you want to:
- select the next market for research
- open or fetch a case
- create research run records
- generate persona-specific prompts
- build a dispatch manifest
- launch the swarm through a runtime controller session
- patch returned runtime metadata into `research_runs`
- reconcile child completion events back into Postgres
- summarize launch and completion outcomes

This folder is the **launch procedure** for getting the research swarm into motion cleanly and keeping runtime state aligned with DB state.

---

# Mental model

The system has three layers.

## 1. Planner / control-plane layer
Handled by Python scripts.

It does the deterministic local work:
- market selection
- case creation
- run creation
- prompt assembly
- artifact path planning
- dispatch manifest emission

## 2. Runtime controller layer
Handled inside a dispatch-bounded OpenClaw runtime session.

It does the operational runtime work:
- validating the manifest
- determining launchable vs skipped runs
- calling `sessions_spawn`
- patching runs to `running`
- reconciling child completion events to `completed` or `failed`
- summarizing launch/completion state back to Orchestrator

## 3. Research worker layer
Handled by child researcher subagent sessions.

It does the actual case research and artifact creation.

Core rule:
- **Python prepares**
- **Runtime controller launches and reconciles**
- **Research workers research**

---

# Key documents

### `RESEARCH_DISPATCH_SPEC.md`
High-level operating contract for case research.
Defines personas, required outputs, state model, and the role of vault + Postgres.

### `OPENCLAW_RUNTIME_BRIDGE.md`
Architecture boundary between local scripts and the OpenClaw runtime.

### `DISPATCH_LIVE_SWARM.md`
Live procedure for launching the swarm.

### `RUNTIME_HARNESS_PROCEDURE.md`
Exact runtime launch/reconciliation procedure.

### `SWARM_RUNTIME_CONTROLLER_SPEC.md`
Defines the dispatch-bounded runtime controller session, including lifecycle, edge cases, and message contract.

### `RUNTIME_CONTROLLER_PROMPT.md`
Minimal instruction block for spawning a runtime controller session.

---

# Script map

All scripts live in:
- `roles/orchestrator/pipeline-launch-procedure/initialize/scripts/`

## Planner/control-plane
- `select_next_market.py` — select one eligible market
- `open_case.py` — fetch or create the case record
- `set_market_pipeline_status.py` — update `markets.pipeline_status`
- `create_research_run.py` — create one `research_runs` row per persona
- `build_researcher_prompt.py` — generate the exact prompt for one persona on one case
- `dispatch_case_research.py` — create runs, build prompts, emit the canonical dispatch manifest

Important defaults in `dispatch_case_research.py`:
- model defaults to `openai-codex/gpt-5.4`
- thinking defaults to `medium`

## Runtime-control helpers
- `runtime_execute_dispatch.py` — validate manifest, prepare launchable/skipped runs, build post-spawn patches, finalize summaries
- `run_dispatch_runtime.py` — runtime orchestration wrapper around the launch flow
- `update_research_run.py` — patch one `research_runs` row
- `reconcile_research_run_completion.py` — reconcile a completion event back into `research_runs` by `notes.child_session_key`

---

# Process walkthrough

## Phase 1 — planner preparation
1. `select_next_market.py`
2. `open_case.py`
3. `dispatch_case_research.py --case-id <case_id>`

Output:
- canonical dispatch manifest

## Phase 2 — runtime control
4. Orchestrator spawns a **dispatch-bounded runtime controller session** using `RUNTIME_CONTROLLER_PROMPT.md`
5. The controller validates and prepares the launch plan with `run_dispatch_runtime.py`
6. The controller calls `sessions_spawn` for each launchable run
7. After each successful spawn, the controller patches the DB row to `running`
8. On child completion events, the controller reconciles rows to `completed` or `failed`
9. The controller sends launch/final summaries back to Orchestrator and exits only after all tracked child runs are terminal and reconciled

---

# Status model

## `markets.pipeline_status`
- `new`
- `pending_research`
- `researching`
- `ignored`
- `executed`
- `closed`

## `research_runs.status`
- `queued`
- `running`
- `completed`
- `failed`
- `canceled`

Canonical join key between runtime events and DB rows:
- `research_runs.notes.child_session_key`

---

# Partial failures and retries

If some runs launch successfully and others fail:
- patch successful runs to `running`
- keep them active
- return `launched_partial`
- retry only runs that still lack `notes.child_session_key`

If completion reconciliation fails:
- preserve recovery data
- do not silently drop the event
- retry reconciliation before considering the dispatch cleanly finished

---

# End-to-end ownership

## Orchestrator owns
- market selection
- case opening
- manifest generation
- strategic supervision
- synthesis

## Runtime controller owns
- swarm launch
- spawn-time DB patching
- completion-time DB reconciliation
- launch/final summaries
- exit after reconciliation

## Research workers own
- research
- qualitative artifact creation
- persona-specific analysis

---

# One-line summary

This folder contains the launch control-plane for the research swarm: planner scripts prepare the manifest, a dispatch-bounded runtime controller session launches and reconciles the swarm, research workers create the artifacts, and helper scripts keep Postgres state aligned with real runtime state.
