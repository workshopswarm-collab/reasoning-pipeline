---
type: source_note
case_key: case-20260415-7f8f0d04
dispatch_id: dispatch-case-20260415-7f8f0d04-20260415T104754Z
analysis_date: 2026-04-15
persona: variant-view
domain: tech-ai
subdomain: model-benchmarks
entity:
topic: chatbot-arena-style-control-leaderboard
question: Will claude-opus-4-6-thinking be the top AI model on April 17, 2026 (Style Control On)?
driver: reliability
date_created: 2026-04-15
source_name: Chatbot Arena LLM Leaderboard — Text Arena Overall with Style Control
source_type: primary
source_url: https://arena.ai/leaderboard/text
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [claude, anthropic]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-7f8f0d04/researcher-analyses/2026-04-15/dispatch-case-20260415-7f8f0d04-20260415T104754Z/personas/variant-view.md]
tags: [chatbot-arena, leaderboard, style-control, primary-source]
---

# Summary

This source is the governing source of truth for the market. A live fetch of the leaderboard page on 2026-04-15 showed `claude-opus-4-6-thinking` ranked #1 in Text Arena Overall under Style Control, ahead of `claude-opus-4-6` at #2.

## Key facts extracted

- The page includes a visible `Style Control` selector and leaderboard rows.
- Top visible rows from the fetched HTML snapshot:
  - #1 `claude-opus-4-6-thinking` (Anthropic) — score 1502 ±5, votes 17,219.
  - #2 `claude-opus-4-6` (Anthropic) — score 1496 ±5, votes 18,377.
  - #3 `muse-spark` — score 1495 ±9, marked preliminary.
  - #4 `gemini-3.1-pro-preview` — score 1493 ±5.
  - #5 `gemini-3-pro` — score 1486 ±4.
- The score gap between #1 and #2 in the fetched snapshot is 6 points.
- The score gap between #1 and #4 is 9 points.
- Because the market uses alphabetical ordering only as a tiebreaker, a tie between `claude-opus-4-6-thinking` and `claude-opus-4-6` would resolve against the `-thinking` variant.

## Evidence directly stated by source

- The leaderboard page itself presents rank, model name, organization, score, uncertainty band, and vote counts.
- `claude-opus-4-6-thinking` is currently shown first.
- `claude-opus-4-6` is currently shown second.
- `Style Control` is a visible page control on the leaderboard surface.

## What is uncertain

- The source note is based on a fetched HTML snapshot two days before the market check time, not the final April 17 noon ET resolution snapshot.
- The page HTML is difficult to query in a perfectly structured way from shell because the app is heavily client-rendered; however, both web fetch and curl-based extraction pointed to the same top ordering.
- We do not know how quickly Arena scores may move over the next ~49 hours.
- We do not know whether the live page state at resolution will preserve the same ordering.

## Why this source may matter

It is the explicit contract source of truth. For this market, current leaderboard state is much more relevant than generalized product hype or third-party benchmark commentary.

## Possible impact on the question

This source strongly supports the current market favorite status for `claude-opus-4-6-thinking`, but it also reveals the main variant risk: the lead is narrow enough that small score movement or a tie could flip the outcome to `claude-opus-4-6` or another close competitor.

## Reliability notes

- High relevance because this is the stated resolution source.
- High recency because the snapshot was taken on 2026-04-15 for a 2026-04-17 check market.
- Moderate residual uncertainty because the source is dynamic and the market resolves at a future snapshot rather than immediately.