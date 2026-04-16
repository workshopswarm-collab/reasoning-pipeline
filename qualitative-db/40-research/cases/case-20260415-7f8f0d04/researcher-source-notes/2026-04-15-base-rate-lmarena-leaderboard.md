---
type: source_note
case_key: case-20260415-7f8f0d04
dispatch_id: dispatch-case-20260415-7f8f0d04-20260415T104754Z
analysis_date: 2026-04-15
persona: base-rate
domain: tech-ai
subdomain: model-rankings
entity:
topic: chatbot-arena-style-control-on-leaderboard
question: Will claude-opus-4-6-thinking be the top AI model on April 17, 2026 (Style Control On)?
driver: reliability
date_created: 2026-04-15
source_name: Chatbot Arena Text Arena Overall leaderboard snapshot via web fetch
source_type: primary leaderboard source
source_url: https://lmarena.ai/leaderboard/text
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: high
agent: Orchestrator
related_entities: [anthropic, claude]
related_drivers: [reliability, operational-risk, product-launches]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-7f8f0d04/researcher-analyses/2026-04-15/dispatch-case-20260415-7f8f0d04-20260415T104754Z/personas/base-rate.md]
tags: [chatbot-arena, leaderboard, style-control-on, anthropic]
---

# Summary

A direct web fetch of the Chatbot Arena text leaderboard page on 2026-04-15 showed an Anthropic model occupying the top line of the extracted ranking table with score `1502±5`, followed by another Anthropic model at `1496±5`, then Meta and Google entries. The extracted page text did not preserve clean model names in a human-readable way, which limits exact model-string verification from this fetch alone, but it still strongly indicates Anthropic currently leads the relevant leaderboard.

## Key facts extracted

- The fetched leaderboard page redirected from `lmarena.ai` to `arena.ai` and returned status 200.
- The extracted ranking content showed the top few rows as:
  - rank 1: Anthropic entry at score `1502±5`
  - rank 2: Anthropic entry at score `1496±5`
  - rank 3: Meta entry at score `1495±9`
  - rank 4: Google entry at score `1493±5`
- The margin from first to third in the extracted text was only about 7 points, so the top spot is not locked by a huge gap.
- The top of the board appears crowded with several frontier labs, but Anthropic currently occupies both of the top two extracted lines.

## Evidence directly stated by source

- Anthropic appears to be currently ahead on the relevant leaderboard snapshot.
- The current market favorite is directionally consistent with the currently observed leaderboard state.

## What is uncertain

- The readability extraction stripped or mangled the exact model names, so this note cannot independently prove that the #1 row is specifically `claude-opus-4-6-thinking` rather than another Anthropic variant.
- The fetch does not clearly expose whether the style-control-on toggle state is rendered exactly as the contract requires, though the page URL and Polymarket contract both point to this text leaderboard surface.
- The leaderboard can change materially before April 17, 2026 noon ET.

## Why this source may matter

This is the main primary evidence about present leaderboard state. Even with name-parsing limitations, it supports the outside-view claim that the market is anchored to a model family already in or near first place rather than pricing a long-shot challenger.

## Possible impact on the question

Current leaderboard state supports a high probability for the Anthropic side of the market, but exact-contract resolution still depends on the precise model string remaining first at the deadline and on tie handling.

## Reliability notes

Primary and timely, but only medium certainty for exact-model identification because the extraction degraded the model names. Best used together with the contract text and an explicit verification caveat.