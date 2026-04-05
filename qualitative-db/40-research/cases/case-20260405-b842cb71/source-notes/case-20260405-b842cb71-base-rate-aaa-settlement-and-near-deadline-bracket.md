---
type: source_note
domain: energy
subdomain: gasoline_prices
entity: AAA Fuel Prices
topic: AAA settlement source and near-deadline national average path
question: Will AAA Current Avg. Regular reach at least $4.000 by March 31, 2026 under the market's first-two-digits rule?
driver: pump_price_spike
date_created: 2026-04-05
source_name: AAA Fuel Prices homepage and AAA March 26 / April 2 news posts
source_type: primary + authoritative settlement source
source_url: https://gasprices.aaa.com/
source_date: 2026-03-26 to 2026-04-05
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: base-rate
related_entities: [AAA Fuel Prices]
related_drivers: [pump_price_spike]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260405-b842cb71/analyses/2026-04-05/dispatch-case-20260405-b842cb71-20260405T074926Z/personas/base-rate.md]
tags: [aaa, settlement-source, gasoline, march-2026, threshold]
legacy_imported: true
legacy_original_path: qualitative-db/40-research/source-notes/by-market/case-20260405-b842cb71-base-rate-aaa-settlement-and-near-deadline-bracket.md
legacy_original_note_kind: source
imported_by: legacy_40_research_backfill
import_batch: 20260405T225345Z
case_key: case-20260405-b842cb71
---

# Summary
AAA is the governing resolution source. The contract settles off the AAA homepage cell under "Regular" and row "Current Avg." with a truncation-style first-two-digits rule. AAA's own March 26, 2026 post said the national average was $3.981 and "could reach $4/gallon in the coming days." AAA's April 2, 2026 post said the national average had exceeded $4/gallon "this week" and listed today's average as $4.081. The homepage fetched on April 5, 2026 showed Current Avg. Regular at $4.110.

## Key facts extracted
- Market description names AAA as the resolution source, specifically the homepage "Current Avg." / "Regular" cell.
- Market description says: "This market will resolve based on the first two digits of the reported price (e.g., if the price is reported as $3.157, this market will resolve to the '$3.15' bracket)."
- AAA homepage fetch on 2026-04-05 showed:
  - Current Avg. Regular: $4.110
  - Yesterday Avg.: $4.104
  - Week Ago Avg.: $3.980
  - Month Ago Avg.: $3.251
  - Year Ago Avg.: $3.262
- AAA news post dated 2026-03-26 stated:
  - Today's National Average: $3.981
  - "The national average could reach $4/gallon in the coming days for the first time since August 2022."
- AAA news post dated 2026-04-02 stated:
  - Today's National Average: $4.081
  - "The national average for a gallon of regular exceeded $4/gallon this week for the first time since August 2022."
  - One Week Ago: $3.981

## Evidence directly stated by source
- AAA directly states both the governing source-of-truth surface and the relevant near-deadline values.
- AAA directly states the price was $3.981 on March 26 and $4.081 on April 2.
- AAA directly states the >$4 crossing occurred "this week" by April 2.

## What is uncertain
- I did not find a directly archived AAA homepage snapshot for March 31 itself.
- "This week" on the April 2 AAA post brackets the crossing to roughly March 27-April 2, but does not explicitly say whether the threshold was first crossed before or after March 31.
- Because the rule uses truncation rather than rounding, a value like $3.999 would still resolve No; the exact daily AAA value on March 31 therefore matters.

## Why this source may matter
This is the settlement source, so it dominates every contextual source. The March 26 and April 2 AAA posts are the strongest direct evidence for timing around the threshold.

## Possible impact on the question
The direct AAA bracket strongly suggests the contract was very close by late March and likely crossed around the deadline window. The lack of a March 31 archived AAA value prevents full certainty, but this source alone makes Yes materially more plausible than a generic base rate would.

## Reliability notes
- AAA is authoritative for settlement because the contract names it explicitly.
- The homepage and AAA's own posts are first-party sources, but the near-deadline inference still depends on interpolation because I did not recover the exact March 31 homepage value.
