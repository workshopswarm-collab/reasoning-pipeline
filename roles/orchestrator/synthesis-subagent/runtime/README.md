# Synthesis Runtime Lane

This folder contains the **runtime-control** half of the synthesis subagent system.

## Canonical truth

Runtime should own everything that happens after a synthesis bundle has been prepared.

## Intended responsibilities

- validate the synthesis bundle
- run the synthesis worker/subagent
- render `syndicated-finding.md`
- write `syndicated-finding.runtime.json`
- compute runtime-derived frontmatter fields such as midpoint, edge, relation-to-market, and edge-quality
- apply normalization and repair logic when synthesis output is malformed or incomplete

## Layout

- `scripts/` — runtime-control helpers

## Boundary

Runtime should enforce the artifact contract.
Behavioral instructions belong in the planner prompt/contract layer, not in the runtime implementation itself.
