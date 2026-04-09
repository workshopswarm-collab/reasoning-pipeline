# Synthesis Planner Lane

This folder contains the **planner/control-plane** half of the synthesis subagent system.

## Canonical truth

Planner should own deterministic local preparation work.
Planner should not directly perform synthesis runtime execution.

## Intended responsibilities

- identify the dispatch/case to synthesize
- gather canonical persona findings
- gather allowed supporting artifacts when needed
- build the synthesis bundle
- build the synthesis prompt/contract
- emit a synthesis manifest or equivalent runtime input

## Layout

- `prompts/` — synthesis base contract and future synthesis prompt fragments
- `scripts/` — planner/control-plane helpers

## Boundary

Planner output should be a validated synthesis input package.
Execution, rendering, sidecar persistence, derived-field computation, and repair belong to the sibling `../runtime/` lane.
