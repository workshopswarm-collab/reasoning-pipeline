---
type: source_note
case_key: case-20260409-92464f9a
dispatch_id: dispatch-case-20260409-92464f9a-20260409T201552Z
analysis_date: 2026-04-09
persona: market-implied
domain: climate
subdomain: global-temperature-indices
entity: nasa
topic: march-2026-global-temperature-resolution-source
question: Will global temperature increase by more than 1.29ºC in March 2026?
driver: reliability
date_created: 2026-04-09
source_name: Polymarket contract description and linked NASA resolution source
source_type: market-contract-and-primary-source-pointer
source_url: https://polymarket.com/event/march-2026-temperature-increase-c
source_date: 2026-04-09
credibility: medium
recency: current
stance: neutral
certainty: medium
importance: high
novelty: low
agent: market-implied
related_entities: [nasa]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [source-note, polymarket, nasa, gistemp, resolution-source]
---

# Summary

The market contract description is valuable mainly because it states the exact resolution mechanics and points to the governing NASA source-of-truth table. It says the market resolves according to the value reported by NASA’s Global Land-Ocean Temperature Index for March 2026, specifically the table `GLB.Ts+dSST.txt`, row `2026`, column `Mar`.

## Key facts extracted

- The market asks whether March 2026 global temperature increase is **more than 1.29ºC**.
- The primary resolution source is the NASA GISTEMP table `GLOBAL Land-Ocean Temperature Index in 0.01 degrees Celsius` at `https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.txt`.
- The relevant cell is the row `2026`, column `Mar`.
- Once the March 2026 figure is available, that bracket is sufficient for resolution even if later revised.
- If NASA’s main temperature index page is permanently unavailable, other NASA information may be used.
- If no information for the target month is provided by the stated fallback deadline, the market resolves to the lowest bracket.

## Evidence directly stated by source

- NASA is the governing source of truth.
- The contract is about one specific monthly anomaly value, not a broader climate narrative.
- Revisions after first publication do not matter for settlement.

## What is uncertain

- The fetched market page did not itself expose the actual March 2026 NASA value.
- The market page does not independently verify what the NASA table currently says; it only points to the governing source.
- The fallback clause appears internally inconsistent in one place because it references February 2026 in the copied description even though the market is about March 2026; this increases the need to privilege the main source-of-truth clause over copy noise.

## Why this source may matter

This source defines what counts and what does not count. For a rule-sensitive official-stat market, the contract text matters because it narrows the relevant evidence to the exact NASA table entry rather than any other climate dataset or later revision.

## Possible impact on the question

If the NASA March 2026 anomaly cell exists and is above 1.29ºC, the market should resolve Yes regardless of wider debate. If it is 1.29ºC or below, or absent past fallback conditions, the market should resolve No / lowest bracket depending on the exact market structure.

## Reliability notes

- Reliable for contract mechanics, not for the underlying data value itself.
- Should be paired with the actual NASA source or strong contextual secondary climate sources.
- The apparent month-reference inconsistency in the fallback clause is a reminder to treat the primary NASA table reference as controlling.