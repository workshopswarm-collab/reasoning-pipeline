---
type: assumption_note
case_key: case-20260414-4c35c81d
dispatch_id: dispatch-case-20260414-4c35c81d-20260414T204205Z
research_run_id: 02719a2b-735e-4389-83a6-a04c37a7db57
analysis_date: 2026-04-14
persona: risk-manager
domain: sports
subdomain: soccer
entity:
topic: al-qadisiyah-vs-al-shabab
question: "Will Al Qadisiyah Saudi Club win on 2026-04-23?"
driver: performance
date_created: 2026-04-14
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: immediate
related_entities: ["saudi-arabia"]
related_drivers: ["performance"]
proposed_entities: ["al-qadsiah", "al-shabab", "saudi-pro-league"]
proposed_drivers: ["resolution-timestamp-misalignment"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-4c35c81d/researcher-analyses/2026-04-14/dispatch-case-20260414-4c35c81d-20260414T204205Z/personas/risk-manager.md"]
tags: ["sports", "soccer", "assumption", "timing-risk", "resolution-risk"]
---

# Assumption

The operative contract should be interpreted as referring to the already-posted Al Qadisiyah vs Al Shabab league match evidenced on 2026-04-14 metadata, despite the assignment text saying 2026-04-23.

## Why this assumption matters

The entire probability estimate swings from a pre-match handicapping question to a near-settled/no-win interpretation if the relevant event has already been played and ended 2-2.

## What this assumption supports

- A very low probability that `Al Qadisiyah win` resolves yes.
- A risk-manager conclusion that the market's 0.83 price is dangerously high relative to observed outcome metadata.
- Elevated attention to source-of-truth and timestamp mismatch risk rather than pure team-strength analysis.

## Evidence or logic behind the assumption

- Polymarket page metadata for this exact market slug includes article text stating the Round 29 matchup ended in a 2-2 draw.
- ESPN fixtures for 2026-04-14 also show Al Qadsiah 2-2 Al Shabab FT.
- Both sources cohere on teams and result, which is unlikely if they referred to unrelated matches.

## What would falsify it

- Evidence from the governing market rules or official competition source that the contract instead refers to a different future match on 2026-04-23.
- Evidence that Polymarket metadata cached an incorrect or unrelated result.
- Evidence of replay, abandonment, or administrative result change that would convert the non-win into a win.

## Early warning signs

- Contract text or event description explicitly naming 2026-04-23 as the actual scheduled kickoff.
- Official league fixture list showing a second Qadsiah-Shabab meeting on 2026-04-23.
- Polymarket settlement page diverging from the market-context article body.

## What changes if this assumption fails

If the assignment date is correct and the relevant match has not yet happened, then the analysis should revert toward a conventional pre-match favorite view, likely materially above 50% and potentially near the market, depending on lineup/injury checks.

## Notes that depend on this assumption

- Main risk-manager finding for this dispatch.
- Evidence map for this dispatch.