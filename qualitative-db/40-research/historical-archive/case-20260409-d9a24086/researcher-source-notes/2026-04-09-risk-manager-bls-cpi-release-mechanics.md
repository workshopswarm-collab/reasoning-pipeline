---
type: source_note
case_key: case-20260409-d9a24086
dispatch_id: dispatch-case-20260409-d9a24086-20260409T165631Z
analysis_date: 2026-04-09
persona: risk-manager
domain: economics
subdomain: macro-data-and-indicators
entity: bureau-of-labor-statistics
topic: march-2026-cpi-release-mechanics
question: Will monthly inflation increase by 0.8% or more in March?
driver: operational-risk
date_created: 2026-04-09
source_name: BLS Consumer Price Index Summary - 2026 M02 Results
source_type: primary
source_url: https://www.bls.gov/news.release/cpi.nr0.htm
source_date: 2026-03-11
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [bureau-of-labor-statistics]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-d9a24086/researcher-analyses/2026-04-09/dispatch-case-20260409-d9a24086-20260409T165631Z/personas/risk-manager.md]
tags: [source-note, bls, cpi, resolution-source, seasonal-adjustment]
---

# Summary

This source is the direct BLS CPI release surface and also contains the key methodological language relevant to this market: the market settles on the seasonally adjusted one-month CPI-U change for March 2026, reported to one decimal place.

## Key facts extracted

- February 2026 CPI-U all items increased 0.3% month-over-month on a seasonally adjusted basis.
- The release explicitly states that the March 2026 CPI will be released on April 10, 2026 at 8:30 a.m. ET.
- BLS says short-term price-trend analysis usually prefers seasonally adjusted changes.
- BLS states seasonal factors are updated each February and used to revise the previous 5 years of seasonally adjusted data.
- BLS notes CPI-U is considered final when released.
- BLS gives a 1-month all-items CPI standard error example of 0.04 percentage point, implying boundary outcomes near a one-decimal threshold can be sensitive to underlying measurement noise even if settlement uses the published figure.

## Evidence directly stated by source

- Governing resolution metric is available on the authoritative BLS CPI release surface.
- Seasonal adjustment is not incidental; it is the intended short-term analytical series and is revised using updated seasonal factors each February.
- The next release timing is fixed for April 10, 2026 at 8:30 a.m. ET.

## What is uncertain

- This source does not provide a March nowcast or probability distribution.
- It does not tell us whether March will print 0.7% versus 0.8%; it only defines the authoritative measurement framework and recent baseline.

## Why this source may matter

It is the clearest primary source for both contract mechanics and the seasonal-adjustment requirement. For this market, the biggest operational risk is not source ambiguity but overconfidence before the official release.

## Possible impact on the question

This source lowers settlement ambiguity: the published BLS seasonally adjusted CPI-U month-over-month figure for March 2026 is the source of truth. It also supports the risk view that pre-release confidence should be discounted because the contract resolves on one official rounded print.

## Reliability notes

Very high reliability for settlement mechanics and methodology because it is the authoritative producer. Low usefulness for directional forecasting by itself because it is backward-looking and not a forecast source.