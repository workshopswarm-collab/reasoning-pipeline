---
type: source_note
case_key: case-20260413-4147dabc
dispatch_id: dispatch-case-20260413-4147dabc-20260413T183547Z
analysis_date: 2026-04-13
persona: variant-view
domain: wildlife
subdomain: bald-eagle-cam-market
entity: polymarket
topic: first-eaglet-hatch-date-resolution
question: Will the first eaglet hatch on April 11, 2026?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket market context and resolution text
source_type: market rule / resolution source description
source_url: https://polymarket.com/event/when-will-the-first-eaglet-hatch
source_date: 2026-04-13
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [polymarket]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-4147dabc/researcher-analyses/2026-04-13/dispatch-case-20260413-4147dabc-20260413T183547Z/personas/variant-view.md]
tags: [source-note, polymarket, resolution, source-of-truth, timing]
---

# Summary

This source note captures the market's governing contract language and the explicit source-of-truth hierarchy for resolving the first-hatch date.

## Key facts extracted

- The market resolves to the calendar date in ET on which the first eaglet is visibly fully emerged from its shell.
- A pip or partial emergence does not qualify.
- The timing is determined from the live timestamps available on the Great Lakes Bald Eagle Cam livestreams.
- The stated resolution sources are the two YouTube livestreams for the Great Lakes Bald Eagle Cam in Traverse City, Michigan.
- If both livestreams are unavailable and later return showing that a qualifying hatch occurred while they were down, the market resolves to the ET calendar date on which the livestream returns, not necessarily the biological hatch date.
- If both streams remain unavailable through April 16, 2026 11:59 PM ET, the market resolves to "No Hatch before April 17," even if a hatch actually happened during the outage.

## Evidence directly stated by source

The market text directly defines the qualifying hatch event, timezone basis, and outage-resolution edge case.

## What is uncertain

- The market page itself does not provide the actual egg-laying dates.
- The market page does not resolve how likely April 11 is biologically; it only defines what counts and what source governs.

## Why this source may matter

This is the primary governing source for resolution mechanics. For a date-specific wildlife-cam market, contract wording and outage handling matter because timing precision and source-availability can determine the final answer.

## Possible impact on the question

This source increases confidence about what must happen for an April 11 resolution, but it also highlights a small operational-risk tail: the market can resolve based on stream return timing if both streams are down during the true hatch.

## Reliability notes

High reliability for resolution mechanics because this is the market's own governing text. Low informational value on the underlying biological timing beyond defining what counts.