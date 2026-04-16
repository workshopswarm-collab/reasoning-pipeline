---
type: source_note
case_key: case-20260414-4c35c81d
dispatch_id: dispatch-case-20260414-4c35c81d-20260414T204205Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: sports
subdomain: saudi-pro-league
entity:
topic: al-qadisiyah-vs-al-shabab-2026-04-23
question: Will Al Qadisiyah Saudi Club win on 2026-04-23?
driver: performance
date_created: 2026-04-14
source_name: Polymarket market page
source_type: market page / contract description
source_url: https://polymarket.com/event/spl-qad-sha-2026-04-23
source_date: 2026-04-14
credibility: medium
recency: current
stance: neutral
certainty: medium
importance: high
novelty: low
agent: catalyst-hunter
related_entities: []
related_drivers:
  - performance
upstream_inputs: []
downstream_uses: []
tags: [market-structure, resolution-source, sports-market]
---

# Summary

This source establishes the contract mechanics and the governing source-of-truth hierarchy for the market. It says the match is scheduled for 2026-04-23, resolves Yes only if Al Qadisiyah win, and counts only first 90 minutes plus stoppage time. It also specifies that official statistics recognized by the governing body or event organizers are the primary resolution source, with credible-reporting fallback only if official final stats are unavailable within two hours.

## Key facts extracted

- Market is for the upcoming Saudi Professional League game scheduled for 2026-04-23.
- Yes resolves only if Al Qadisiyah win.
- Draw or Al Shabab win resolves No.
- Postponement keeps market open until the game is completed.
- Full cancellation with no make-up game resolves No.
- Only regular time plus stoppage time counts.
- Primary source of truth is official match statistics recognized by the governing body or organizers.
- Credible consensus reporting is fallback only if official stats are not published within two hours.

## Evidence directly stated by source

The page explicitly states the 90-minute-only condition and the official-statistics-first resolution rule.

## What is uncertain

The page does not itself provide team news, standings, odds history, or independent evidence about likely match strength. It is a contract/market surface, not a sports-information source.

## Why this source may matter

This source is mandatory for interpreting what counts as a win and for determining whether extra-time or a postponement would matter. It also narrows the resolution risk materially.

## Possible impact on the question

It lowers rule ambiguity: the analysis should focus on standard full-time win probability and scheduled-match completion risk, not cup-style extra-time paths.

## Reliability notes

Reliable for contract terms and source-of-truth hierarchy because it is the market’s own published description. Not reliable as an independent indicator of match probability beyond current market price and wording.