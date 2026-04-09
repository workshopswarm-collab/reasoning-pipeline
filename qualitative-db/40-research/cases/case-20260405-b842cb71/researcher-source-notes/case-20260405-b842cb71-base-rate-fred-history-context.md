---
type: source_note
domain: energy
subdomain: gasoline_prices
entity: FRED / EIA gasoline retail series
topic: historical base rates and contextual near-threshold check
question: How rare is a U.S. regular gasoline move to $4+, and what does the contextual weekly series imply near March 31, 2026?
driver: gasoline_price_history
date_created: 2026-04-05
source_name: FRED series GASREGW (US Regular All Formulations Gas Price)
source_type: secondary/contextual data aggregator sourced from EIA
source_url: https://fred.stlouisfed.org/graph/fredgraph.csv?id=GASREGW
source_date: 1990-08-20 to 2026-03-30
credibility: high
recency: high
stance: neutral
certainty: high
importance: medium
novelty: medium
agent: base-rate
related_entities: [EIA, FRED]
related_drivers: [gasoline_price_history]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260405-b842cb71/researcher-analyses/2026-04-05/dispatch-case-20260405-b842cb71-20260405T074926Z/personas/base-rate.md]
tags: [fred, eia, gasoline, history, base-rate, threshold]
legacy_imported: true
legacy_original_path: qualitative-db/40-research/researcher-source-notes/by-market/case-20260405-b842cb71-base-rate-fred-history-context.md
legacy_original_note_kind: source
imported_by: legacy_40_research_backfill
import_batch: 20260405T225345Z
case_key: case-20260405-b842cb71
---

# Summary
The long-run outside view says national U.S. regular gasoline prices above $4 are uncommon. In the weekly FRED/EIA series since 1990, only 2008 and 2022 ever printed at or above $4, and only 2022 was already above $4 by March 31. The same weekly series shows 2026-03-30 at $3.990, which is extremely close to the threshold but still below it and therefore serves as the strongest contextual disconfirmation for a Yes call.

## Key facts extracted
- Series used: FRED GASREGW, "US Regular All Formulations Gas Price."
- Last observation in fetched CSV: 2026-03-30 = 3.990.
- Years with any weekly reading >= $4 since 1990: 2008 and 2022.
- Years with a weekly reading >= $4 on or before March 31: only 2022.
- Recent pre-April maxima from the fetched series:
  - 2023: 3.489
  - 2024: 3.523
  - 2025: 3.162
  - 2026: 3.990

## Evidence directly stated by source
- The CSV directly reports weekly retail gasoline values by observation date.
- The 2026-03-30 observation is directly reported as 3.990.

## What is uncertain
- This is not the settlement source; the contract resolves on AAA daily national average, not this weekly EIA/FRED series.
- Methodology and timing differ from AAA enough that 3.990 here does not rule out AAA having crossed $4 on an individual day before the deadline.

## Why this source may matter
This is the best compact outside-view and cross-check source I found. It shows both how unusual $4 national gasoline is and why the timing window near March 31 is genuinely close rather than trivial.

## Possible impact on the question
The historical rarity keeps the base-rate researcher from treating a $4 breach as automatic. The 2026-03-30 weekly value of 3.990 is the main reason not to assign a near-certain Yes probability even after seeing the AAA March 26 and April 2 bracket.

## Reliability notes
- High-quality contextual source with long history and clean machine-readable values.
- Not independent of EIA sourcing and not authoritative for settlement, so it should be treated as contextual/disconfirming rather than decisive.
