---
type: source_note
case_key: case-20260413-61dcf900
dispatch_id: dispatch-case-20260413-61dcf900-20260413T184628Z
analysis_date: 2026-04-13
persona: base-rate
domain: sports
subdomain: hockey
entity:
topic: los-angeles-kings-playoff-qualification
question: Will the Los Angeles Kings make the NHL Playoffs?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket contract description and market price snapshot
source_type: market-contract
source_url: https://polymarket.com/event/which-teams-will-make-the-nhl-playoffs
source_date: 2026-04-13
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: []
related_drivers:
  - operational-risk
upstream_inputs: []
downstream_uses: []
tags: [market, polymarket, contract, resolution, price]
---

# Summary

The market asks whether the Los Angeles Kings will make the 2025-26 NHL Playoffs. Current market price in the assignment context is 0.735, implying 73.5%. The contract says official NHL information is the resolution source, while a consensus of credible reporting may also be used. It also states the market resolves early to No if qualification becomes impossible.

## Key facts extracted

- Market-implied probability from assignment snapshot: 73.5%.
- Resolution standard: official NHL information governs, with consensus credible reporting as supplemental fallback.
- Qualification through official NHL format including wild cards counts.
- Early No resolution can occur if mathematical elimination is official under NHL rules.

## Evidence directly stated by source

- Contract wording and resolution mechanics.
- Current market price snapshot supplied in assignment context.

## What is uncertain

- The exact timing of resolution may depend on when NHL publishes clinch/elimination status versus when consensus reporting becomes clear.
- Because the contract permits consensus reporting, there is some source-of-truth ambiguity before an explicit official clinch marker appears.

## Why this source may matter

It defines both the comparison baseline and the resolution mechanics. For this case, the main analytic task is not whether the contract is ambiguous overall, but whether the market price is too high or low relative to the Kings' actual playoff odds given their standings position.

## Possible impact on the question

The contract structure makes official standings and official qualification status the key direct evidence. The fallback to consensus reporting matters mainly if the standings combinations imply a clinch/elimination before the NHL labels it explicitly.

## Reliability notes

- High reliability for the quoted contract terms provided in assignment context.
- Moderate reliability for inference from current market price because price is a market snapshot, not a truth source.