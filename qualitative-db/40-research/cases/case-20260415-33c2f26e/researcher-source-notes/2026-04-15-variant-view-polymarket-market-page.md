---
type: source_note
case_key: case-20260415-33c2f26e
dispatch_id: dispatch-case-20260415-33c2f26e-20260415T211658Z
analysis_date: 2026-04-15
persona: variant-view
domain: sports
subdomain: soccer
entity:
topic: Al Nassr vs Al Ettifaq market framing
question: Will Al Nassr Saudi Club win on 2026-04-24?
driver:
date_created: 2026-04-15
source_name: Polymarket market page
source_type: market page / contract text
source_url: https://polymarket.com/event/spl-nsr-ett-2026-04-24
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: variant-view
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract, resolution]
---

# Summary

This source establishes the market framing, current implied probability context, and the governing resolution logic for the case.

## Key facts extracted

- The market is for the upcoming Saudi Professional League game scheduled for April 24, 2026 between Al Nassr Saudi Club and Al Ettifaq Saudi Club.
- If Al Nassr wins, the market resolves Yes; otherwise No.
- Resolution is based only on the outcome within the first 90 minutes plus stoppage time.
- If postponed, the market stays open until the game is completed.
- If canceled entirely with no make-up game, the market resolves No.
- The primary resolution source is official statistics recognized by the governing body or event organizers; if unavailable within two hours, a consensus of credible reporting may be used instead.
- The visible market page showed volume around $112.51K at fetch time.

## Evidence directly stated by source

The market page directly states the timing window, settlement rule, postponement/cancellation treatment, and official-stats-first source-of-truth hierarchy.

## What is uncertain

- The fetchable market page text did not expose a fully structured odds history or all surrounding market microstructure.
- The page itself is not an independent sports-information source for team strength or fixture certainty.

## Why this source may matter

It is the governing contract surface for what counts as a win and how the market resolves, which matters for avoiding hidden assumptions about extra time, penalties, or cancellation handling.

## Possible impact on the question

This source narrows the operative question to a regulation-time match result and reduces resolution ambiguity. It does not itself prove how likely Al Nassr is to win.

## Reliability notes

Reliable for contract interpretation and current market framing, but not independent evidence on soccer strength, lineup availability, or fixture confirmation beyond the market's own listing.