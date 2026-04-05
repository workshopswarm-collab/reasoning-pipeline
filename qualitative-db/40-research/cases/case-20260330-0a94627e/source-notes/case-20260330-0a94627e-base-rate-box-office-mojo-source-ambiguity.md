---
type: source_note
domain: culture
subdomain: film
entity: Project Hail Mary
topic: Box Office Mojo source path and title-page ambiguity
question: Will "Project Hail Mary" 2nd weekend box office be greater than $54M?
driver: product-launches
date_created: 2026-03-30
source_name: Box Office Mojo
source_type: primary box office data source
source_url: https://www.boxofficemojo.com/title/tt12042730/
source_date: 2026-03-30
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: base-rate
related_entities: [Project Hail Mary]
related_drivers: [product-launches]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260330-0a94627e/analyses/2026-03-30/dispatch-case-20260330-0a94627e-20260330T142051Z/evidence/base-rate.md
  - qualitative-db/40-research/cases/case-20260330-0a94627e/analyses/2026-03-30/dispatch-case-20260330-0a94627e-20260330T142051Z/personas/base-rate.md
tags: [domain/culture, subdomain/film, source/box-office-mojo, market/case-20260330-0a94627e]
legacy_imported: true
legacy_original_path: qualitative-db/40-research/source-notes/by-market/case-20260330-0a94627e-base-rate-box-office-mojo-source-ambiguity.md
legacy_original_note_kind: source
imported_by: legacy_40_research_backfill
import_batch: 20260405T225345Z
case_key: case-20260330-0a94627e
---

# Summary

Box Office Mojo appears to have the actual `Project Hail Mary` page at **`/title/tt12042730/`**, while the market description links **`/title/tt28650488/`**, which did not resolve to the film when checked. The actual Mojo page shows domestic gross and opening data consistent with other reporting, but the market text’s URL appears mismatched.

## Key facts extracted

- Fetching `https://www.boxofficemojo.com/title/tt12042730/` returned a page titled **"Project Hail Mary - Box Office Mojo"**.
- That Mojo page showed:
  - Domestic gross: **$164,302,240**
  - Worldwide gross: **$300,802,240**
  - Domestic opening: **$80,506,007**
  - Domestic week-1 gross: **$109,764,644**
- Fetching the URL embedded in the market description (`tt28650488`) did **not** return the `Project Hail Mary` page in the extractor output.

## Evidence directly stated by source

- Box Office Mojo has a live page for `Project Hail Mary` matching the movie title and broad commercial totals reported elsewhere.
- The opening number on the actual Mojo page matches The Numbers and trade coverage, which increases confidence that the correct movie page is `tt12042730`.

## What is uncertain

- The Mojo fetch extractor did not expose the "Domestic Daily" table directly, so I could not verify the exact final 3-day second-weekend figure from Mojo through this tool alone.
- Because the market description includes a likely wrong Mojo URL, there is some small resolution-process ambiguity even though the intended movie is obvious from the market title.
- It remains possible that Monday finalization changes the exact Mojo weekend figure slightly.

## Why this source may matter

This is the contractual source family named in the market description. Even though the extractor was limited, it matters for identifying the likely correct page and for flagging that the market text’s embedded URL seems inconsistent with the actual film page.

## Possible impact on the question

The mismatch does **not** materially weaken the commercial case for a YES outcome, but it does introduce a small operational/resolution risk: a reviewer should verify that the market resolves against the correct `Project Hail Mary` Mojo page and its Domestic Daily tab.

## Reliability notes

- Box Office Mojo is the primary resolution source named by the market.
- Tool extraction was incomplete for daily-table detail, so this note is strongest on page identity and summary numbers, weaker on the exact final weekend figure.