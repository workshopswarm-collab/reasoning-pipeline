---
type: source_note
case_key: case-20260415-7f8f0d04
dispatch_id: dispatch-case-20260415-7f8f0d04-20260415T104754Z
analysis_date: 2026-04-15
persona: variant-view
domain: prediction-markets
subdomain: contract-resolution
entity:
topic: polymarket-contract-resolution
question: Will claude-opus-4-6-thinking be the top AI model on April 17, 2026 (Style Control On)?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market description and resolution rules
source_type: primary
source_url: https://polymarket.com/event/top-ai-model-on-april-17-style-control-on
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: []
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-7f8f0d04/researcher-analyses/2026-04-15/dispatch-case-20260415-7f8f0d04-20260415T104754Z/personas/variant-view.md]
tags: [polymarket, contract, resolution, primary-source]
---

# Summary

This source defines the exact market mechanics: the winner is the model with the highest `Score` on the Chatbot Arena Text Arena Overall leaderboard with Style Control on, checked on April 17, 2026 at 12:00 PM ET.

## Key facts extracted

- Resolution checks the Chatbot Arena LLM Leaderboard on April 17, 2026 at 12:00 PM ET.
- The relevant surface is `https://lmarena.ai/leaderboard/text` under the `Text Arena | Overall` leaderboard with Style Control on.
- Models are ranked first by arena score.
- Ties are resolved by alphabetical order of the listed model names.
- The contract explicitly gives the example that `claude-opus-4-6` would rank ahead of `claude-opus-4-6-thinking` on a tied score.
- If the resolution source is unavailable at check time, the market remains open until the leaderboard returns and resolves on the first subsequent check.

## Evidence directly stated by source

- The exact time window and timezone are explicit.
- The exact leaderboard tab and scoring column are explicit.
- The tie-break rule is explicit.
- Fallback behavior for a temporarily unavailable source is explicit.

## What is uncertain

- The contract does not specify how long the source must remain stable; it resolves on the first relevant check.
- If the source were permanently unavailable, a substitute source would be used, but the substitute is not pre-named.

## Why this source may matter

This source determines what conditions all must hold for the market to resolve YES: `claude-opus-4-6-thinking` must still be first by score at the check time, or at minimum not tied with any alphabetically earlier listed competitor.

## Possible impact on the question

This source materially weakens an overly simplistic bullish case. `claude-opus-4-6-thinking` does not merely need to remain tied for best; it must remain strictly ahead of `claude-opus-4-6` unless some other tie structure still leaves it first.

## Reliability notes

- Highest relevance because it is the contract text.
- High certainty because the wording is explicit.
- Main residual risk is source availability/fallback ambiguity, but that only matters if Chatbot Arena is unavailable at check time.