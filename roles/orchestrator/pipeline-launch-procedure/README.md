# Pipeline Launch Procedure

This folder contains the **launch control-plane** for starting research-swarm case work from the Orchestrator side.

It is the operational bridge between:
- market/case state in Postgres
- prompt generation and run planning in local scripts
- actual `sessions_spawn` calls in the OpenClaw runtime
- DB patching and launch summaries after runtime execution

## What this folder is for

Use this folder when you want to:
- select the next market for research
- open or fetch a case
- create research run records
- generate persona-specific prompts
- build a dispatch manifest
- execute the runtime launch loop
- patch returned runtime metadata into `research_runs`
- summarize launch outcomes, including partial failures

This folder is **not** the full prediction workflow.
It is specifically the **launch procedure** for getting the research swarm into motion cleanly.

---

# Mental model

The launch system is split into two halves.

## 1. Planner / control-plane half
Handled by Python scripts.

This half does everything that is deterministic and local:
- market selection
- case creation
- run creation
- prompt assembly
- artifact path planning
- dispatch manifest emission

## 2. Runtime execution half
Handled inside the OpenClaw runtime session.

This half does the work that requires OpenClaw tools:
- validating the manifest for launch
- determining launchable vs skipped runs
- calling `sessions_spawn`
- capturing returned runtime metadata
- patching `research_runs`
- finalizing the launch summary

The key rule:
- **Python prepares**
- **OpenClaw runtime spawns**
- **Python patch helpers normalize and summarize**

---

# Folder map

## Top-level docs

### `README.md`
This file.
Explains the full launch process and each script's role.

### `RESEARCH_DISPATCH_SPEC.md`
High-level operating contract for case research.
Defines:
- persona philosophy
- run expectations
- required outputs
- state model
- how vault artifacts and Postgres work together

### `OPENCLAW_RUNTIME_BRIDGE.md`
Defines the architectural boundary between local scripts and the OpenClaw runtime.

### `DISPATCH_LIVE_SWARM.md`
Live procedure for launching the real swarm.

### `RUNTIME_HARNESS_PROCEDURE.md`
Explains the thin runtime harness flow and partial-failure handling.

---

# Script map

All scripts live in:
- `roles/orchestrator/pipeline-launch-procedure/initialize/scripts/`

## `select_next_market.py`
Purpose:
- select the next market eligible for orchestrator processing

What it does:
- looks for markets in `new` or `pending_research`
- skips markets that already have an open case
- returns one selected market

Use when:
- you want the next candidate market from the queue

---

## `open_case.py`
Purpose:
- fetch or create the case record for one market

What it does:
- accepts either `market_id` or `(platform, external_market_id)`
- returns an existing open case if present
- otherwise creates a new one

Use when:
- a selected market needs to become an orchestrated case

---

## `set_market_pipeline_status.py`
Purpose:
- update `markets.pipeline_status`

What it does:
- changes one market's status such as `new -> researching`

Use when:
- dispatch begins or other pipeline state changes are needed

---

## `create_research_run.py`
Purpose:
- create one `research_runs` row for a persona on a case

What it does:
- inserts a queued run row
- records the persona, runtime label, artifact path, and notes

Use when:
- planner is creating the swarm run records before launch

---

## `build_researcher_prompt.py`
Purpose:
- generate the exact dispatch prompt for one persona on one case

What it does:
- reads the base contract prompt
- reads the persona prompt
- combines them with current case/market context
- encodes artifact path rules directly into the prompt

Use when:
- planner needs the literal `task` string for `sessions_spawn`

---

## `dispatch_case_research.py`
Purpose:
- planner / manifest emitter

What it does:
- loads case + market context
- sets `pipeline_status = researching`
- creates one run per persona
- builds one prompt per persona
- emits the canonical dispatch manifest

Important defaults:
- model defaults to `codex`
- thinking defaults to `medium`

Use when:
- preparing the launch plan for the swarm

---

## `runtime_execute_dispatch.py`
Purpose:
- runtime-side manifest helper

What it does:
- validates manifest structure
- prepares launchable vs skipped runs
- builds post-spawn DB patch payloads
- finalizes launch summary

Use when:
- the OpenClaw runtime needs deterministic support logic around the launch loop

---

## `run_dispatch_runtime.py`
Purpose:
- realtime runtime orchestration wrapper

What it does:
- calls runtime validation and preparation logic
- emits the exact OpenClaw tool loop to execute
- accepts actual spawn results
- builds patch/update steps
- finalizes the launch summary

Use when:
- Orchestrator wants to drive the launch end-to-end from the OpenClaw runtime session

---

## `update_research_run.py`
Purpose:
- patch one `research_runs` row

What it does:
- updates status
- merges notes
- updates primary artifact path
- optionally marks completion timestamp

Use when:
- runtime needs to store returned child session metadata or later completion metadata

---

# Full process walkthrough

## Phase 1 — planner preparation

### Step 1: select a market
Run:
- `select_next_market.py`

Output:
- one eligible market payload

### Step 2: open or fetch the case
Run:
- `open_case.py`

Output:
- one case record

### Step 3: prepare dispatch manifest
Run:
- `dispatch_case_research.py --case-id <case_id>`

This will:
- set market to `researching`
- create `research_runs`
- generate prompts
- emit dispatch manifest JSON

Output:
- canonical dispatch manifest

---

## Phase 2 — runtime launch execution

### Step 4: validate + prepare runtime launch plan
Run:
- `run_dispatch_runtime.py`
with the manifest

This returns:
- launchable runs
- skipped runs
- runtime tool loop

### Step 5: execute `sessions_spawn`
Inside the OpenClaw runtime, for each launchable run:
- call `sessions_spawn` with the emitted `spawn_payload`

### Step 6: patch DB after successful spawn
For each successful spawn:
- build the patch payload
- apply it using `update_research_run.py`

### Step 7: finalize summary
Feed actual spawn results back into:
- `run_dispatch_runtime.py --spawn-results-json ...`

Output:
- final launch summary

---

# Partial-failure handling

If some runs launch successfully and others fail:
- keep successful runs active
- record failed launches
- return dispatch status `launched_partial`
- on retry, skip runs that already have `notes.child_session_key`
- retry only the still-unlaunched runs

This is the intended behavior.

Example:
- 3/5 launched
- 2/5 failed
- overall result = `launched_partial`

---

# Idempotency rule

The main idempotency key is:
- `research_runs.notes.child_session_key`

If that field is already present for a run:
- do not relaunch by default
- treat it as `skipped_existing`

This prevents duplicate researcher launches.

---

# Default runtime profile

Unless explicitly overridden, the swarm launch defaults are:
- `model: codex`
- `thinking: medium`

These defaults are set in:
- `dispatch_case_research.py`

---

# End-to-end orchestration question

## Can Orchestrator run this from end to end?
Yes.

The intended model is:
1. Orchestrator runs planner scripts
2. Orchestrator runs the runtime wrapper
3. Orchestrator performs the OpenClaw `sessions_spawn` loop in-session
4. Orchestrator applies DB patch steps
5. Orchestrator receives the final launch summary

The only important boundary is:
- `sessions_spawn` must still happen in the OpenClaw runtime/session layer
- not inside plain Python subprocess code

That is by design.

---

# One-line summary

This folder contains the launch control-plane for the research swarm: planner scripts prepare the manifest, the OpenClaw runtime executes the spawn loop, patch helpers update DB state, and the runtime wrapper summarizes launch outcomes for clean retries and downstream orchestration.
