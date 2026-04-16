---
type: source_note
case_key: case-20260415-7f8f0d04
dispatch_id: dispatch-case-20260415-7f8f0d04-20260415T104754Z
analysis_date: 2026-04-15
persona: risk-manager
domain: tech-ai
subdomain: model-rankings
entity:
topic: polymarket contract and resolution mechanics
question: Will claude-opus-4-6-thinking be the top AI model on April 17, 2026 (Style Control On)?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page
source_type: market contract / resolution source summary
source_url: https://polymarket.com/event/top-ai-model-on-april-17-style-control-on
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [anthropic, claude]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [risk-manager finding, risk-manager evidence map, risk-manager assumption note]
tags: [polymarket, contract, resolution, style-control-on, leaderboard]
---

# Summary

This source gives the operative market wording and resolution mechanics. It says the market resolves by the model with the highest arena score under the Chatbot Arena / LM Arena text leaderboard with style control on, checked on April 17, 2026 at 12:00 PM ET.

## Key facts extracted

- Resolution is based on the `Score` column under the `Text Arena | Overall` leaderboard tab.
- Style control must be on.
- Check time is April 17, 2026, 12:00 PM ET.
- Ranking is by arena score first.
- If scores are tied, alphabetical order of the listed model strings in the market group is the tiebreaker.
- The market uses the leaderboard availability fallback rule: if the source is unavailable at check time, resolution waits until the first later check after it returns.

## Evidence directly stated by source

- The leaderboard at check time governs, not current standings.
- Multiple material conditions must all hold for a YES resolution on `claude-opus-4-6-thinking`:
  1. the relevant leaderboard page must be the same governing source,
  2. style control must be on,
  3. the relevant row must correspond to `claude-opus-4-6-thinking`,
  4. that model must be first by score at the check time,
  5. if tied on score, the alphabetical tiebreak must still favor that exact string.

## What is uncertain

- This page does not itself verify the live leaderboard row naming at the check moment.
- The fallback phrase `another resolution source` leaves some ambiguity if LM Arena becomes permanently unavailable.
- The market page does not itself prove that `claude-opus-4-6-thinking` is currently first; it only states how resolution will occur.

## Why this source may matter

This is the governing contract source for resolution mechanics and timing risk. The key risk-manager contribution is not just who is currently first, but whether current confidence properly prices model-string mapping, tie behavior, and the fact that the decisive observation happens later.

## Possible impact on the question

This source raises caution against treating current leaderboard leadership as sufficient. Contract interpretation and exact model naming are material because the market resolves on a later timestamp and on the exact listed string.

## Reliability notes

Useful and necessary for contract interpretation, but it is not the final source of truth on the winning model itself. It is authoritative for market wording, while LM Arena is the stated external resolution source.