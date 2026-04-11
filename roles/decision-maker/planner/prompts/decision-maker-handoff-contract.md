# Decision-Maker handoff contract

This contract defines what Orchestrator should send to the separate `decision-maker` agent when handing off a case.

## Target

Default target session:
- `agent:decision-maker:main`

## Handoff goals

The handoff should:
- identify the case unambiguously
- point to the canonical case artifacts in the Orchestrator repo
- point to the canonical Decision-Maker implementation surface in `roles/decision-maker`
- request final judgment and packet production
- keep the message compact and execution-oriented

## Required references

Every handoff should include:
- `case_key`
- `dispatch_id` when available
- absolute path to `decision-handoff.md`
- absolute path to `syndicated-finding.runtime.json` when present
- absolute path to the built decision-context JSON
- absolute path to the canonical Decision-Maker runtime entry point
- absolute path to the canonical output paths

## Required instruction shape

The message should tell Decision-Maker to:
1. review the upstream synthesis artifacts
2. use the canonical implementation surface in the Orchestrator repo
3. write/update the decision packet in the canonical Orchestrator case folder
4. fail closed rather than manufacture action
5. report back with a concise completion summary and blockers if any

## Design rule

Do not treat the separate `~/.openclaw/decision-maker` workspace as the canonical code location.
It is the agent's identity and continuity home.
The Orchestrator repo is the canonical implementation and artifact home.
