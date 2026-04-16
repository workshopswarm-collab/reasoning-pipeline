---
type: assumption_note
case_key: case-20260413-e8e9e57e
dispatch_id: dispatch-case-20260413-e8e9e57e-20260413T224434Z
research_run_id: a71a7e05-3ebf-4d05-8e70-91f193956657
analysis_date: 2026-04-13
persona: market-implied
domain: sports
subdomain: hockey
entity: connor-mcdavid
topic: "leaderboard-to-award mapping"
question: "Will Connor McDavid win the 2025–2026 NHL Art Ross Trophy?"
date_created: 2026-04-13
agent: market-implied
status: active
certainty: medium-high
importance: high
time_horizon: "near-term resolution"
related_entities: ["connor-mcdavid", "nhl"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["award-resolution-mechanics"]
upstream_inputs: []
downstream_uses: ["market-implied.md", "market-implied.sidecar.json", "evidence/market-implied.md"]
tags: ["assumption-note", "art-ross", "resolution"]
driver:
---

# Assumption

The market is implicitly assuming that publicly visible 2025-26 points-leader status will map cleanly to the NHL’s official Art Ross Trophy attribution without a meaningful procedural surprise.

## Why this assumption matters

This is the bridge between the statistical case for McDavid and the contract-resolving case for `Yes`. If the mapping is clean, a 90%+ price is justified. If the mapping is messier than it looks, the market could be slightly overconfident.

## What this assumption supports

- A high-probability `Yes` view on McDavid.
- A conclusion that the market is mostly efficient rather than stale.
- A judgment that remaining uncertainty is procedural rather than performance-driven.

## Evidence or logic behind the assumption

- Independent contextual stats verification shows McDavid leading the 2025-26 points race.
- The Art Ross is ordinarily tied to the season points leader.
- There is no visible evidence from current sources that a rival is within one scoring correction or tiebreak edge.
- Polymarket itself prices the field as essentially closed.

## What would falsify it

- Official NHL information naming a different Art Ross winner.
- A late stat correction that changes the points leader.
- Resolution treatment hinging on a non-obvious procedural detail around finalist/announcement language.

## Early warning signs

- Official NHL publication delays or ambiguous wording.
- Credible reporting that the leaderboard is subject to correction.
- Any official source indicating that McDavid has not yet clinched.

## What changes if this assumption fails

The current high-confidence `Yes` view would need to be reduced sharply, and the market would look overextended rather than efficient.

## Notes that depend on this assumption

- Main finding at `personas/market-implied.md`.
- Evidence map at `evidence/market-implied.md`.
- Reasoning sidecar at `personas/market-implied.sidecar.json`.