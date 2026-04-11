# Synthesis Subagent

This folder is the synthesis control-plane for consolidating researcher-swarm outputs into downstream-ready synthesis artifacts.

## Intended architecture

Match the same broad split used by `../researchers-swarm-subagents/`:
- `planner/` = deterministic preparation work
- `runtime/` = execution, validation, rendering, and persistence

## Planner responsibility

Planner owns:
- selecting the synthesis target (typically one dispatch)
- loading the canonical researcher findings for that dispatch
- loading and validating researcher sidecars for that dispatch
- assembling raw + structured synthesis bundles
- building the final synthesis prompt/contract
- emitting runtime-ready inputs

Current planner scripts:
- `planner/scripts/build_synthesis_bundle.py`
- `planner/scripts/build_sidecar_synthesis_bundle.py`
- `planner/scripts/build_synthesis_prompt.py`

## Runtime responsibility

Runtime owns:
- validating synthesis-stage state
- promoting dispatches into synthesis once sidecars are ready
- running the synthesis worker/subagent
- validating the worker's JSON result
- rendering markdown artifacts from that JSON result
- writing `syndicated-finding.md`
- writing `decision-handoff.md`
- writing `syndicated-finding.runtime.json`
- computing runtime-derived decision-header fields
- normalizing and repairing synthesis outputs when needed

Current runtime scripts:
- `runtime/scripts/validate_synthesis_result.py`
- `runtime/scripts/render_syndicated_finding.py`
- `runtime/scripts/render_decision_handoff.py`
- `runtime/scripts/write_syndicated_runtime_metadata.py`
- `runtime/scripts/run_synthesis_executor.py`
- `runtime/scripts/kickoff_synthesis_after_swarm.py`
- `runtime/scripts/launch_synthesis_if_ready.py`
- `runtime/scripts/bootstrap_synthesis_telegram_lane.py`
- `runtime/scripts/status.py`
- `runtime/scripts/show_synthesis_stage_status.py`
- `runtime/scripts/runrepairs/reconcile_synthesis_from_artifacts.py`
- `runtime/scripts/runrepairs/finalize_synthesis_after_stage.py`

## Canonical artifact contract

Important implementation detail:
- the synthesis worker returns JSON, not markdown
- runtime code validates that JSON and renders the markdown artifacts
- `syndicated-finding-template.md` is the live human-readable contract the worker is prompted against

Current artifact targets:
- `qualitative-db/00-system/templates/syndicated-finding-template.md`
- `qualitative-db/00-system/templates/syndicated-finding-runtime-metadata-template.json`

## Current staged direction

1. build raw dispatch synthesis bundle
2. require one researcher sidecar per persona next to the persona memo
3. build sidecar-synthesis bundle directly from researcher sidecars
4. synthesize over raw findings plus sidecar guidance, while running a bounded synthesis-stage truth-finding research pass aimed at improving predictive accuracy
5. render syndicated finding + runtime sidecar
6. render deterministic `decision-handoff.md` for the downstream decision-maker

Canonical per-persona sidecar path:
- `researcher-analyses/<date>/<dispatch-id>/personas/<persona>.sidecar.json`

## How the synthesis pipeline works now

1. **Market/case selection happens upstream**
   - Orchestrator selects the next market/case and creates a dispatch id plus a researcher-swarm manifest.

2. **Researcher swarm runs first**
   - Persona lanes run in their Telegram threads and write dispatch-scoped research artifacts such as:
     - `personas/<persona>.md`
     - `personas/<persona>.sidecar.json`
     - `assumptions/<persona>.md`
     - `evidence/<persona>.md`

3. **Researcher completion hard-requires the sidecar**
   - `researchers-swarm-subagents/runtime/scripts/reconcile_research_run_completion.py` validates that the sidecar exists and matches the final persona memo before allowing a run to finalize as completed.

4. **Dispatch finalization triggers synthesis kickoff**
   - Once the swarm is truly complete, `researchers-swarm-subagents/runtime/scripts/runrepairs/finalize_dispatch_after_swarm.py` calls `runtime/scripts/kickoff_synthesis_after_swarm.py` and then hands the returned status file into `runtime/scripts/launch_synthesis_if_ready.py`.
   - The researcher-side finalizer is only invoked once the active dispatch is actually terminal, which reduces pre-terminal fan-out.

5. **Kickoff builds synthesis-stage preparation artifacts**
   - Kickoff writes:
     - `synthesis-bundle.json`
     - `synthesis-stage-status.json`
   - If all sidecars are present, kickoff can also build:
     - `sidecar-synthesis-bundle.json`
     - `synthesis-prompt.md`

