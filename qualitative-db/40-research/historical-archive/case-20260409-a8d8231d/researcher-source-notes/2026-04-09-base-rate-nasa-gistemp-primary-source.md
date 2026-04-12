---
type: source_note
case_key: case-20260409-a8d8231d
dispatch_id: dispatch-case-20260409-a8d8231d-20260409T183257Z
analysis_date: 2026-04-09
persona: base-rate
domain: climate
subdomain: global-temperature
entity: nasa
topic: march-2026-global-temperature-index
question: Will global temperature increase by between 1.25ºC and 1.29ºC in March 2026?
driver: reliability
date_created: 2026-04-09
source_name: NASA GISS Global Land-Ocean Temperature Index table
source_type: primary_data_table
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
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-a8d8231d/researcher-analyses/2026-04-09/dispatch-case-20260409-a8d8231d-20260409T183257Z/personas/base-rate.md]
tags: [source-note, nasa, gistemp, settlement-source, primary-source]
---

# Summary

This is the governing source-of-truth surface named directly in the market rules. It contains the row for 2026 and a populated `Mar` column.

## Key facts extracted

- The market rules specify this exact NASA GISS table as the primary resolution source.
- The table header is `GLOBAL Land-Ocean Temperature Index in 0.01 degrees Celsius` with monthly columns including `Mar`.
- The 2026 row is present and the `Mar` value is populated at **134**, i.e. **1.34°C** relative to the 1951-1980 base period.
- A March 2026 anomaly of 1.34°C is above the target bracket of 1.25°C to 1.29°C inclusive.

## Evidence directly stated by source

- The table explicitly reports monthly anomaly values in hundredths of a degree Celsius.
- The row `2026` and column `Mar` provide the direct value used for settlement under the contract.

## What is uncertain

- The source note does not by itself prove whether the value was first posted before market close, though the runtime fetch on 2026-04-09 shows it available during analysis.
- NASA data can later be revised, but the contract states the market resolves immediately based on the first available March 2026 figure regardless of later revision.

## Why this source may matter

This source is dispositive for settlement unless NASA permanently removes the index and fallback NASA information must be used.

## Possible impact on the question

If the `2026 / Mar` cell remains 134 at settlement, the market should resolve **No** because 1.34°C is outside the 1.25–1.29°C bracket.

## Reliability notes

High reliability for this contract because it is the explicitly named primary resolution source. The main residual risk is not measurement credibility but contract-mechanics ambiguity or any operational issue with availability/timing.