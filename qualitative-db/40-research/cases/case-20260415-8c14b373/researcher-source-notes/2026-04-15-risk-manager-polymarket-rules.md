---
type: source_note
case_key: case-20260415-8c14b373
dispatch_id: dispatch-case-20260415-8c14b373-20260415T130923Z
analysis_date: 2026-04-15
persona: risk-manager
domain: prediction-markets
subdomain: market-resolution
entity:
topic: polymarket-resolution-rules
question: Will claude-opus-4-6-thinking be the best AI model on April 17, 2026?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules page
source_type: market_contract_source
source_url: https://polymarket.com/event/best-ai-model-on-april-17-style-control-off
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [claude, anthropic, openai, gemini, grok]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-8c14b373/researcher-analyses/2026-04-15/dispatch-case-20260415-8c14b373-20260415T130923Z/personas/risk-manager.md]
tags: [polymarket, contract, rules, timing-risk]
---

# Summary

This source defines the market's exact resolution mechanics, including the deadline, the leaderboard tab, tie-breaking, and fallback behavior if the source is unavailable.

## Key facts extracted

- The market resolves according to the model with the highest arena score on the Chatbot Arena / LM Arena leaderboard when checked on April 17, 2026 at 12:00 PM ET.
- The relevant table is the `Score` column under the `Text Arena | Overall` leaderboard tab, with style control off.
- Ranking is by arena score first.
- If models are tied by score, the market uses alphabetical order of model names as listed in the market group, including suffixes like `-thinking`, as the tiebreak.
- The rules explicitly give the example that `claude-opus-4-6` would rank ahead of `claude-opus-4-6-thinking` in a tie.
- If the resolution source is unavailable at check time, the market remains open until the leaderboard is back online and then resolves on the first check after availability returns.
- If the original source becomes permanently unavailable, the market can resolve using another source.

## Evidence directly stated by source

- The page directly states the date/time check point: April 17, 2026, 12:00 PM ET.
- The page directly states the relevant leaderboard slice: `Text Arena | Overall` and style control off.
- The page directly states the tie-break rule that is adverse to `claude-opus-4-6-thinking` versus the plain `claude-opus-4-6` model.

## What is uncertain

- The exact fallback source is not predefined if the named leaderboard becomes permanently unavailable.
- The market page excerpt available via fetch gives summary/rules text, but not a separately versioned contract document with immutable rule history.

## Why this source may matter

For this case, contract interpretation matters materially. The current leaderboard leader is not enough by itself; all rule conditions have to be satisfied at the specified check time and tie handling is nontrivial.

## Possible impact on the question

This source introduces meaningful downside risk to a seemingly dominant YES position because `claude-opus-4-6-thinking` loses any exact-score tie with `claude-opus-4-6`, and because a live leaderboard can still move before the check time.

## Reliability notes

High reliability for market mechanics because this is the market's own rules page. Moderate ambiguity remains only around fallback handling if the primary source is unavailable.