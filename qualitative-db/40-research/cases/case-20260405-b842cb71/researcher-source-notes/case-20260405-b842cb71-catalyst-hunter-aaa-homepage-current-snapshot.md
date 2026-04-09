---
type: source_note
domain: energy
subdomain: retail-gasoline
entity: aaa-fuel-prices
topic: AAA national regular gasoline average and contract source-of-truth
question: Did AAA's national regular gasoline average reach at least $4.00 by March 31, 2026?
driver: retail fuel price spike
date_created: 2026-04-05
source_name: AAA Fuel Prices homepage
source_type: authoritative settlement source
source_url: https://gasprices.aaa.com/
source_date: 2026-04-05
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [aaa, us-regular-gasoline]
related_drivers: [oil-supply-shock, seasonal-gasoline-demand]
upstream_inputs: []
downstream_uses: [case-20260405-b842cb71]
tags: [aaa, source-of-truth, gas-prices, settlement]
legacy_imported: true
legacy_original_path: qualitative-db/40-research/researcher-source-notes/by-market/case-20260405-b842cb71-catalyst-hunter-aaa-homepage-current-snapshot.md
legacy_original_note_kind: source
imported_by: legacy_40_research_backfill
import_batch: 20260405T225345Z
case_key: case-20260405-b842cb71
---

# Summary
AAA's fuel-prices homepage is the contract's explicit source of truth. On 2026-04-05 it showed national regular gasoline at $4.110, with yesterday at $4.104 and week-ago at $3.980.

## Key facts extracted
- The market description explicitly says settlement uses AAA, specifically the cell under "Regular" and row "Current Avg."
- AAA homepage on 2026-04-05 displayed:
  - Current Avg. regular: $4.110
  - Yesterday Avg. regular: $4.104
  - Week Ago Avg. regular: $3.980
  - Month Ago Avg. regular: $3.251
- AAA also lists the current page date as 4/5/26.

## Evidence directly stated by source
- "Today’s AAA National Average $4.110"
- "Price as of 4/5/26"
- Under National average gas prices / Regular:
  - Current Avg. $4.110
  - Yesterday Avg. $4.104
  - Week Ago Avg. $3.980

## What is uncertain
- This snapshot is after the contract cutoff, so by itself it does not prove whether the threshold was first crossed on March 30, March 31, or after March 31.
- The homepage does not expose a full daily archive in the fetched text.

## Why this source may matter
It is the governing resolution surface named by the contract, so any interpretation should anchor to AAA rather than EIA or other retail-gas trackers.

## Possible impact on the question
This confirms both the governing source and that prices were extremely close to the threshold one week before 2026-04-05, making a late-March/early-April breach highly plausible and worth checking with a contemporaneous March 31 report.

## Reliability notes
High reliability for settlement mechanics and current values because AAA is named explicitly in the market rules. Lower usefulness for the exact March 31 outcome unless paired with a contemporaneous report or archive.