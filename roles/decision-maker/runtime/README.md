# Decision-Maker Runtime

Runtime code for the Decision-Maker stage should own:
- preparing deterministic decision context bundles
- supporting Orchestrator -> Decision-Maker handoff
- maintaining a canonical decision-stage status artifact for each case
- validating packet structure and deterministic invariants
- rendering the canonical markdown packet
- optionally writing the structured JSON packet
- failing closed when required context is missing or outputs are inconsistent

Runtime ownership split:
- Orchestrator hosts the canonical runtime files in this folder
- the separate `decision-maker` agent executes decision work against these files after Orchestrator hands off a case

Canonical case-level status surface:
- `qualitative-db/40-research/cases/<case-key>/decision-maker/artifacts/decision-stage-status.json`

Current runtime entry points:
- `build_decision_context.py` — build deterministic decision bundle from synthesis artifacts
- `planner/scripts/decide_verification_mode.py` — deterministically choose Decision-Maker verification mode from structured signals
- `planner/scripts/select_decision_inputs.py` — deterministically build the compact selected-input bundle under a hard size budget
- `planner/scripts/build_decision_prompt.py` — build the actual Decision-Maker prompt from the compact selected-input bundle rather than the whole case tree
- `bootstrap_decision_telegram_lane.py` — create/reuse a dedicated Telegram decision lane
- `run_decision_maker.py` — invoke the separate `decision-maker` agent, validate the returned packet, render artifacts, and update lifecycle state
- `show_decision_stage_status.py` — summarize current decision-stage state for a case

Visible Telegram stage markers owned by the Decision-Maker runtime:
- `SYNTHESIS RECEIVED ...`
- `DECISION-MAKING ANALYSIS UNDERWAY ...`
- `DECISION-MAKING COMPLETED, DECISION PACKAGE CREATED ...`

Design rule:
- Decision-Maker runtime should be stricter than synthesis, not looser
- if executable confidence is not justified, produce a no-trade / not-ready packet instead of forcing action
- keep the separate `decision-maker` agent as the judgment brain, but let Orchestrator-hosted runtime own deterministic verification-mode selection, compact input-bundle selection, budget enforcement, validation, artifact rendering, lane bootstrap, and lifecycle status