6. **Structured synthesis is sidecar-first**
   - `planner/scripts/build_sidecar_synthesis_bundle.py` validates researcher sidecars and creates `sidecar-synthesis-bundle.json`.
   - This bundle includes sidecar payloads, references back to raw persona findings, and deterministic aggregate skepticism aids such as:
     - provisional swarm probability range
     - provisional swarm-vs-market edge
     - provisional edge verification bar

7. **The final synthesis prompt is built**
   - `planner/scripts/build_synthesis_prompt.py` consumes `sidecar-synthesis-bundle.json`.
   - The prompt:
     - treats the swarm as a baseline prior rather than a final answer
     - treats sidecars as lossy helper summaries rather than canonical truth
     - includes selective raw persona excerpts for cross-checking
     - asks the synthesizer to do bounded truth-finding research
     - asks the synthesizer to explain material divergence from the swarm-implied center

8. **A dedicated Telegram synthesis lane is created at synthesis start**
   - `runtime/scripts/launch_synthesis_if_ready.py` bootstraps or reuses the dedicated synthesis Telegram topic right before final synthesis launch.
   - Launch is single-flight: concurrent callers compete for a dispatch-local launch claim, and only the winner is allowed to create/use the synthesis topic and spawn `run_synthesis_executor.py`.
   - That lane becomes the delivery/session target for the synthesis worker and the visible synthesis start/finish markers.

9. **The synthesis worker returns JSON, not markdown**
   - The synthesis worker/subagent produces a JSON result containing the claim, authored frontmatter fields, and section bodies.

10. **Runtime validates and renders the final artifacts**
   - `runtime/scripts/run_synthesis_executor.py` validates the synthesis JSON and then renders:
     - `syndicated-finding.md`
     - `syndicated-finding.runtime.json`
     - `decision-handoff.md`
   - Runtime, not the model, computes deterministic fields such as midpoint, edge vs market, relation to market, and edge quality.

11. **Canonical case-level synthesis outputs live under `synthesizer-agent/`**
   - Final case-level outputs are written to:
     - `qualitative-db/40-research/cases/<case-key>/synthesizer-agent/syndicated-finding.md`
     - `qualitative-db/40-research/cases/<case-key>/synthesizer-agent/syndicated-finding.runtime.json`
     - `qualitative-db/40-research/cases/<case-key>/synthesizer-agent/decision-handoff.md`

## Status logging and repair/finalization

- `synthesis-stage-status.json` is the explicit stage-state ledger for the synthesis pipeline.
- It records:
  - top-level stage status
  - per-persona sidecar readiness status
  - request-count summaries
  - stage events with timestamps
  - synthesis-lane summary fields
  - terminal summary fields once the stage reaches a terminal outcome
  - final artifact paths once synthesis completes
- Repair/finalization helpers:
  - `runtime/scripts/runrepairs/reconcile_synthesis_from_artifacts.py`
    - infers stage truth from current sidecars and final artifacts
    - can detect a dead final-synthesis process when status says `final_synthesis_launched` but no final artifacts exist
  - `runtime/scripts/runrepairs/finalize_synthesis_after_stage.py`
    - runs reconciliation first and then advances synthesis only when the stage is actually ready
- A compact inspection helper also exists:
  - `runtime/scripts/show_synthesis_stage_status.py`
    - prints a concise summary of current status, lane info, last stage event, terminal summary, and final artifact paths
- Multi-dispatch/idempotency hardening:
  - status-file mutations are lock-protected for kickoff, launcher, and main executor paths
  - kickoff now merges into the existing status file instead of overwriting it, so it preserves any in-flight launch claim or completed synthesis state
  - final synthesis launch uses a dispatch-local claim to enforce single-flight semantics
  - final synthesis launch skips an already-running final synthesis PID
  - synthesis-lane bootstrap is race-safe and reuses the lane if another process created it first
  - re-running launchers or kickoff on a completed dispatch should no-op cleanly rather than duplicating work or resetting the stage back to `ready_for_final_synthesis`
- Early-failure rule:
  - if any required sidecar is missing or invalid, final synthesis should not continue
  - repair/finalization should stop at the earliest failing stage rather than trying to push the whole synthesis process through

## Boundary

This folder should follow the same architectural pattern as the researcher swarm:
- contract/prompt docs define behavior
- templates define artifact shape
- runtime code enforces validation, derivation, and persistence

## Execution model

Canonical intention: Orchestrator should wake a dedicated synthesis subagent for the final synthesis pass only.
Researcher lanes own production of the structured per-persona sidecars upstream.

See `planner/prompts/execution-architecture.md`.
