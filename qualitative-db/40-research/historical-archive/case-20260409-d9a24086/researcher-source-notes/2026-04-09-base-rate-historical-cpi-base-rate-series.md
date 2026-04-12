---
type: source_note
case_key: case-20260409-d9a24086
dispatch_id: dispatch-case-20260409-d9a24086-20260409T165631Z
analysis_date: 2026-04-09
persona: base-rate
domain: economics
subdomain: macro-data-and-indicators
entity:
topic: march-2026-cpi-threshold
question: Will monthly inflation increase by 0.8% or more in March?
driver: seasonality
date_created: 2026-04-09
source_name: FRED CPIAUCSL monthly series used for historical base-rate calculation
source_type: economic data mirror
source_url: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: [macro, seasonality]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-d9a24086/researcher-analyses/2026-04-09/dispatch-case-20260409-d9a24086-20260409T165631Z/personas/base-rate.md]
tags: [cpi, inflation, base-rate, historical-series]
---

# Summary

Used the seasonally adjusted CPIAUCSL monthly index history from FRED as a contextual verification source to estimate how often a 0.8% or greater monthly CPI print occurs, especially in March.

## Key facts extracted

- Using the CPIAUCSL monthly level series and calculating month-over-month percent changes rounded to one decimal place, 0.8%+ monthly CPI prints occurred 79 times in 948 months since 1948, about 8.3% overall.
- For March specifically, 0.8%+ occurred 7 times in 79 March observations, about 8.9% overall.
- Since 2000, March reached 0.8%+ only once in 26 observations: March 2022 at 1.1%.
- Since 2024, observed monthly prints have stayed in the 0.0% to 0.4% range through the latest available data mirrored in the file.
- Recent 0.8%+ months are concentrated in the 2021-2022 inflation surge regime.

## Evidence directly stated by source

- The source directly provides the seasonally adjusted CPI-U level series by month.
- The 0.8%+ frequency statistics are derived calculations from that level series, not verbatim source language.

## What is uncertain

- FRED is a trusted mirror, but not itself the named resolution authority.
- Rounded month-over-month changes derived from the mirrored index should match BLS history in ordinary use, but the exact historical seasonal-adjustment revision state could differ from archived contemporaneous releases.
- The series currently has missing values for some months affected by the 2025 appropriations lapse, which slightly limits very recent continuity but does not matter for the long-run base-rate result.

## Why this source may matter

This is the cleanest compact way to quantify the outside-view prior. The threshold is not impossible, but it is clearly uncommon, and in recent March data it has been exceptionally rare outside the 2022 inflation spike.

## Possible impact on the question

Historical frequency pushes strongly against a 94.65% market probability for "yes." A base-rate-informed estimate should remain well below the market unless one has strong case-specific evidence that March 2026 resembles the 2021-2022 surge regime.

## Reliability notes

High-quality contextual data source because FRED mirrors official CPI series and is widely used, but it is still secondary/contextual relative to BLS. Best used for historical frequency and verification rather than final settlement.
