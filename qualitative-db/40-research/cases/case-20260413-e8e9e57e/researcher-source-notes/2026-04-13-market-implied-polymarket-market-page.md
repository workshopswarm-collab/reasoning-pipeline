---
type: source_note
case_key: case-20260413-e8e9e57e
dispatch_id: dispatch-case-20260413-e8e9e57e-20260413T224434Z
analysis_date: 2026-04-13
persona: market-implied
domain: sports
subdomain: hockey
entity: connor-mcdavid
topic: market-implied probability and contract wording
question: Will Connor McDavid win the 2025–2026 NHL Art Ross Trophy?
date_created: 2026-04-13
source_name: Polymarket event page
source_type: market page / contract context
source_url: https://polymarket.com/event/nhl-2025-26-art-ross-trophy
source_date: 2026-04-13
credibility: medium
recency: high
stance: supports-yes
certainty: high
importance: high
novelty: low
agent: market-implied
related_entities: [connor-mcdavid]
related_drivers: []
upstream_inputs: []
downstream_uses: [market-implied.md, market-implied.sidecar.json, evidence/market-implied.md]
tags: [source-note, market-page, polymarket, art-ross]
---

# Summary

The Polymarket event page shows Connor McDavid priced around 96% to win the 2025-26 NHL Art Ross Trophy, with Nikita Kucherov and Nathan MacKinnon far behind. The assignment prompt also provides the governing contract wording: resolution is based on the player awarded the Art Ross Trophy, with official NHL information primary and consensus credible reporting as fallback.

## Key facts extracted

- Polymarket page text shows Connor McDavid around 96.1%.
- Other leading listed runners are much lower: Nikita Kucherov around 2.7%, Nathan MacKinnon around 1.4%.
- Event title is `NHL Art Ross Trophy Winner`.
- Assignment prompt states the market resolves according to the player awarded the 2025-26 Art Ross Trophy.
- Assignment prompt further states that if the listed player is not announced as a finalist, the market resolves `No`.
- Assignment prompt states official NHL information is the primary resolution source, with consensus credible reporting as fallback.

## Evidence directly stated by source

- The market is heavily concentrated on McDavid.
- The market is not pricing this as a close race.
- Resolution mechanics depend on official NHL attribution, not merely raw third-party statistics.

## What is uncertain

- The event page is not itself the source of truth for award determination.
- The page extraction does not show a dedicated rules pane beyond market display text.
- The unusual `finalist` wording in the contract could create small settlement ambiguity if the Art Ross is treated as a statistical title rather than finalist-announced award, though the primary intent still appears to be official NHL attribution.

## Why this source may matter

This source defines the market-implied baseline and clarifies that the case is not just about who led today but about how Polymarket expects official NHL determination to line up with the public leaderboard.

## Possible impact on the question

It anchors the comparison: any non-market view has to explain why a 96% price is too high despite McDavid’s apparent lead and the lack of a close alternative implied by current public information.

## Reliability notes

- High reliability for reading the market’s own current price.
- Only medium reliability for resolution truth because the primary source remains official NHL information, not the market page itself.
- Useful as the direct baseline for market-implied analysis.