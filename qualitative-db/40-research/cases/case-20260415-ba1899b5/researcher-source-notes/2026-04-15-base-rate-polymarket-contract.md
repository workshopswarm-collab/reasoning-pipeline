---
type: source_note
case_key: case-20260415-ba1899b5
dispatch_id: dispatch-case-20260415-ba1899b5-20260415T121723Z
analysis_date: 2026-04-15
persona: base-rate
domain: markets
subdomain: prediction-markets
entity: netflix
topic: case-20260415-ba1899b5 | base-rate
question: Will Netflix Inc (NFLX) beat quarterly earnings?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket contract page for NFLX earnings beat market
source_type: market-contract
source_url: https://polymarket.com/event/nflx-quarterly-earnings-gaap-eps-04-16-2026-0pt76
source_date: 2026-04-15
credibility: medium
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [netflix]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [base-rate-finding]
tags: [contract, resolution, earnings, netflix, polymarket]
---

# Summary

This source defines the market mechanics. It states the estimated earnings date, strike, governing source of truth, fallback source, delayed-release clause, and rounding rules.

## Key facts extracted

- Market resolves Yes if Netflix reports GAAP EPS greater than $0.76 in its next quarterly earnings release.
- Governing source of truth is the GAAP EPS listed in Netflix's official earnings documents.
- If Netflix releases earnings without GAAP EPS, fallback source is the GAAP EPS figure reported by Seeking Alpha.
- If no such fallback figure is published within 96 hours of market close on the announcement day, the market resolves No.
- If Netflix does not release earnings within 45 calendar days of the estimated earnings date, the market resolves No.
- Figures are rounded to the nearest cent; diluted GAAP EPS is preferred unless only basic GAAP EPS is published.
- Estimated earnings date shown in the contract is April 16, 2026.

## Evidence directly stated by source

The contract page directly states all material resolution conditions and timing rules.

## What is uncertain

- The contract page itself is not the primary earnings source; it only defines how the market will resolve.
- It does not independently confirm Netflix's actual reporting schedule beyond the estimated date embedded in the market.

## Why this source may matter

This is the definitive source for what conditions must hold for a Yes resolution. It matters more than generic earnings-beat framing because date, rounding, and source-selection rules could matter if reporting is unusual.

## Possible impact on the question

It narrows the operational question to a simple threshold event with a clear governing source: reported diluted GAAP EPS must exceed $0.76 in the initial official earnings materials, subject to the release timing clause.

## Reliability notes

High reliability for contract mechanics; not an authoritative source for the actual earnings result itself.