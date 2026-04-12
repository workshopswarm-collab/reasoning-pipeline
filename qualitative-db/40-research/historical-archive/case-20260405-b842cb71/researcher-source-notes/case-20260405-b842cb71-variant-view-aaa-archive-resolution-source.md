---
type: source_note
domain: energy
subdomain: gasoline-prices
entity: aaa
topic: AAA national regular gasoline average around March 31, 2026
question: Will gas hit (High) $4.00 by March 31?
driver: late-march national gasoline price spike
date_created: 2026-04-05
source_name: AAA Fuel Prices page via Internet Archive snapshots
source_type: archived primary source / resolution source
source_url: https://web.archive.org/web/20260331111835/https://gasprices.aaa.com/
source_date: 2026-03-31
credibility: high
recency: high for the contract window
stance: neutral
certainty: high
importance: high
novelty: high
agent: variant-view
related_entities: [AAA, U.S. regular gasoline]
related_drivers: [spring gasoline seasonality, refinery transition to summer blend]
upstream_inputs: []
downstream_uses: [case-20260405-b842cb71 main finding]
tags: [aaa, resolution-source, internet-archive, gasoline, march-2026]
legacy_imported: true
legacy_original_path: qualitative-db/40-research/researcher-source-notes/by-market/case-20260405-b842cb71-variant-view-aaa-archive-resolution-source.md
legacy_original_note_kind: source
imported_by: legacy_40_research_backfill
import_batch: 20260405T225345Z
case_key: case-20260405-b842cb71
---

# Summary
Archived AAA Fuel Prices snapshots directly show the national regular gasoline "Current Avg." moved from $3.990 on March 30, 2026 to $4.018 on March 31, 2026. Because the contract explicitly resolves from the AAA site’s "Regular" / "Current Avg." cell, this is the central direct evidence.

## Key facts extracted
- Wayback snapshot `20260330211217` of `https://gasprices.aaa.com/` shows:
  - Today’s AAA National Average: $3.990
  - Regular / Current Avg.: $3.990
  - Yesterday Avg.: $3.980
  - Week Ago Avg.: $3.956
- Wayback snapshot `20260331111835` of the same page shows:
  - Today’s AAA National Average: $4.018
  - Regular / Current Avg.: $4.018
  - Yesterday Avg.: $3.990
  - Week Ago Avg.: $3.977
- Additional March 31 snapshots (`20260331150739`, `20260331162243`) also show $4.018 for Regular / Current Avg.
- The live AAA page on 2026-04-05 shows Current Avg. $4.110 and Yesterday Avg. $4.104, confirming continued movement above $4.00 after the cutoff, though the archived March 31 snapshots are the relevant evidence for this contract.

## Evidence directly stated by source
- AAA’s own page labels the governing cell as "Regular" and row "Current Avg."
- The March 31 archived page displays `$4.018` in that cell.

## What is uncertain
- Internet Archive is a preservation layer, not the named source itself, so there is a small residual implementation risk if Polymarket required an internal AAA record inaccessible to the public page archive.
- The contract text’s "first two digits" example is imprecise language for truncation to the cent-level bracket, but $4.018 still clears the $4.00 threshold even under truncation.

## Why this source may matter
This is the explicit source-of-truth surface named in the market rules. If trustworthy, it mostly settles the market.

## Possible impact on the question
Very strong support for Yes. The direct source indicates the threshold was crossed on March 31 itself.

## Reliability notes
- Primary source quality: high, because the contract names AAA’s page and exact table cell.
- Archive-wrapper risk: low but nonzero; mitigated by multiple March 31 captures showing the same value and the adjacent March 30 snapshot showing the pre-crossing value at $3.990.