---
type: source_note
case_key: case-20260415-7f8f0d04
dispatch_id: dispatch-case-20260415-7f8f0d04-20260415T104754Z
analysis_date: 2026-04-15
persona: risk-manager
domain: tech-ai
subdomain: model-rankings
entity:
topic: LM Arena leaderboard spot check
question: Will claude-opus-4-6-thinking be the top AI model on April 17, 2026 (Style Control On)?
driver: reliability
date_created: 2026-04-15
source_name: LM Arena text leaderboard
source_type: primary external resolution source / live leaderboard snapshot
source_url: https://arena.ai/leaderboard/text
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [anthropic, claude]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [risk-manager finding, risk-manager evidence map]
tags: [lm-arena, leaderboard, style-control, snapshot, verification]
---

# Summary

A live fetch of the LM Arena text leaderboard showed an Anthropic model at rank #1 with score about 1502 ± 5, ahead of the next listed Anthropic model at about 1496 ± 5 and other close competitors such as Meta and Google in the high-1490s. This supports the broad thesis that an Anthropic model is currently leading, but the extracted page text had poor model-name legibility, which creates a real risk for exact contract mapping to `claude-opus-4-6-thinking`.

## Key facts extracted

- The fetched leaderboard content is from the stated resolution source family (`lmarena.ai`, redirected to `arena.ai`).
- The top row in the fetch appeared to be an Anthropic proprietary model with score approximately 1502 ± 5.
- The next few rows were tightly clustered, including another Anthropic model near 1496 ± 5 and non-Anthropic models around 1495 and 1493.
- The leaderboard appears live and subject to movement before the April 17, 2026 noon ET check.

## Evidence directly stated by source

- At the time of the fetch, an Anthropic model appears to lead the text leaderboard.
- The margin is not enormous; nearby models are within roughly single-digit points.
- The page extraction quality did not clearly expose full model strings in the retrieved text.

## What is uncertain

- Whether the #1 Anthropic row is exactly `claude-opus-4-6-thinking` rather than another Anthropic variant.
- Whether style control on is definitely represented in the fetch extraction rather than inferred from the page / market wording.
- Whether the current ordering will persist until the actual April 17 noon ET check.

## Why this source may matter

This is the core source-of-truth family for eventual resolution. It gives direct evidence that the broad direction of the market is not crazy: Anthropic currently looks highly competitive and possibly first. But it also reveals the main underpriced risk: exact-string mapping and small leaderboard movement can still break a very high-confidence YES thesis.

## Possible impact on the question

Supports a high probability that the market is directionally right, but not a near-certainty. The evidence is stronger for `an Anthropic model is near/at the top` than for `the exact contract string will definitely be top at the precise future check time`.

## Reliability notes

This is the most important primary external source for eventual resolution, but the fetch extraction is imperfect. The model-name visibility problem lowers confidence in exact contract mapping even while leaving high confidence that Anthropic is currently near the top.