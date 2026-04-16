---
type: source_note
case_key: case-20260415-33c2f26e
dispatch_id: dispatch-case-20260415-33c2f26e-20260415T211658Z
analysis_date: 2026-04-15
persona: risk-manager
domain: sports
subdomain: soccer
entity:
topic: al-nassr-vs-al-ettifaq-2026-04-24
question: Will Al Nassr Saudi Club win on 2026-04-24?
driver:
date_created: 2026-04-15
source_name: Polymarket market page
source_type: market/rules
source_url: https://polymarket.com/event/spl-nsr-ett-2026-04-24
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [polymarket, market-rules, source-note, sports]
---

# Summary

This source establishes the market contract and governing source of truth. It does not provide competitive-strength evidence, but it does define exactly what counts for resolution.

## Key facts extracted

- The market asks whether Al Nassr wins the upcoming Saudi Professional League game scheduled for April 24, 2026.
- "Yes" resolves only if Al Nassr wins.
- Any non-win result resolves "No".
- Only the result within the first 90 minutes plus stoppage time counts.
- If the game is postponed, the market remains open until played.
- If canceled entirely with no make-up game, the market resolves "No".
- Primary resolution source is official statistics recognized by the governing body or event organizers; if not published within 2 hours, a consensus of credible reporting may be used.

## Evidence directly stated by source

Direct contract wording on win-only resolution, postponement/cancellation handling, and the official-statistics-first source-of-truth rule.

## What is uncertain

- The page does not identify the specific official competition site likely to serve as the governing body statistics source.
- The page does not itself provide any form, standings, or lineup information.

## Why this source may matter

This is the key source for avoiding a resolution mistake. For a favorite-priced soccer market, the main contract risk is forgetting that draws and away wins both resolve "No" and that extra time does not matter.

## Possible impact on the question

This source slightly increases caution relative to naive "better team should advance" thinking because only a regulation win counts. It also frames the correct downside tail: draw risk matters materially.

## Reliability notes

Reliable for contract interpretation because it is the market’s own rules surface. Not sufficient by itself for sporting probability estimation.