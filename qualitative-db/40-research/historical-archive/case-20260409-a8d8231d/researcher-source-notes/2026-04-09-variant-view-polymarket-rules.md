---
type: source_note
case_key: case-20260409-a8d8231d
dispatch_id: dispatch-case-20260409-a8d8231d-20260409T183257Z
analysis_date: 2026-04-09
persona: variant-view
domain: climate
subdomain: market-resolution
entity:
topic: march-2026-global-temperature-bracket
question: Will global temperature increase by between 1.25ºC and 1.29ºC in March 2026?
driver: reliability
date_created: 2026-04-09
source_name: Polymarket market description and resolution rules
source_type: market_rules
source_url: https://polymarket.com/event/march-2026-temperature-increase-c
source_date: 2026-04-09
credibility: medium-high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: []
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [market-rules, settlement, polymarket, contract]
---

# Summary

The market rules explicitly tie resolution to NASA GISS’s `GLB.Ts+dSST.txt` March 2026 value and say a bracket match is necessary and sufficient once data becomes available, regardless of later revisions.

## Key facts extracted

- Market resolves according to the value reported by the Global Land-Ocean Temperature Index for March 2026 when released.
- Necessary and sufficient condition: anomaly within the named bracket for March 2026.
- Primary resolution source: the `Mar` column in row `2026` of `GLB.Ts+dSST.txt`.
- If NASA’s temperature index is permanently unavailable, other information from NASA may be used.
- A fallback clause says if no information for `February 2026` is provided by NASA by May 1, 2026, 11:59 PM ET, the market resolves to the lowest range bracket.

## Evidence directly stated by source

- The source names the exact table and exact row/column to use.
- It states revisions after availability do not matter.

## What is uncertain

- The fallback clause mentioning February rather than March appears inconsistent with the rest of the contract and may be a drafting error.
- The source does not itself define whether `between 1.25ºC and 1.29ºC` is inclusive, but the market is a named bracket market and 1.28°C clearly lies inside the interval either way.

## Why this source may matter

This source determines what counts and what does not count for settlement. It narrows the analysis away from other datasets, other agencies, or later revisions.

## Possible impact on the question

Because the contract is source-specific and revision-insensitive after release, the key variant risk is not climate uncertainty but settlement-mechanics or drafting ambiguity. Once NASA posts March 2026 = 1.28°C, those mechanics still point strongly to YES.

## Reliability notes

- High relevance for contract interpretation.
- Some source-quality ambiguity from the February fallback clause, but the main settlement instruction is otherwise unusually explicit.
- This is not independent of the market operator, so it must be paired with the NASA primary source rather than used alone.
