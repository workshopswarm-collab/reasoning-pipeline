---
type: source_note
case_key: case-20260416-bacb47cd
dispatch_id: dispatch-case-20260416-bacb47cd-20260416T101708Z
analysis_date: 2026-04-16
persona: market-implied
domain: weather
subdomain: daily-temperature-threshold
entity:
topic: highest-temperature-in-seoul-on-april-17-2026-18corhigher
question: Will the highest temperature recorded at Incheon Intl Airport Station on 2026-04-17 be 18°C or higher?
driver:
date_created: 2026-04-16
source_name: Polymarket market page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/highest-temperature-in-seoul-on-april-17-2026
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-bacb47cd/researcher-analyses/2026-04-16/dispatch-case-20260416-bacb47cd-20260416T101708Z/personas/market-implied.md
tags: [weather, polymarket, resolution-rules, price-signal]
---

# Summary

This source establishes both the live market-implied baseline and the governing settlement mechanics.

## Key facts extracted

- The contract currently prices `18°C or higher` at about `71%`.
- The market resolves using the **highest temperature recorded at the Incheon Intl Airport Station** on `17 Apr 2026`.
- The named settlement surface is **Wunderground daily history for station RKSI**.
- Resolution uses **whole degrees Celsius**.
- The market cannot resolve Yes until all data for that date is finalized.

## Evidence directly stated by source

- The market page explicitly states the source-of-truth surface and threshold bucket.
- The same page shows the distribution across adjacent buckets, with `17°C` around `21%`, implying the market sees the threshold as close but more likely than not to be met.

## What is uncertain

- The page does not itself prove what the final Apr 17 temperature will be.
- The page does not explain why traders prefer 18°C+, only that they currently do.

## Why this source may matter

This is the authoritative contract-definition source for what counts, what date counts, how temperature is rounded, and what station governs settlement.

## Possible impact on the question

It frames the entire research task: the relevant question is not generic Seoul city weather but whether **RKSI / Incheon Intl Airport Station** will print a finalized whole-degree high of at least 18°C on Apr 17 local date.

## Reliability notes

Strong for contract mechanics and live market baseline; not independently reliable for meteorological truth.