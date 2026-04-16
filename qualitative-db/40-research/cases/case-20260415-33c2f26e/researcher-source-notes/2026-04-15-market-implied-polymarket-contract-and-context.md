---
type: source_note
case_key: case-20260415-33c2f26e
dispatch_id: dispatch-case-20260415-33c2f26e-20260415T211658Z
analysis_date: 2026-04-15
persona: market-implied
domain: sports
subdomain: soccer
entity:
topic: al-nassr-vs-al-ettifaq-2026-04-24
question: Will Al Nassr Saudi Club win on 2026-04-24?
driver:
date_created: 2026-04-15
source_name: Polymarket market page and contract text
source_type: market_contract
source_url: https://polymarket.com/event/spl-nsr-ett-2026-04-24
source_date: 2026-04-15
credibility: medium
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses: [market-implied-finding]
tags: [polymarket, contract, resolution, market-price]
---

# Summary

This source establishes the exact market contract, current pricing context, and governing resolution rules for the case.

## Key facts extracted

- The market asks whether Al Nassr Saudi Club will win the upcoming Saudi Professional League game against Al Ettifaq Saudi Club.
- The event page shows substantial market activity and a current price consistent with a very high implied probability for Al Nassr.
- Resolution is based on the match result in the first 90 minutes plus stoppage time only.
- If the game is postponed, the market stays open until completed.
- If the game is canceled entirely with no make-up game, the market resolves No.
- Primary resolution source is official statistics recognized by the governing body or event organizers; if unavailable within 2 hours, consensus of credible reporting may be used.

## Evidence directly stated by source

- "If Al Nassr Saudi Club wins, this market will resolve to 'Yes'. Otherwise, this market will resolve to 'No'."
- "This market refers only to the outcome within the first 90 minutes of regular play plus stoppage time."
- "The primary resolution source for this market is the official statistics of the event as recognized by the governing body or event organizers."

## What is uncertain

- The page does not itself explain why the market is pricing Al Nassr so aggressively.
- It does not provide team-form, injuries, or bookmaker line context in the extracted view.

## Why this source may matter

This is the governing market-contract source. It anchors both the implied probability comparison and the resolution/source-of-truth analysis.

## Possible impact on the question

It confirms the market is a simple 90-minute home-win question, which reduces contract ambiguity. That makes public strength signals such as standings and matchup context more directly relevant.

## Reliability notes

Strong for contract wording and source-of-truth interpretation. Weak for independent validation of whether the extreme price is efficient.