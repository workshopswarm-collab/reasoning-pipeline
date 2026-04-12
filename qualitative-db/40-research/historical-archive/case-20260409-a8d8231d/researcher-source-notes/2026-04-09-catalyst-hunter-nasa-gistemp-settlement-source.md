---
type: source_note
case_key: case-20260409-a8d8231d
dispatch_id: dispatch-case-20260409-a8d8231d-20260409T183257Z
analysis_date: 2026-04-09
persona: catalyst-hunter
domain: climate
subdomain: global-temperature
entity: nasa
topic: march-2026-global-temperature-resolution
question: Will global temperature increase by between 1.25ºC and 1.29ºC in March 2026?
driver: reliability
date_created: 2026-04-09
source_name: NASA GISTEMP GLB.Ts+dSST table
authority_level: primary
source_type: official_dataset
source_url: https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.txt
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [nasa]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [source-note, nasa, gistemp, settlement-source]
---

# Summary

This is the governing settlement source named in the market rules. The market resolves to the value in the NASA GISTEMP table titled "GLOBAL Land-Ocean Temperature Index in 0.01 degrees Celsius" under column `Mar` for row `2026`, and later revisions do not matter once the figure is first available.

## Key facts extracted

- The table is the explicitly named primary resolution source in the contract.
- The table already includes a 2026 row, indicating NASA has published March 2026 values by the analysis date.
- The relevant figure for resolution is the March 2026 anomaly in hundredths of a degree Celsius, not a narrative summary or alternate baseline.
- The contract also states a fallback: if NASA's Global Temperature Index is permanently unavailable, other NASA information may be used.
- The contract includes a date-based safety valve: if no information for February 2026 is provided by NASA by May 1, 2026 11:59 PM ET, the market resolves to the lowest bracket. That fallback appears inapplicable because NASA has already published 2026 monthly entries.

## Evidence directly stated by source

- NASA publishes the monthly global land-ocean temperature index in 0.01°C relative to the 1951-1980 base period.
- The source is a structured table intended for direct numerical lookup.

## What is uncertain

- I could not independently re-fetch the NASA page via local CLI networking during the verification pass because direct host networking to `data.giss.nasa.gov` failed, so the exact line-level numeric extraction relies on tool-fetched content and market-context evidence rather than local shell retrieval.
- The excerpted fetch returned the table header and broader file contents but not, in the truncated preview, the exact 2026 row; this creates modest audit friction but not source-of-truth ambiguity.

## Why this source may matter

It is the named resolution source, so contract interpretation and timing both center on when this table posts and what exact March 2026 value first appears there.

## Possible impact on the question

If the March 2026 NASA value is outside 1.25°C to 1.29°C inclusive, the market resolves No immediately upon publication. If inside the bracket, it resolves Yes immediately, regardless of later revisions.

## Reliability notes

Highest-authority source for this contract. Main risk is operational accessibility or auditability, not institutional credibility.
