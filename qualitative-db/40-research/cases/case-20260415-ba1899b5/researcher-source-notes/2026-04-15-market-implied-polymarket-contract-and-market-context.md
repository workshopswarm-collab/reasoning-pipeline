---
type: source_note
case_key: case-20260415-ba1899b5
dispatch_id: dispatch-case-20260415-ba1899b5-20260415T121723Z
analysis_date: 2026-04-15
persona: market-implied
domain: culture
subdomain: streaming
entity: netflix
topic: Polymarket resolution mechanics and current pricing
question: Will Netflix Inc (NFLX) beat quarterly earnings?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and contract description
source_type: market rule / exchange listing
source_url: https://polymarket.com/event/nflx-quarterly-earnings-gaap-eps-04-16-2026-0pt76
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: market-implied
related_entities: [netflix]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [source-note, polymarket, resolution, contract]
---

# Summary

The Polymarket market page provides the active market-implied probability and the operative contract wording. As of assignment time, the price is 0.945, implying roughly 94.5% probability of a beat. The rules make this a narrow threshold question, not a broad 'good quarter' question.

## Key facts extracted

- Current price supplied in case context is 0.945.
- Market resolves Yes only if Netflix reports GAAP EPS greater than $0.76 for the relevant quarter.
- Official company earnings documents are the primary resolution source.
- If official documents omit GAAP EPS, fallback is Seeking Alpha's GAAP EPS figure, with a 96-hour publication condition.
- Figures are rounded to the nearest cent using standard rounding.
- GAAP EPS means diluted GAAP EPS unless only basic GAAP EPS is published.
- If Netflix does not release earnings within 45 calendar days of the estimated earnings date, market resolves No.

## Evidence directly stated by source

- Threshold is strictly greater than $0.76.
- The governing source of truth is Netflix's official earnings documents.
- The contract is date-sensitive and has explicit fallback / rounding mechanics.

## What is uncertain

- The market page does not itself justify why traders are pricing 94.5%; it only states the rules and market level.
- It does not independently verify the expected earnings date beyond the market description.

## Why this source may matter

This is the source for both the market-implied baseline and the exact resolution mechanics. Because the threshold is strict and rounded to the nearest cent, even a result that exactly matches prior guidance at $0.76 resolves No.

## Possible impact on the question

The contract structure raises the burden for a Yes at such an extreme price: traders are effectively assuming not just a strong quarter, but a printed diluted GAAP EPS of at least $0.77 after rounding, released on time in official company documents.

## Reliability notes

Authoritative for market wording and live market context, but not for underlying fundamentals. The strongest use is contract interpretation, not independent evidence about Netflix operating performance.