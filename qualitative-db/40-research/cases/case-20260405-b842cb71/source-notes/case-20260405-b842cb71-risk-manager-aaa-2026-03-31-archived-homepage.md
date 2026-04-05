---
type: source_note
domain: energy
subdomain: retail-gasoline
entity: aaa-fuel-prices
topic: case-20260405-b842cb71 | risk-manager
question: Will gas hit (High) $4.00 by March 31?
driver: resolution-source-verification
date_created: 2026-04-05
source_name: AAA Fuel Prices homepage archived by Internet Archive on 2026-03-31
source_type: archived authoritative source-of-truth surface
source_url: https://web.archive.org/web/20260331150739/https://gasprices.aaa.com/
source_date: 2026-03-31
credibility: high
recency: high for the case window
stance: supports_yes
certainty: high
importance: high
novelty: medium
agent: risk-manager
related_entities: [aaa-fuel-prices, internet-archive, polymarket]
related_drivers: [resolution-source-verification, contract-mechanics]
upstream_inputs: []
downstream_uses: [case-20260405-b842cb71-finding, case-20260405-b842cb71-evidence-map]
tags: [aaa, gas-prices, authoritative-source, archived-page, march-31, resolution]
legacy_imported: true
legacy_original_path: qualitative-db/40-research/source-notes/by-market/case-20260405-b842cb71-risk-manager-aaa-2026-03-31-archived-homepage.md
legacy_original_note_kind: source
imported_by: legacy_40_research_backfill
import_batch: 20260405T225345Z
case_key: case-20260405-b842cb71
---

# Summary
AAA’s own homepage, captured by the Internet Archive on 2026-03-31, shows the national “Regular” price in the “Current Avg.” row at **$4.018**.

## Key facts extracted
- Archived AAA homepage timestamp used: `20260331150739`.
- Relevant table row: `Current Avg.` under `Regular`.
- Reported value in the archived page: **$4.018**.
- Under the contract’s stated truncation mechanic (“first two digits,” example `3.157 -> 3.15`), `$4.018` maps to the **$4.01 bracket**, which is **at or above $4.00**.

## Evidence directly stated by source
- AAA page displays the national average gas prices table.
- In the row `Current Avg.` and column `Regular`, the archived page shows `$4.018`.

## What is uncertain
- The Internet Archive is an archival wrapper around AAA’s page, so the preservation layer is independent but the underlying content is still AAA-origin data.
- The market metadata supplied to this run lists `closes_at` as 2026-03-30 20:00 ET, which is slightly awkward against the plain-language rule “by March 31.” The contract text itself still points to March 31 and to AAA’s `Current Avg.` cell.

## Why this source may matter
This is the closest thing to a direct settlement check available after the fact: it preserves the exact AAA source surface named in the contract on the key date.

## Possible impact on the question
This source strongly supports **Yes**. If accepted as the governing AAA surface for March 31, the market should resolve Yes because $4.018 clears the $4.00 threshold even under truncation.

## Reliability notes
- AAA is the named resolution source, so the underlying source authority is high.
- Internet Archive adds a preservation layer rather than a new analytical interpretation.
- Best use: direct resolution/source-of-truth verification, not broader causal context.