# Synthesis Subagent

This folder is the parallel synthesis control-plane for consolidating researcher-swarm outputs into downstream-ready synthesis artifacts.

## Intended architecture

Match the same broad split used by `../researchers-swarm-subagents/`:
- `planner/` = deterministic preparation work
- `runtime/` = execution, validation, rendering, and persistence

## Planner responsibility

Planner should own:
- selecting the synthesis target (typically one dispatch)
- loading the canonical researcher findings for that dispatch
- assembling a synthesis bundle from persona findings plus any allowed supporting artifacts
- building the synthesis prompt/contract
- emitting a synthesis manifest or equivalent runtime input

Current first-pass planner scripts:
- `planner/scripts/build_synthesis_bundle.py`
- `planner/scripts/build_reasoning_extract_jobs.py`
- `planner/scripts/build_reasoning_extract_prompt.py`
- `planner/scripts/build_extracts_synthesis_bundle.py`
- `planner/scripts/build_synthesis_prompt.py`

## Runtime responsibility

Runtime should own:
- validating the synthesis bundle
- running the synthesis worker/subagent
- validating the worker's JSON result
- rendering markdown artifacts from that JSON result
- writing `syndicated-finding.md`
- writing `decision-handoff.md`
- writing `syndicated-finding.runtime.json`
- computing runtime-derived decision-header fields
- normalizing and repairing synthesis outputs when needed

Current first-pass runtime scripts:
- `runtime/scripts/validate_reasoning_extract.py`
- `runtime/scripts/validate_synthesis_result.py`
- `runtime/scripts/render_syndicated_finding.py`
- `runtime/scripts/render_decision_handoff.py`
- `runtime/scripts/write_syndicated_runtime_metadata.py`
- `runtime/scripts/run_reasoning_extract_executor.py`
- `runtime/scripts/run_synthesis_executor.py`
- `runtime/scripts/launch_pending_extraction_subagents.py`
- `runtime/scripts/launch_synthesis_if_ready.py`
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

Current staged direction:
1. build raw dispatch synthesis bundle
2. build per-persona reasoning-extraction jobs
3. run persona reasoning extraction
4. validate reasoning extracts
5. build extracts-synthesis bundle
6. synthesize over raw findings plus extract guidance, while running a bounded synthesis-stage truth-finding research pass aimed at improving predictive accuracy
7. render syndicated finding + sidecar
8. render deterministic `decision-handoff.md` for the downstream decision-maker

Canonical per-persona extract path:
- `researcher-analyses/<date>/<dispatch-id>/synthesis-reasoning-extracts/<persona>.json`

Current extraction executor:
- `runtime/scripts/run_reasoning_extract_executor.py`
  - builds the raw synthesis bundle when needed
  - builds reasoning-extract jobs when needed
  - builds the persona-specific extraction prompt
  - supports manual-result mode and live `sessions.send` execution mode
  - validates the extract JSON before writing the canonical artifact

Current extracts-to-synthesis builder:
- `planner/scripts/build_extracts_synthesis_bundle.py`
  - loads validated per-persona extracts
  - emits `extracts-synthesis-bundle.json`
  - requires all expected extracts by default, with `--allow-partial` for development/testing
  - computes compact aggregate fields such as reasoning-mode counts, recommended-weight counts, persona probability estimates, and a provisional swarm-vs-market skepticism signal that raises the verification bar when the swarm appears far from market

Current final synthesis prompt builder:
- `planner/scripts/build_synthesis_prompt.py`
  - uses `extracts-synthesis-bundle.json` as a compact navigation/index layer rather than as canonical truth
  - treats raw persona findings as the authoritative upstream artifacts and exposes them alongside the extracts so the synthesizer can critically interrogate compression, omission, or overstatement in each extract
  - now includes raw persona material selectively by default rather than full-body by default: every persona gets a compact claim/summary excerpt, while only a small targeted subset gets a larger raw-body excerpt
  - now explicitly supports a bounded synthesis-stage truth-finding research pass aimed at improving predictive accuracy while treating the swarm as the baseline prior rather than as a final answer
  - requires the syndicated probability range to be the synthesizer's own final post-synthesis judgment rather than a mechanical average/median/restatement of the swarm's probabilities
  - requires the synthesizer to explain any material difference between its final probability and the swarm-implied center
  - explicitly raises the independent-verification bar when the provisional swarm-vs-market edge is large, and asks the synthesizer to surface both edge-verification quality and any compression back toward market caused by insufficient verification

Automatic handoff hook now exists:
- `runtime/scripts/kickoff_synthesis_after_swarm.py`
  - runs after researcher swarm terminal completion
  - builds the raw synthesis bundle, reasoning-extract jobs, and extraction prompts automatically
  - writes `synthesis-stage-status.json` into the dispatch directory
  - emits explicit dedicated extraction-subagent requests (`label`, `persona`, `prompt_path`, `artifact_path`) plus a dedicated synthesis-subagent label
  - if all extracts already exist, can also build the extracts-synthesis bundle and final synthesis prompt

## How the synthesis pipeline works now

1. **Market/case selection happens upstream**
   - Orchestrator selects the next market/case and creates a dispatch id plus a researcher-swarm manifest.

2. **Researcher swarm runs first**
   - Persona lanes run in their Telegram threads and write dispatch-scoped research artifacts such as:
     - `personas/<persona>.md`
     - `assumptions/<persona>.md`
     - `evidence/<persona>.md`

3. **Dispatch finalization triggers synthesis kickoff**
   - Once the swarm is truly complete, `researchers-swarm-subagents/runtime/scripts/runrepairs/finalize_dispatch_after_swarm.py` can best-effort call `runtime/scripts/kickoff_synthesis_after_swarm.py`.

