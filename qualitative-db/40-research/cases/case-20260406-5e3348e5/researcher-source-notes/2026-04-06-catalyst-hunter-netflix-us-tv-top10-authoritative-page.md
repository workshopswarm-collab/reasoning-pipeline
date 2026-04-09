---
type: source_note
case_key: case-20260406-5e3348e5
dispatch_id: dispatch-case-20260406-5e3348e5-20260406T175635Z
analysis_date: 2026-04-06
persona: catalyst-hunter
domain: entertainment
subdomain: streaming-rankings
entity:
topic: netflix-us-tv-top10-authoritative-page-and-timing-check
question: Will "XO, Kitty Season 3" be the top US Netflix show this week?
driver:
date_created: 2026-04-06
source_name: Netflix Tudum Top 10 - United States TV
source_type: authoritative platform ranking / source-of-truth surface
source_url: https://www.netflix.com/tudum/top10/united-states/tv
source_date: 2026-04-06
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260406-5e3348e5/researcher-analyses/2026-04-06/dispatch-case-20260406-5e3348e5-20260406T175635Z/personas/catalyst-hunter.md
tags: [netflix-top10, authoritative-source, timing-check, resolution]
---

# Summary

Netflix’s own United States TV Top 10 page is the governing source-of-truth surface for this market. On 2026-04-06, the live page still showed the last completed published week as **3/23/26 - 3/29/26**, meaning the decisive **3/30/26 - 4/5/26** update had not yet posted. A direct HTML inspection of the live page confirms the currently published top 10 for the older week and cleanly identifies **Beauty in Black: Season 2** as the current #1 card.

## Key facts extracted

- Governing page: `https://www.netflix.com/tudum/top10/united-states/tv`
- Region/category: United States / TV (Shows)
- Current visible completed reporting window on 2026-04-06: **3/23/26 - 3/29/26**
- Direct HTML card extraction for that week shows:
  - #1 `Beauty in Black: Season 2`
  - #2 `Homicide: New York: Season 2`
  - #3 `Raw: 2026 - March 23, 2026`
  - #4 `Virgin River: Season 7`
  - #5 `Something Very Bad Is Going to Happen: Season 1`
  - #6 `Age of Attraction: Season 1`
  - #7 `The Predator of Seville: Limited Series`
  - #8 `Ms. Rachel: Season 1`
  - #9 `ONE PIECE: Season 2`
  - #10 `Ms. Rachel: Season 2`
- No `XO, Kitty` entry appeared in the currently posted week’s top 10.
- The market description says resolution should use Netflix’s update expected on **Tuesday, April 7, 2026, 3:00 PM ET**, reflecting the prior Monday-Sunday week, i.e. **3/30/26 - 4/5/26**.

## Evidence directly stated by source

- The page explicitly displays the weekly selector including **3/23/26 - 3/29/26**.
- The page is the Netflix-controlled Top 10 surface referenced by the contract.
- Direct page HTML for the top-10 cards contains rank-number anchors and card alt text that identify titles for the currently published week.

## What is uncertain

- This source does **not** yet reveal the outcome for the target week **3/30/26 - 4/5/26**.
- The market title refers to `XO, Kitty Season 3`; that may be a market-label issue versus Netflix’s own title formatting, but the governing ranking surface is still the deciding reference.

## Why this source may matter

This source governs settlement mechanics and timing. For this case, the most important catalyst is simply the scheduled publication of the next weekly Netflix US TV chart.

## Possible impact on the question

High. The market cannot be settled from narrative chatter or current-week speculation alone; the real trigger is the Netflix-authored chart update expected on April 7. This makes the key catalyst a publication-time event rather than an ongoing flow of ambiguous popularity signals.

## Reliability notes

- Highest reliability for settlement because it is the named source-of-truth surface.
- Extra verification was performed via direct HTML card inspection, which materially improved title-to-rank confidence versus lossy readability extraction.
- Independence is low in the strict sense because this is a single-source settlement surface, but that is acceptable here because the source itself is authoritative.
