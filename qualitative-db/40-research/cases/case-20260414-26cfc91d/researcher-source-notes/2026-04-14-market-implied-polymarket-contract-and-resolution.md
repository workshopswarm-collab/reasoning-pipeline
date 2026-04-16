---
type: source_note
case_key: case-20260414-26cfc91d
dispatch_id: dispatch-case-20260414-26cfc91d-20260414T181516Z
analysis_date: 2026-04-14
persona: market-implied
domain: sports
subdomain: soccer
entity:
topic: case-20260414-26cfc91d | market-implied
question: Will FC Internazionale Milano win on 2026-04-17?
driver:
date_created: 2026-04-14
source_name: Polymarket market page and resolution rules
source_type: market_contract
source_url: https://polymarket.com/event/sea-int-cag-2026-04-17
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [polymarket, resolution, source-of-truth, serie-a]
---

# Summary

This source establishes the exact contract terms, current market framing, and governing resolution logic for the Inter vs Cagliari market.

## Key facts extracted

- The market asks whether FC Internazionale Milano will win the Serie A game scheduled for April 17, 2026 against Cagliari Calcio.
- If Inter wins, the market resolves Yes; otherwise No.
- Only the result within first 90 minutes plus stoppage time counts.
- If postponed, the market stays open until the game is completed.
- If canceled entirely with no make-up game, the market resolves No.
- Primary resolution source is the official statistics of the event as recognized by the governing body or event organizers; if those are not published within 2 hours after conclusion, consensus credible reporting can be used.

## Evidence directly stated by source

The market page directly states the resolution criteria and source-of-truth hierarchy.

## What is uncertain

The market page does not itself provide a detailed evidentiary basis for the 0.815 price, only the contract mechanics and current traded framing.

## Why this source may matter

It is the authoritative surface for what counts for settlement. In a three-way soccer result market, the draw matters materially because the contract resolves No unless Inter wins in regulation.

## Possible impact on the question

This source prevents overcounting extra time or generic "advance/win" language. It supports interpreting the price strictly as Inter win probability in regulation plus stoppage time, not broader team strength.

## Reliability notes

High reliability for contract wording and settlement mechanics because it is the primary market source. It is not independent evidence about team strength, injuries, or form.