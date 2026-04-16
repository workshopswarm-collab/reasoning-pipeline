---
type: source_note
case_key: case-20260415-33c2f26e
dispatch_id: dispatch-case-20260415-33c2f26e-20260415T211658Z
analysis_date: 2026-04-15
persona: base-rate
domain: sports
subdomain: soccer
entity:
topic: Al Nassr vs Al Ettifaq market rules and source of truth
question: Will Al Nassr Saudi Club win on 2026-04-24?
driver:
date_created: 2026-04-15
source_name: Polymarket event page
source_type: market page / contract description
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
tags: [sports, soccer, polymarket, source-of-truth]
---

# Summary
The Polymarket market page provides the contract wording and resolution mechanics. It is the governing market surface for what counts as a Yes or No, but not the best source for estimating team strength.

## Key facts extracted
- The market asks whether Al Nassr wins the Saudi Professional League match scheduled for 2026-04-24.
- Yes resolves only if Al Nassr wins.
- No resolves for a draw, an Al Ettifaq win, or full cancellation with no makeup game.
- Only first 90 minutes plus stoppage time count.
- Primary resolution source is the official statistics of the event as recognized by the governing body or event organizers; credible reporting is fallback if no final official stats appear within two hours.

## Evidence directly stated by source
- Contract wording is explicit about win-only resolution.
- The page names official match statistics as the governing source of truth.

## What is uncertain
- The page does not provide team form, injuries, expected lineups, or odds context.
- It does not identify the exact official feed/provider that will be treated as authoritative if multiple public match centers exist.

## Why this source may matter
This is necessary to prevent a common sports-market mistake: overreading a likely favorable result without verifying that only a regulation-time win counts.

## Possible impact on the question
It slightly lowers a naive favorite-win probability versus any-to-advance or draw-no-bet style framing, because a draw is a No.

## Reliability notes
Reliable for contract interpretation and source-of-truth mechanics because it is the market's own rule surface. Not independent evidence on match quality or likely outcome.
