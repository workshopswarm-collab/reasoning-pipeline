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
source_name: Polymarket market description for top AI model on April 17 style control on
source_type: market contract / resolution criteria
source_url: https://polymarket.com/event/top-ai-model-on-april-17-style-control-on
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-7f8f0d04/researcher-analyses/2026-04-15/dispatch-case-20260415-7f8f0d04-20260415T104754Z/personas/base-rate.md]
tags: [polymarket, resolution, chatbot-arena, style-control-on]
---

# Summary

This source is the governing contract text for the market. It specifies that resolution depends on the model with the highest arena score under the Chatbot Arena `Text Arena | Overall` leaderboard with style control on, checked on April 17, 2026 at 12:00 PM ET.

## Key facts extracted

- Governing source of truth is the Chatbot Arena LLM Leaderboard at `https://lmarena.ai/`.
- Resolution uses the `Leaderboard` tab, specifically the `Text Arena | Overall` leaderboard with style control on.
- Check time is April 17, 2026, 12:00 PM ET.
- Ranking is determined first by arena score, then by alphabetical order of model names as listed in the market group if there is a score tie.
- Example given in contract text implies `claude-opus-4-6` would beat `claude-opus-4-6-thinking` on a tie.
- If the resolution source is unavailable at the specified time, the market stays open until the first later check when the leaderboard returns.

## Evidence directly stated by source

- The market is not asking about current rank today; it asks who will be first at the specified future check time.
- Multiple conditions must hold for YES on this contract: the relevant model string must appear on the applicable leaderboard, the score used must be under style control on, and no other listed competitor can have a higher score at the check time.
- Tie mechanics are material because the named model loses alphabetical tiebreaks against its non-`-thinking` counterpart.

## What is uncertain

- The market description does not itself identify the current top model or the current rank of `claude-opus-4-6-thinking`; that must be checked separately.
- It does not define the exact fallback source if Chatbot Arena becomes permanently unavailable.

## Why this source may matter

This is the primary source for contract interpretation. Any forecast has to be grounded in these exact mechanics, especially the date/time check and alphabetical tie rule.

## Possible impact on the question

The source pushes analysis toward operational and reliability considerations around leaderboard persistence, exact naming, and tie risk rather than only raw model capability narratives.

## Reliability notes

High reliability for resolution mechanics because it is the contract text itself. It is not independent evidence about likely leaderboard movement.