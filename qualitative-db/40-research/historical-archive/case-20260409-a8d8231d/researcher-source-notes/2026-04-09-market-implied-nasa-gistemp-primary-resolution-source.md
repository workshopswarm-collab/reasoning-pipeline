---
type: source_note
case_key: case-20260409-a8d8231d
dispatch_id: dispatch-case-20260409-a8d8231d-20260409T183257Z
analysis_date: 2026-04-09
persona: market-implied
domain: climate
subdomain: global-temperature
entity: nasa
topic: case-20260409-a8d8231d | market-implied
question: Will global temperature increase by between 1.25ºC and 1.29ºC in March 2026?
driver: reliability
date_created: 2026-04-09
source_name: NASA GISTEMP v4 GLB.Ts+dSST table
source_type: primary_dataset
source_url: https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.txt
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: high
agent: market-implied
related_entities: [nasa]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-a8d8231d/researcher-analyses/2026-04-09/dispatch-case-20260409-a8d8231d-20260409T183257Z/personas/market-implied.md]
tags: [source-note, primary-source, resolution-source, gistemp]
---

# Summary

This is the governing primary source for settlement under the contract. The live table currently shows the March 2026 value in the row `2026` and column `Mar` as `128`, which corresponds to a 1.28ºC anomaly relative to the 1951-1980 base period.

## Key facts extracted

- The table title is `GLOBAL Land-Ocean Temperature Index in 0.01 degrees Celsius`.
- The row for `2026` currently reads: `2026   108  124  128 **** ...`.
- Therefore the March 2026 value is `128` hundredths of a degree Celsius, i.e. `1.28ºC`.
- `1.28ºC` falls inside the contract bracket `1.25ºC to 1.29ºC`.
- The table also states the base period is `1951-1980`, matching the contract’s referenced NASA surface.
- The source list on the table identifies the inputs as `GHCN-v4` and `ERSST v5` through `2026`.

## Evidence directly stated by source

- The March 2026 numerical anomaly is displayed directly in the exact table surface named by the contract.
- The source is a NASA GISS-maintained plain-text table, not a third-party summary.

## What is uncertain

- The contract says the market resolves immediately once the data becomes available and ignores later revisions, but a reviewer still needs to confirm Polymarket has recognized the release if timing becomes disputed.
- If NASA later reformats the page, the contract’s fallback clause could matter, but that does not appear necessary right now because the primary source is available.

## Why this source may matter

It is the explicit source of truth named in the contract, so it can by itself settle the numeric bracket question if the March 2026 value is visible and unambiguous.

## Possible impact on the question

This source alone strongly supports a YES interpretation for the 1.25ºC-1.29ºC bracket because the contract points to the exact row/column cell and that cell currently reads `128`.

## Reliability notes

High reliability for settlement because it is the exact NASA surface named by the contract. Residual risk is mostly operational/timing-related rather than interpretive.