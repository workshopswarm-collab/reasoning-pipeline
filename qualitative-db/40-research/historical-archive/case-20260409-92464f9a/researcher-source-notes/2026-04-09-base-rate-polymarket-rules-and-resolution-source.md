---
type: source_note
case_key: case-20260409-92464f9a
dispatch_id: dispatch-case-20260409-92464f9a-20260409T201552Z
analysis_date: 2026-04-09
persona: base-rate
domain: climate
subdomain: global-temperature
entity: nasa
topic: March 2026 global temperature bracket resolution mechanics
question: Will global temperature increase by more than 1.29ºC in March 2026?
driver: reliability
date_created: 2026-04-09
source_name: Polymarket market rules page for March 2026 Temperature Increase (ºC)
source_type: market-rules
source_url: https://polymarket.com/event/march-2026-temperature-increase-c
source_date: 2026-04-09
credibility: medium
recency: current
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [nasa]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [base-rate.md, base-rate.sidecar.json, evidence/base-rate.md]
tags: [polymarket, resolution-source, market-rules, nasa-gistemp]
---

# Summary

The market rules specify that resolution is determined by NASA GISS Global Land-Ocean Temperature Index data for March 2026, specifically the value in `GLB.Ts+dSST.txt` under column `Mar` and row `2026`. The rules also say that once data becomes available, later revisions do not matter. If the NASA index is permanently unavailable, other NASA information may be used.

## Key facts extracted

- Primary resolution source is NASA GISS `GLB.Ts+dSST.txt`.
- The exact resolving cell is the `Mar` column in row `2026`.
- A bracket resolves immediately once that March 2026 figure becomes available.
- Later revisions do not affect resolution.
- If NASA’s Global Temperature Index is permanently unavailable, other NASA information may be used.
- The fallback clause appears internally inconsistent: it says that if no information for **February 2026** is provided by NASA by May 1, 2026 11:59 PM ET, the market resolves to the lowest range bracket, even though the market concerns March 2026.

## Evidence directly stated by source

- The market explicitly names NASA as the governing source of truth.
- Resolution depends on a structured release mechanism, not on a generic climate-news consensus.
- The typo / mismatch around “February 2026” creates non-zero rules ambiguity, but only in the fallback clause.

## What is uncertain

- Whether the February reference is a clerical error or an intentional fallback trigger.
- Whether Polymarket would apply that fallback literally if NASA delayed March 2026 publication beyond May 1.
- Whether the market can resolve before the listed close time if NASA posts the data earlier on the same date.

## Why this source may matter

This is the governing contract language. For a date-sensitive and rule-sensitive market, the mechanics matter as much as the climatological level.

## Possible impact on the question

The rules make this closer to a question about whether the relevant NASA March 2026 table entry, once released, exceeds 1.29°C, with a small but real ambiguity arising from the fallback clause.

## Reliability notes

Polymarket is authoritative for contract wording but not for the climate data itself. The page is reliable for settlement mechanics, while NASA remains the authoritative data source for the underlying statistic.
