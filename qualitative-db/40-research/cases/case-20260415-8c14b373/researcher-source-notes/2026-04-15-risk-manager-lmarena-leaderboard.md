---
type: source_note
case_key: case-20260415-8c14b373
dispatch_id: dispatch-case-20260415-8c14b373-20260415T130923Z
analysis_date: 2026-04-15
persona: risk-manager
domain: tech-ai
subdomain: frontier-model-benchmarks
entity:
topic: chatbot-arena-text-overall-leaderboard
question: Will claude-opus-4-6-thinking be the best AI model on April 17, 2026?
driver: reliability
date_created: 2026-04-15
source_name: Chatbot Arena Text Leaderboard
source_type: primary_resolution_source
source_url: https://lmarena.ai/leaderboard/text
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [anthropic, claude, openai, gemini, grok]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-8c14b373/researcher-analyses/2026-04-15/dispatch-case-20260415-8c14b373-20260415T130923Z/personas/risk-manager.md]
tags: [chatbot-arena, leaderboard, primary-source, resolution-source]
---

# Summary

This source is the governing resolution surface named by the market rules: the "Text Arena | Overall" leaderboard with style control off at lmarena.ai / arena.ai.

## Key facts extracted

- Current leaderboard snapshot shows `claude-opus-4-6-thinking` ranked #1 with rating 1502.33, confidence interval 1497.14-1507.53, and 17,219 votes.
- The closest named competitors in the fetched page data are:
  - `claude-opus-4-6` ranked #2 at 1495.68
  - `gemini-3.1-pro-preview` ranked #4 at 1492.98
  - `gemini-3-pro` ranked #5 at 1485.84
  - `grok-4.20-beta1` ranked #6 at 1484.89
  - `gpt-5.4-high` ranked #7 at 1481.44
- The page header explicitly identifies the relevant table as `Text Arena` and `Overall`.
- The current lead over the nearest visible competitor (`claude-opus-4-6`) is about 6.65 Elo.
- The published uncertainty bands overlap among the top entries, so current leadership is real but not mathematically locked.

## Evidence directly stated by source

- The page contains serialized leaderboard entry data for the named models and scores.
- The page labels the relevant ranking surface as "Text Arena | Overall".
- The entry names match the market-group model naming convention closely enough to support a direct mapping check for `claude-opus-4-6-thinking`.

## What is uncertain

- This source is a live leaderboard, so the relevant state is the value at the market check time, not the value on 2026-04-15.
- The extracted page did not cleanly expose a visible textual string for "style control off," though the market rules say the check uses that mode.
- The uncertainty intervals and live rankings imply that a new release, rating update, or leaderboard reshuffle before April 17 noon ET could still change first place.

## Why this source may matter

It is the explicit primary resolution source, so it governs both the identity of the winning model and the exact ranking mechanics that matter for settlement.

## Possible impact on the question

If the leaderboard state remained unchanged through the April 17, 2026 12:00 PM ET check, this source supports a YES resolution for `claude-opus-4-6-thinking`. But because the market resolves off a future check on a live ranking, the same source also defines the key risk: any leaderboard movement before that deadline could flip the answer.

## Reliability notes

High reliability as the named source of truth for settlement. Lower reliability for forward prediction because it is not static and because top-rank uncertainty bands overlap.