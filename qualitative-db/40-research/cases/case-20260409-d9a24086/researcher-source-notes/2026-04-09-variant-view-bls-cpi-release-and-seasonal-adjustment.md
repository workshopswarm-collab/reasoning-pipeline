---
type: source_note
case_key: case-20260409-d9a24086
dispatch_id: dispatch-case-20260409-d9a24086-20260409T165631Z
analysis_date: 2026-04-09
persona: variant-view
domain: economics
subdomain: macro-data-and-indicators
entity: bureau-of-labor-statistics
topic: march-2026-cpi-resolution-mechanics
question: Will monthly inflation increase by 0.8% or more in March?
driver: reliability
date_created: 2026-04-09
source_name: BLS CPI release pages and seasonal-adjustment FAQ
source_type: primary
source_url: https://www.bls.gov/news.release/cpi.nr0.htm
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities:
  - bureau-of-labor-statistics
related_drivers:
  - reliability
  - operational-risk
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260409-d9a24086/researcher-analyses/2026-04-09/dispatch-case-20260409-d9a24086-20260409T165631Z/personas/variant-view.md
tags:
  - source-note
  - cpi
  - bls
  - seasonal-adjustment
---

# Summary

This source note captures the direct BLS settlement mechanics for the market and the main methodological nuance that matters for a threshold contract: the market resolves to the BLS monthly **seasonally adjusted** CPI-U change for March 2026, published to one decimal place on the April 10, 2026 release.

## Key facts extracted

- The BLS CPI schedule page lists the **March 2026** CPI release for **April 10, 2026 at 8:30 AM ET**.
- The current CPI release page for February 2026 states directly that the **Consumer Price Index for March 2026 is scheduled to be released on Friday, April 10, 2026, at 8:30 a.m. ET**.
- The CPI release page explains that the monthly headline CPI-U figure is reported on a **seasonally adjusted basis** for the 1-month change.
- The same release page explicitly distinguishes seasonally adjusted monthly changes from unadjusted monthly changes.
- BLS says seasonally adjusted data are computed using **X-13ARIMA-SEATS** seasonal factors updated each February, revising the previous 5 years of seasonally adjusted data.
- BLS seasonal-adjustment FAQ says aggregate all-items seasonal factors are **dependently derived** and not knowable in advance because component weights and aggregation matter.
- The FAQ also notes the **2025 funding lapse** created atypical handling for missing October 2025 data in the seasonal-adjustment process, which is relevant as a data-quality/contextual caution rather than a direct settlement risk.

## Evidence directly stated by source

- February 2026 CPI-U increased **0.3% seasonally adjusted** and **0.5% before seasonal adjustment**. This directly confirms that adjusted and unadjusted monthly prints can differ materially.
- BLS states short-term trend analysis should usually rely on **seasonally adjusted** data.
- BLS is the governing publication surface for the contract’s source of truth.

## What is uncertain

- The exact March 2026 seasonal factor and resulting rounded 1-month CPI-U print are not knowable from these pages alone before release.
- The release page and FAQ do not provide a March forecast.
- Because the market threshold is **0.8% or more** at one-decimal precision, any raw or model estimate near the upper-0.7s would remain a rounding-sensitive edge case until the official release.

## Why this source may matter

This is the authoritative source-of-truth surface for settlement and the cleanest way to verify the case-specific requirements to check the BLS report and verify seasonal adjustment.

## Possible impact on the question

The main effect is on contract interpretation rather than directional forecasting. It reduces ambiguity about what counts and suggests that a variant bearish-on-YES view can be defended partly on mechanics: the bar is not merely a hot unadjusted month but a **BLS-published, seasonally adjusted, one-decimal monthly CPI-U print of at least 0.8%**.

## Reliability notes

- Primary source and direct settlement authority: high reliability.
- Independence is limited because all settlement mechanics trace back to BLS, but that is appropriate here because BLS is the contractual source of truth.
- The 2025 missing-data note is a useful contextual caution about process complexity, though it does not itself imply elevated risk for the March 2026 release.