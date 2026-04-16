---
type: source_note
case_key: case-20260415-8c14b373
dispatch_id: dispatch-case-20260415-8c14b373-20260415T130923Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: tech-ai
subdomain: llm-leaderboards
entity:
topic: Chatbot Arena leaderboard state and timing
question: Will claude-opus-4-6-thinking be the best AI model on April 17, 2026?
driver: reliability
date_created: 2026-04-15
source_name: Arena AI / Chatbot Arena Text Leaderboard (style control off)
source_type: primary_resolution_source
source_url: https://arena.ai/leaderboard/text
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: high
agent: catalyst-hunter
related_entities: []
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-8c14b373/researcher-analyses/2026-04-15/dispatch-case-20260415-8c14b373-20260415T130923Z/personas/catalyst-hunter.md]
tags: [primary-source, leaderboard, resolution-source, timing]
---

# Summary

This source note captures the current observable state of the official resolution source for the market. The key point is that the live Text Arena Overall leaderboard with style control off currently does **not** show `claude-opus-4-6-thinking` in first place; it shows that model in 4th place at the time checked on 2026-04-15.

## Key facts extracted

- The market resolves off the Text Arena | Overall leaderboard with style control off at the check time specified in the contract.
- On the observed leaderboard snapshot, `claude-opus-4-6-thinking` appears at rank 4.
- The same snapshot shows `claude-opus-4-6-thinking` with score `1502 ± 5`.
- The same snapshot shows `gpt-5.4-high` at score `1481 ± 6`.
- The same snapshot shows `grok-4.20-beta1` at rank 10 with score `1485 ± 6`.
- The same snapshot shows `gemini-2.5-pro` much lower, rank 41 with score `1448 ± 3`.
- Because the checked live board is the governing source, the dominant catalyst before resolution is not a scheduled formal event but any leaderboard reranking or score refresh before the market’s Apr. 17, 2026 noon ET check.

## Evidence directly stated by source

- Model names and displayed scores on the live leaderboard.
- Current leaderboard ordering.
- The source page corresponds to the text leaderboard used by the market rules.

## What is uncertain

- The readable scrape does not fully expose every top-three model name cleanly in one compact output, though it clearly exposes the rank and score context for several named competitors including the target model.
- The site is dynamic, so rankings can change before the market check time.
- The source note does not by itself prove that today’s ranking will persist to Apr. 17 noon ET.

## Why this source may matter

This is the explicit source of truth for resolution, so any thesis must start from the fact that the target model is presently **not** leading on the governing board. That sharply changes the catalyst framing: the market price is implicitly betting on a near-term leaderboard update favorable enough to move `claude-opus-4-6-thinking` from 4th to 1st before the check.

## Possible impact on the question

Direct negative impact on a bullish reading of the current 93.1% market price. If the board were checked now, the target would lose. Therefore the path to “Yes” requires an additional leaderboard change before the resolution check.

## Reliability notes

- High relevance because this is the governing resolution source.
- Medium extraction certainty because the site is heavily dynamic and machine-readable output is messy, but the target model’s current rank and score were directly inspected from page HTML.
- Independence is limited because any secondary commentary about the leaderboard would ultimately derive from this same source.