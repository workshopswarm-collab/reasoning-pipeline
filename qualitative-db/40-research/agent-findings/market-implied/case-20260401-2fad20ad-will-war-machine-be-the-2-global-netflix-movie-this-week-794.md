---
type: agent_finding
domain: culture
subdomain: film
entity: War Machine
topic: case-20260401-2fad20ad | market-implied
question: Will "War Machine" be the #2 global Netflix movie this week?
driver: media-narratives
date_created: 2026-04-01
agent: market-implied
stance: disagree
certainty: high
importance: high
novelty: medium
time_horizon: immediate / already-at-resolution-surface
related_entities: [War Machine, Netflix]
related_drivers: [media-narratives, seasonality]
upstream_inputs:
  - qualitative-db/40-research/source-notes/by-market/case-20260401-2fad20ad-market-implied-netflix-top10-context.md
downstream_uses: []
tags: [domain/culture, subdomain/film, netflix, top10, war-machine, market-implied, disagree]
---

# Claim
I disagree strongly with the market price. The market-implied probability is 95.85%, but the official Netflix Top 10 surface indicates War Machine was already #1 on the relevant Global Movies (English) chart for 3/23/26-3/29/26, which makes a YES position on "War Machine will be #2" look badly inconsistent with public resolution evidence.

## Implication for the question
At 0.9585, the market is effectively assuming either that War Machine occupies the #2 slot with near-certainty or that the market mechanics somehow justify treating it as such. The strongest market-respecting case would be that traders were using a stale or misread prior from pre-update speculation, or that the market remained open despite the official Netflix update already making the answer mostly knowable. But once the official chart is consulted, the price does not look efficient; it looks stale or misaligned with the actual resolution surface.

My own estimate for YES is about 3%.

Reasoning:
- Netflix's official Tudum Top 10 page is the resolution source class named in the market description.
- That page shows the weekly chart for 3/23/26-3/29/26.
- The chart distribution is #1 19.4M, #2 10.3M, #3 7.9M, etc.
- Raw page inspection ties `war-machine` to a `#1 in Movies` badge on that chart.
- If that mapping is correct, then War Machine is not #2 and YES should be near zero.
- I leave a small residual probability only for extraction/mapping error or unusual market-resolution mismatch, not for substantive competition uncertainty.

## Supporting evidence
- Official Netflix Tudum Top 10 Movies page for Global Movies (English) showed the relevant weekly update and its view counts.
- The page linked War Machine directly as one of the current charted titles.
- Raw page inspection associated War Machine with `#1 in Movies`, KPop Demon Hunters with `#3 in Movies`, and Louis Theroux: Inside the Manosphere with `#9 in Movies`.
- This means the decisive public evidence is not a subtle competitive read between neighboring titles; it is that War Machine appears to sit above the target rank.

## Counterpoints
- The readability/plain-text extraction did not provide a perfectly clean title-to-rank table for every title.
- I did not recover a secondary official export that names the #2 title explicitly in a cleaner format.
- If the chart page's dynamic markup were misread, the confidence should come down.
- If the market remained open after the official update, price could reflect operational lag rather than genuine belief.

## Key assumptions
- The official Tudum Top 10 page for Global Movies (English) is the controlling resolution surface, consistent with the market description.
- The raw HTML mapping from `war-machine` to `#1 in Movies` is accurate.
- No later corrective Netflix update superseded the visible weekly chart before resolution.

## Why this is decision-relevant
This is exactly the kind of case where a market-implied researcher should try hard to respect price first. A 95.85% price would usually deserve deference. But after checking the official source, the more plausible story is not that the market knows something hidden; it is that the market price failed to update to already-public resolution evidence. So the market appears stale rather than insightful here.

## What would falsify this interpretation
- A cleaner official Netflix table or API output showing War Machine was actually #2, not #1.
- Evidence that the visible chart segment I inspected was for a different category or date than the market resolves on.
- A market rule nuance showing the market should ignore the already-visible official update.

## Recommended follow-up
- Before trade or synthesis, verify once with a cleaner official extraction or screenshot of the named title at #1/#2 on the Netflix chart.
- Treat the current market price as likely stale/misaligned unless that verification fails.
- Do not spend more research budget on broad competitor hunting; the key mechanism is official-source inconsistency, which is already material and decisive.