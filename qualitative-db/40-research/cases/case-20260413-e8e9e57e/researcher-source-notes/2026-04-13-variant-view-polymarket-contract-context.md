---
type: source_note
case_key: case-20260413-e8e9e57e
dispatch_id: dispatch-case-20260413-e8e9e57e-20260413T224434Z
analysis_date: 2026-04-13
persona: variant-view
domain: sports
subdomain: hockey
entity: connor-mcdavid
topic: Polymarket contract framing / Art Ross market state
question: Will Connor McDavid win the 2025–2026 NHL Art Ross Trophy?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket event page
source_type: market_context
source_url: https://polymarket.com/event/nhl-2025-26-art-ross-trophy
source_date: 2026-04-13
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: variant-view
related_entities: [connor-mcdavid]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-e8e9e57e/researcher-analyses/2026-04-13/dispatch-case-20260413-e8e9e57e-20260413T224434Z/personas/variant-view.md]
tags: [source-note, polymarket, contract-context]
---

# Summary

The Polymarket event page shows the market pricing McDavid in the mid-90s to roughly 96% range and lists other contenders far behind, confirming that the consensus market already treats this as close to resolved.

## Key facts extracted

- The event page title is NHL Art Ross Trophy Winner.
- The extracted page shows Connor McDavid around 96.1% on the leaderboard and an active Yes price around 96.3 cents.
- It shows Nikita Kucherov around 2.7% and Nathan MacKinnon around 1.4%.
- Volume is substantial enough that the market is not purely illiquid noise.

## Evidence directly stated by source

The market itself is implying that McDavid is the overwhelming favorite / near-certain winner.

## What is uncertain

- Web extraction captured the rendered market surface, not the full formal rules text.
- Market prices can move intraday and the assignment's canonical current_price is 0.9475, which is slightly below the rendered page snapshot.
- This source is not authoritative for actual NHL settlement; it is only authoritative for current market consensus.

## Why this source may matter

The variant-view role needs to explain whether the market's confidence is justified or fragile. This source establishes the crowd's baseline and shows how little room is currently reserved for upset or resolution noise.

## Possible impact on the question

Because the market is already pricing McDavid above 94%, any variant case must show why that confidence may still be a little too high even if the overall direction remains Yes.

## Reliability notes

Useful for consensus pricing, not for source-of-truth settlement. Independence from NHL data is medium because it reflects trader synthesis rather than official stats, but it may still be copying the same official leaderboard narrative.