---
type: source_note
case_key: case-20260407-b34d8893
dispatch_id: dispatch-case-20260407-b34d8893-20260407T004114Z
analysis_date: 2026-04-07
persona: variant-view
domain: crypto
subdomain: institutions
entity: strategy
topic: case-20260407-b34d8893 | variant-view
question: Will Microstrategy announce a Bitcoin purchase March 31-April 6?
date_created: 2026-04-07
source_name: Strategy official website surfaces (press archive and purchases page)
source_type: official company website
source_url: https://www.strategy.com/press
source_date: 2026-04-07
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: variant-view
related_entities: [strategy, bitcoin]
related_drivers: []
upstream_inputs: []
downstream_uses: [variant-view finding]
tags: [official-source, company-website, resolution-source, direct-verification]
---

# Summary

I checked Strategy's official press archive and the company-maintained purchases page as the primary direct verification surfaces for whether an in-window BTC purchase announcement was posted.

## Key facts extracted

- Strategy's official press archive page was accessible and returned a list of recent press items.
- In the visible recent archive entries returned on 2026-04-07 UTC / 2026-04-06 ET, there was no listed BTC purchase announcement dated March 31, April 1, April 2, April 3, April 4, April 5, or April 6, 2026.
- The visible archive included older BTC-purchase-style announcements, which supports that this archive is a plausible place where such announcements appear when made.
- The `https://www.strategy.com/purchases` page was accessible but the fetch extractor returned only footer text, so it confirmed the surface existed but did not yield machine-readable holdings detail in this pass.

## Evidence directly stated by source

- The press archive directly displayed recent official company press items and their dates.
- The purchases page directly exists as an official company reference surface for BTC purchase tracking.

## What is uncertain

- The purchases page content was not fully readable through the fetch extractor, so this pass cannot independently confirm whether holdings changed during the title window from that page alone.
- This note does not verify Michael Saylor's personal account/posts; it only verifies the official company website surfaces.

## Why this source may matter

The market explicitly resolves from official information from MicroStrategy/Strategy or Michael Saylor. The official company website is therefore a governing direct source, not just contextual evidence.

## Possible impact on the question

Absence of an in-window BTC purchase announcement on the official company press archive strongly supports No, especially because this is a low-difficulty official-announcement market and the archive visibly carries company announcements including BTC-related ones.

## Reliability notes

- Credibility is high because this is the company-owned website and named resolution source family.
- Independence is low because both checked pages are same-entity surfaces.
- The press archive produced materially useful direct evidence; the purchases page provided partial verification only due to extraction limitations.