---
type: source_note
case_key: case-20260415-33c2f26e
dispatch_id: dispatch-case-20260415-33c2f26e-20260415T211658Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: sports
subdomain: soccer
entity:
topic: polymarket contract rules and timing
question: Will Al Nassr Saudi Club win on 2026-04-24?
driver:
date_created: 2026-04-15
source_name: Polymarket market page
source_type: market contract / resolution rules
source_url: https://polymarket.com/event/spl-nsr-ett-2026-04-24
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-33c2f26e/researcher-analyses/2026-04-15/dispatch-case-20260415-33c2f26e-20260415T211658Z/personas/catalyst-hunter.md
tags: [polymarket, resolution-rules, source-note, saudi-pro-league]
---

# Summary

This source establishes the contract wording, timing, and governing source-of-truth for the market.

## Key facts extracted

- Market asks whether Al Nassr Saudi Club wins the upcoming game scheduled for April 24, 2026.
- "Yes" resolves only if Al Nassr wins.
- Otherwise the market resolves "No".
- If postponed, market stays open until the game is completed.
- If canceled entirely with no make-up game, market resolves "No".
- Only result within first 90 minutes plus stoppage time counts.
- Primary resolution source is official statistics of the event as recognized by the governing body or event organizers.
- If final official match statistics are not published within 2 hours after conclusion, credible reporting consensus may be used.

## Evidence directly stated by source

The source directly states the settlement mechanics, the timing exception for postponement/cancellation, and that extra time / penalties do not count.

## What is uncertain

- The market page does not itself identify the exact official competition page that will publish the final recognized score.
- It does not provide team news, venue specifics, or lineup timing.

## Why this source may matter

This is the governing contract surface. For a simple match-winner market, the most important catalyst is the match itself, but the contract also makes postponement/cancellation handling and 90-minute-only settlement explicit.

## Possible impact on the question

It lowers resolution ambiguity. The main live catalyst before settlement is any credible information that changes expected win probability before kickoff; the settlement source itself is straightforward.

## Reliability notes

High reliability for contract wording and resolution mechanics because this is the market operator's own rules page. It is not an independent performance source for team strength.