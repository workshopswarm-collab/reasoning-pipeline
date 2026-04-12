---
type: source_note
case_key: case-20260409-a8d8231d
dispatch_id: dispatch-case-20260409-a8d8231d-20260409T183257Z
analysis_date: 2026-04-09
persona: variant-view
domain: climate
subdomain: global-temperature
entity: nasa
topic: march-2026-global-temperature-bracket
question: Will global temperature increase by between 1.25ºC and 1.29ºC in March 2026?
driver: operational-risk
date_created: 2026-04-09
source_name: NASA GISS GISTEMP v4 GLB.Ts+dSST monthly table
source_type: primary_dataset_table
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
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [climate, settlement-source, nasa, gistemp, primary-source]
---

# Summary

This is the governing primary source named directly in the contract. The 2026 row in the `GLOBAL Land-Ocean Temperature Index in 0.01 degrees Celsius` table shows `Mar = 128`, which converts to 1.28°C and falls inside the 1.25°C–1.29°C bracket.

## Key facts extracted

- The contract’s named primary resolution source is `GLB.Ts+dSST.txt` under the `Mar` column for row `2026`.
- The current table includes a `2026` row with `Jan 108`, `Feb 124`, `Mar 128`.
- NASA’s table states values are in `0.01 degrees Celsius`.
- Therefore `128` means `1.28°C`.
- `1.28°C` is inside the target bracket `[1.25, 1.29]`.

## Evidence directly stated by source

- Table heading: `GLOBAL Land-Ocean Temperature Index in 0.01 degrees Celsius`.
- 2026 row excerpt: `2026   108  124  128 **** ...`.
- Footer instruction: `Divide by 100 to get changes in degrees Celsius (deg-C).`

## What is uncertain

- The source note itself does not prove publication timestamp beyond current availability.
- The market text contains a fallback clause that appears to mention February 2026 rather than March 2026, which is likely a typo or template artifact; however it does not matter because March 2026 data is already present.
- The contract says later revisions do not matter once the data becomes available, so audit attention should focus on first posted March value, not subsequent updates.

## Why this source may matter

It is both the direct measurement source and the explicit governing source of truth for resolution.

## Possible impact on the question

If the market follows its stated rules, this source alone is sufficient to make the event resolve YES because the March 2026 anomaly is listed as 1.28°C.

## Reliability notes

- Highest relevance because the contract names this exact NASA table.
- Reliability for settlement is high even if broader climate-analysis disputes existed, because contract wording privileges this source over alternative datasets.
- Operational risk is low but not zero: website availability or parsing errors could create temporary settlement friction, though not a real evidentiary conflict once the row is visible.
