---
type: source_note
case_key: case-20260409-a8d8231d
dispatch_id: dispatch-case-20260409-a8d8231d-20260409T183257Z
analysis_date: 2026-04-09
persona: risk-manager
domain: climate
subdomain: global-temperature
entity: nasa
topic: march-2026-global-temperature-index
question: Will global temperature increase by between 1.25ºC and 1.29ºC in March 2026?
driver: reliability
date_created: 2026-04-09
source_name: NASA GISS Global Land-Ocean Temperature Index table
source_type: primary_dataset
source_url: https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.txt
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: high
agent: orchestrator
related_entities: [nasa]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [source-note, nasa, gistemp, settlement-source, market-resolution]
---

# Summary

This is the governing source of truth named directly in the contract. The operative check is the value in the table titled "GLOBAL Land-Ocean Temperature Index in 0.01 degrees Celsius" under column `Mar` and row `2026`.

## Key facts extracted

- The contract explicitly names this NASA GISS text table as the primary resolution source.
- The fetched table currently contains a `2026` row, meaning NASA has already published March 2026 data.
- The March 2026 value in the relevant row/column is `130`, which corresponds to **1.30°C** in the table's 0.01°C units.
- Because the target bracket is **between 1.25°C and 1.29°C**, a reading of 1.30°C is outside the bracket and implies `No` under the literal contract wording.
- The contract also states that once data becomes available, later revisions do not matter.

## Evidence directly stated by source

- The source is the NASA GISS monthly global land-ocean index table.
- Units are 0.01 degrees Celsius relative to the 1951-1980 base period.
- The specific settlement location is row `2026`, column `Mar`.

## What is uncertain

- This note depends on correct extraction of the `2026` / `Mar` cell from the live table.
- The table itself is authoritative for settlement, but the market text includes a likely typo in the fallback clause referring to February 2026 rather than March 2026.
- If the live table were altered or temporarily malformed after publication, fallback NASA sources might become relevant, but the contract strongly prefers this exact table.

## Why this source may matter

This source is not just evidence about the climate outcome; it is the literal settlement mechanism for the market.

## Possible impact on the question

If the March 2026 NASA GISS value is 130 (1.30°C), the market should resolve `No` for the 1.25°C to 1.29°C bracket, regardless of secondary analyses or later revisions.

## Reliability notes

High reliability for settlement because the contract explicitly names this table. Residual risk is operational rather than scientific: correct row/column extraction, potential website availability issues, and any dispute arising from the contract's typo in the fallback clause.