4. **Kickoff builds synthesis-stage preparation artifacts**
   - Kickoff writes:
     - `synthesis-bundle.json`
     - `reasoning-extract-jobs.json`
     - per-persona extraction prompts
     - `synthesis-stage-status.json`

5. **Extraction subagents produce compact per-persona reasoning extracts**
   - `runtime/scripts/launch_pending_extraction_subagents.py` reads `synthesis-stage-status.json` and launches missing extraction executors in the existing persona Telegram topic sessions.
   - Extract artifacts are written under `synthesis-reasoning-extracts/<persona>.json`.
   - Raw persona findings remain authoritative; extracts are helper artifacts only.

6. **Extraction artifacts are validated**
   - `runtime/scripts/run_reasoning_extract_executor.py` validates each extract before writing the canonical dispatch-scoped extract artifact.
   - Extract artifacts now carry runtime metadata tying them to the current persona source content, extraction job input, and extraction prompt hash.
   - If an existing extract artifact is missing that metadata or no longer matches the current job/prompt, kickoff and bundle-building treat it as stale and require regeneration.

7. **Validated extracts are bundled for final synthesis**
   - `planner/scripts/build_extracts_synthesis_bundle.py` creates `extracts-synthesis-bundle.json`.
   - This bundle includes extract payloads, references back to raw persona findings, and deterministic aggregate skepticism aids such as:
     - provisional swarm probability range
     - provisional swarm-vs-market edge
     - provisional edge verification bar

8. **The final synthesis prompt is built**
   - `planner/scripts/build_synthesis_prompt.py` consumes `extracts-synthesis-bundle.json`.
   - The prompt:
     - treats the swarm as a baseline prior rather than a final answer
     - treats extracts as lossy suggestions rather than canonical truth
     - includes selective raw persona excerpts for cross-checking
     - asks the synthesizer to do bounded truth-finding research
     - asks the synthesizer to explain material divergence from the swarm-implied center

9. **A dedicated Telegram synthesis lane is created at synthesis start**
   - `runtime/scripts/launch_synthesis_if_ready.py` now bootstraps a fresh synthesis Telegram topic right before final synthesis launch.
   - That lane becomes the delivery/session target for the synthesis worker and the visible synthesis start/finish markers.

10. **The synthesis worker returns JSON, not markdown**
   - The synthesis worker/subagent produces a JSON result containing the claim, authored frontmatter fields, and section bodies.

11. **Runtime validates and renders the final artifacts**
   - `runtime/scripts/run_synthesis_executor.py` validates the synthesis JSON and then renders:
     - `syndicated-finding.md`
     - `syndicated-finding.runtime.json`
     - `decision-handoff.md`
   - Runtime, not the model, computes deterministic fields such as midpoint, edge vs market, relation to market, and edge quality.

12. **Canonical case-level synthesis outputs live under `synthesizer-agent/`**
   - Final case-level outputs are written to:
     - `qualitative-db/40-research/cases/<case-key>/synthesizer-agent/syndicated-finding.md`
     - `qualitative-db/40-research/cases/<case-key>/synthesizer-agent/syndicated-finding.runtime.json`
     - `qualitative-db/40-research/cases/<case-key>/synthesizer-agent/decision-handoff.md`

## Status logging and repair/finalization

- `synthesis-stage-status.json` is now the explicit stage-state ledger for the synthesis pipeline.
- It records:
  - top-level stage status
  - per-persona extraction request status
  - request-count summaries
  - stage events with timestamps
  - synthesis-lane summary fields
  - terminal summary fields once the stage reaches a terminal outcome
  - final artifact paths once synthesis completes
- Repair/finalization helpers now exist:
  - `runtime/scripts/runrepairs/reconcile_synthesis_from_artifacts.py`
    - infers stage truth from current extract/final artifacts and current job/prompt hashes
    - can also detect a dead final-synthesis process when status says `final_synthesis_launched` but no final artifacts exist
  - `runtime/scripts/runrepairs/finalize_synthesis_after_stage.py`
    - runs reconciliation first and then advances synthesis only when the stage is actually ready
- A compact inspection helper also exists:
  - `runtime/scripts/show_synthesis_stage_status.py`
    - prints a concise summary of current status, lane info, last stage event, terminal summary, and final artifact paths
- Multi-dispatch/idempotency hardening now also exists:
  - status-file mutations are lock-protected for the main launcher/executor paths
  - extraction relaunch skips already-running extractor PIDs
  - final synthesis launch skips an already-running final synthesis PID
  - synthesis-lane bootstrap is race-safe and reuses the lane if another process created it first
  - re-running launchers on a completed dispatch should no-op cleanly rather than duplicating work
- Early-failure rule:
  - if any extraction request is failed/stale/missing, final synthesis should not continue
  - repair/finalization should stop at the earliest failing stage rather than trying to push the whole synthesis process through

## Current known caveats

- The live architecture is mostly wired end to end, and extraction provenance/mismatch checks are now stronger, but legacy extract artifacts created before those checks will be treated as stale and need regeneration.
- Manual-result testing is still supported, but it now depends on runtime metadata plus current-job/prompt alignment; preserving that discipline matters if manual-result mode is used again.
- The current synthesis prompt is materially smaller than the full-body hybrid version, but prompt-size discipline still matters because selective raw-reference inclusion can grow again if left unconstrained.

## Boundary

This folder should follow the same architectural pattern as the researcher swarm:
- contract/prompt docs define behavior
- templates define artifact shape
- runtime code enforces validation, derivation, and persistence

## Execution model

Canonical intention: Orchestrator should wake dedicated subagents for the two semantic phases rather than reuse arbitrary sessions:
- extraction subagents for per-persona reasoning extraction
- a separate synthesis subagent for the final synthesis pass

See `planner/prompts/execution-architecture.md`.
