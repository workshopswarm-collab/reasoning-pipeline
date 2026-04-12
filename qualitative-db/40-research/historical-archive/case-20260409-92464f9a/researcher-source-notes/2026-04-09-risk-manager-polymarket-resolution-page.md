---
type: source_note
case_key: case-20260409-92464f9a
dispatch_id: dispatch-case-20260409-92464f9a-20260409T201552Z
analysis_date: 2026-04-09
persona: risk-manager
domain: climate
subdomain: global-temperature
entity: nasa
topic: case-20260409-92464f9a | risk-manager
question: Will global temperature increase by more than 1.29ºC in March 2026?
driver: operational-risk
date_created: 2026-04-09
source_name: Polymarket market resolution page
source_type: market-resolution-page
source_url: https://polymarket.com/event/march-2026-temperature-increase-c
source_date: 2026-04-09
credibility: medium
recency: current
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: risk-manager
related_entities: [nasa]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, resolution, market-rules, climate]
---

# Summary

The Polymarket event page states the contract wording, names NASA GISTEMP `GLB.Ts+dSST.txt` as the primary resolution source, and currently shows `Outcome proposed: No` and `Final outcome: No` with `No dispute`.

## Key facts extracted

- Market resolves to the March 2026 value reported by NASA GISTEMP in `GLOBAL Land-Ocean Temperature Index in 0.01 degrees Celsius`.
- The operative cell is the `Mar` column in row `2026` of `GLB.Ts+dSST.txt`.
- The page says the named bracket is necessary and sufficient once data becomes available, regardless of later revisions.
- Fallback: if NASA’s Global Temperature Index is permanently unavailable, other NASA information may be used.
- Additional fallback: if no information for February 2026 is provided by NASA by May 1, 2026 11:59 PM ET, the market resolves to the lowest range bracket.
- Page currently displays `Outcome proposed: No`, `No dispute`, and `Final outcome: No`.

## Evidence directly stated by source

Directly stated on page: contract wording, primary source-of-truth path, fallback logic, and displayed resolution state.

## What is uncertain

- The readable fetch did not expose the exact bracket menu text on the event page, so this note does not independently restate every bracket.
- This page is strong evidence of actual market settlement state, but the underlying quantitative March 2026 NASA table value was not independently retrieved in this run because direct fetch to NASA host failed from the runtime environment.

## Why this source may matter

It is the closest available source to actual settlement mechanics and current settled status. For a risk-manager lens, it sharply lowers residual uncertainty because the market itself is already showing a finalized `No` outcome with no dispute.

## Possible impact on the question

This source strongly supports a `No` conclusion, but residual process risk remains if the displayed final state somehow diverged from the underlying NASA source or if the page were stale. That is why independent contextual verification still matters.

## Reliability notes

High relevance for settlement mechanics; medium credibility as an independently auditable scientific source because it is the market page rather than the NASA table itself. Best used together with independent contextual confirmation that NASA/peer climate reporting for the relevant release window exists.