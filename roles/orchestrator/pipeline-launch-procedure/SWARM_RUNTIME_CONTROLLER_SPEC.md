# Swarm Runtime Controller Spec

This document defines **Option 3**: a lightweight dedicated runtime-control lane for swarm execution.

## Purpose

Separate three concerns cleanly:
- planner/control-plane preparation
- runtime spawn/completion control
- research cognition inside child subagents

The runtime controller is **not** a second strategist.
It is an event-driven execution lane responsible for keeping Postgres state in sync with actual runtime state.

## Role definition

The runtime controller session owns:
- reading a prepared dispatch manifest
- preparing the launch plan
- calling `sessions_spawn` for launchable runs
- immediately patching successful spawns to `running`
- listening for child completion events
- immediately reconciling completions to `completed` or `failed`
- preserving recovery data when patching fails
- producing launch/completion summaries for Orchestrator

The runtime controller session does **not** own:
- market selection
- persona design
- prompt design
- case synthesis
- canon updates
- strategic decision-making

## Core automation pattern

### Hook A — spawn hook
Immediately after a successful `sessions_spawn`:
1. build the post-spawn patch payload
2. patch the matching `research_runs` row
3. verify the row now shows:
   - `status = running`
   - `notes.child_session_key`
   - `notes.spawn_run_id`
   - `notes.dispatch_stage = spawned`

### Hook B — completion hook
Immediately after a child completion event:
1. extract `child_session_key`
2. determine final run status:
   - `completed`
   - `failed`
3. call `reconcile_research_run_completion.py`
4. verify the row now shows:
   - `status = completed` or `failed`
   - `completed_at` when completed
   - `notes.dispatch_stage = completed` or `terminated`

## Concrete runtime loop

### Launch phase
1. receive dispatch manifest from Orchestrator/planner
2. call `run_dispatch_runtime.py` to validate + prepare
3. for each launchable run:
   - call `sessions_spawn`
   - if successful, apply Hook A
   - if failed, record failed launch result and continue
4. finalize launch summary
5. report summary back to Orchestrator

### Completion phase
1. wait for runtime-generated child completion events
2. on each event, apply Hook B
3. report notable completions/failures back to Orchestrator
4. when all child runs for a dispatch are terminal, report dispatch completion summary

## Canonical join key

The canonical join key between runtime events and `research_runs` is:
- `research_runs.notes.child_session_key`

This must be stored immediately after spawn succeeds.

## Edge cases

### 1. Spawn succeeds, DB patch fails
Meaning:
- child session exists
- DB row is not updated

Required behavior:
- mark the run as **recovery required** in the controller's summary
- preserve:
  - `research_run_id`
  - `child_session_key`
  - `spawn_run_id`
- do not silently treat the launch as clean
- retry the DB patch before considering the run fully launched

### 2. Spawn fails before child session exists
Required behavior:
- mark run launch as failed
- continue launching remaining runs
- overall dispatch becomes `launched_partial` if others succeed

### 3. Completion event arrives, reconciliation fails
Meaning:
- child finished
- DB row did not update

Required behavior:
- preserve raw completion metadata
- mark completion reconciliation as recovery required
- retry the reconciliation step
- do not silently drop the event

### 4. Duplicate completion event arrives
Required behavior:
- treat reconciliation as idempotent
- if row is already terminal (`completed` or `failed`), do not re-open it
- optionally append a note like `duplicate_completion_event_seen = true`

### 5. Duplicate launch attempt
Required behavior:
- check for existing `notes.child_session_key`
- if present, skip relaunch by default
- surface as `skipped_existing`

### 6. Partial swarm success
Example:
- 3 runs launched successfully
- 2 runs failed launch

Required behavior:
- patch successful runs to `running`
- keep them active
- mark overall dispatch `launched_partial`
- retry only runs that still lack `notes.child_session_key`

### 7. Child writes artifacts but completion event is delayed
Required behavior:
- keep run as `running`
- do not mark complete from filesystem evidence alone unless explicitly using a fallback reconciliation policy

### 8. Child never completes / stalls
Required behavior:
- keep run `running`
- optionally later add watchdog logic or timeout policy
- do not auto-mark `failed` without an explicit controller rule

## Operational statuses

### `research_runs.status`
Use only:
- `queued`
- `running`
- `completed`
- `failed`
- `canceled`

### `notes.dispatch_stage`
Use finer-grained runtime markers such as:
- `awaiting_agent_runtime_spawn`
- `spawned`
- `completed`
- `terminated`
- `patch_failed`
- `completion_reconcile_failed`
- `superseded`

## Dedicated runtime controller session

Recommended role:
- one dispatch-bounded session dedicated to runtime swarm control for a single swarm run

Suggested responsibilities:
- own one live swarm launch from start to finish
- process completion events as they arrive
- send concise progress summaries back to Orchestrator
- exit after all tracked child runs are terminal and reconciled

Suggested naming:
- `swarm-runtime-controller`
- `pipeline-runtime-controller`
- `research-runtime-controller`

## Controller lifecycle

### Phase 1 — controller creation
Trigger:
- Orchestrator has selected/opened a case, generated a dispatch manifest, and decided to launch a swarm.

Action:
- Orchestrator spawns a fresh runtime-controller session for this dispatch only.

Inputs to the controller:
- dispatch manifest or manifest path
- case id
- case key
- dispatch id
- instruction to launch and monitor the full swarm
- instruction to terminate only after all child runs are terminal and reconciled

### Phase 2 — launch ownership
The controller session:
1. validates the manifest
2. prepares the launch plan
3. launches each child with `sessions_spawn`
4. after each successful spawn:
   - patches the run to `running`
   - stores `child_session_key`
   - stores `spawn_run_id`
5. records launch summary

Launch phase ends when every run is either:
- `running`
- failed to launch
- `skipped_existing`

### Phase 3 — monitor and reconcile
While the controller remains alive:
- it receives child completion events
- for each event it resolves the row by `notes.child_session_key`
- it patches the run to `completed` or `failed`
- it stores error/completion summary details in `notes`

The controller must not terminate while any tracked child run remains non-terminal.

Terminal states:
- `completed`
- `failed`
- `canceled`

### Phase 4 — final summary
When all tracked child runs are terminal and reconciled:
- controller sends a final dispatch summary back to Orchestrator
- include:
  - dispatch id
  - case id / case key
  - launched count
  - completed count
  - failed count
  - any recovery-required anomalies
  - child session keys by persona

### Phase 5 — termination
The controller may exit only when all of the following are true:
1. all launched child runs are terminal in DB
2. no spawn-patch recovery items remain
3. no completion-reconciliation recovery items remain
4. final summary has been sent to Orchestrator

## Message contract with Orchestrator

### Orchestrator -> runtime controller
Should include:
- dispatch manifest or manifest path
- case id / case key
- optional retry mode
- mode: `launch-and-monitor`
- termination rule: exit when all child runs are terminal and reconciled

### Runtime controller -> Orchestrator
Should include:
- launch summary
- per-run statuses
- recovery-required alerts
- dispatch completion summary when all child runs are terminal

## Implementation guidance

The runtime controller should treat these scripts as mandatory helpers:
- `run_dispatch_runtime.py`
- `runtime_execute_dispatch.py`
- `update_research_run.py`
- `reconcile_research_run_completion.py`

The runtime controller should never rely on memory alone for status tracking.

## One-line rule

Create one controller session per dispatch, let it own the swarm until every child run is terminal and reconciled, then let it exit.
