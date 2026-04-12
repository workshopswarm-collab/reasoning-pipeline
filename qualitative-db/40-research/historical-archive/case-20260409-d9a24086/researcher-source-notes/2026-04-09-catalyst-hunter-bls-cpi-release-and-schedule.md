---
type: source_note
case_key: case-20260409-d9a24086
dispatch_id: dispatch-case-20260409-d9a24086-20260409T165631Z
analysis_date: 2026-04-09
persona: catalyst-hunter
domain: economics
subdomain: macro-data-and-indicators
entity: bureau-of-labor-statistics
topic: march-2026-cpi-release-schedule-and-resolution-source
question: Will monthly inflation increase by 0.8% or more in March?
driver: reliability
date_created: 2026-04-09
source_name: BLS CPI February 2026 release plus BLS CPI release schedule and seasonal-adjustment methodology page
source_type: official government release and official methodology pages
source_url: https://www.bls.gov/news.release/cpi.nr0.htm
source_date: 2026-03-11
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
upstream_inputs: []
downstream_uses: []
tags:
  - source-note
  - bls
  - cpi
  - seasonal-adjustment
---

# Summary

BLS is the governing source of truth for this market, and its own release schedule confirms the March 2026 CPI-U release is due April 10, 2026 at 8:30 AM ET. The current BLS CPI release page also confirms the market resolves on the seasonally adjusted CPI-U monthly change reported to one decimal place, while the BLS seasonal-adjustment page confirms seasonal factors were updated on February 13, 2026 and that seasonally adjusted CPI data are generated via X-13ARIMA-SEATS with annual revisions to the prior five years.

## Key facts extracted

- BLS February 2026 CPI release says CPI-U increased 0.3% seasonally adjusted in February and explicitly states: "The Consumer Price Index for March 2026 is scheduled to be released on Friday, April 10, 2026, at 8:30 a.m. (ET)."
- BLS CPI schedule page lists reference month March 2026 with release date Apr. 10, 2026 at 08:30 AM.
- BLS archived/current CPI release structure shows the official CPI-U all-items monthly change is reported on a seasonally adjusted basis to one decimal place in Table A.
- BLS seasonal-adjustment page says seasonal factors were updated February 13, 2026 and prior five years of seasonally adjusted indexes were revised then.
- BLS seasonal-adjustment page says CPI seasonally adjusted data are computed using X-13ARIMA-SEATS.

## Evidence directly stated by source

- The relevant release date/time is April 10, 2026 at 8:30 AM ET.
- The governing series for this market is CPI-U all items, seasonally adjusted, monthly change.
- The official BLS output reports monthly CPI-U changes to one decimal place.
- Seasonal adjustment is a live methodological layer and was recalculated recently for 2021-2025 with updated factors introduced February 13, 2026.

## What is uncertain

- These BLS pages do not provide the March 2026 result in advance.
- The pages do not themselves imply whether March will print 0.8% or higher; they mainly settle timing, methodology, and source-of-truth mechanics.
- The seasonal-adjustment page confirms methodology and recent factor revisions, but not whether March 2026 seasonal factors will amplify or damp the final one-month all-items print enough to cross 0.8%.

## Why this source may matter

This source is decisive for contract interpretation and timing. It anchors the key catalyst calendar: there is one dominant repricing event, the April 10 BLS release. It also reduces resolution ambiguity by confirming that seasonally adjusted CPI-U, not an unadjusted series or core CPI, governs the answer.

## Possible impact on the question

Because the market closes before the release and then resolves on the official BLS publication, repricing should be driven mainly by any late nowcast/preview information before April 10 and then by the single official BLS release itself. The methodology note matters because a very high threshold like 0.8% depends on the exact seasonally adjusted all-items print, not broader inflation narrative.

## Reliability notes

Source quality is high: these are official BLS pages, including the direct settlement surface and official schedule/methodology pages. Independence is low because all pages are the same institution, but for a directly settled official-stat market that is acceptable and expected.