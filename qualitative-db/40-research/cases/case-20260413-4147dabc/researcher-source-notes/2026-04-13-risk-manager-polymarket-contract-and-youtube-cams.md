---
type: source_note
case_key: case-20260413-4147dabc
dispatch_id: dispatch-case-20260413-4147dabc-20260413T183547Z
analysis_date: 2026-04-13
persona: risk-manager
domain: wildlife
subdomain: bald-eagle-hatch-market
entity: polymarket
topic: case-20260413-4147dabc | risk-manager
question: Will the first eaglet hatch on April 11, 2026?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket market page plus linked YouTube livestream metadata
source_type: primary-market-rule-and-resolution-source
source_url: https://polymarket.com/event/when-will-the-first-eaglet-hatch
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [polymarket]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [risk-manager-finding, risk-manager-evidence-map, risk-manager-assumption-note]
tags: [primary-source, resolution-rules, youtube-livestream, outage-risk]
---

# Summary

The Polymarket market description provides the governing contract mechanics: resolution is based solely on the two Great Lakes Bald Eagle Cam livestreams; a qualifying hatch is only when an eaglet is visibly fully emerged from its shell; timing is based on live timestamps in ET; and if both livestreams are down during the actual hatch and later return, the market resolves to the ET calendar date when the stream returns, not necessarily when the hatch physically occurred. Separate extraction from the linked YouTube pages confirms both linked feeds are active live streams operated by the Great Lakes Bald Eagle Cam channel.

## Key facts extracted

- Governing source of truth is the Great Lakes Bald Eagle Cam livestreams linked in the contract.
- Resolution date is the ET calendar date of the first qualifying hatch.
- "Hatch" excludes a pip or partial emergence and requires visible full emergence from shell.
- If both streams are unavailable during the event and later return showing a hatch occurred while down, the market resolves to the ET date of return.
- If both remain unavailable through April 16 11:59 PM ET, market resolves to "No Hatch before April 17" regardless of biological reality.
- YouTube extraction confirms both linked pages are live streams from the Great Lakes Bald Eagle Cam channel, supporting that these are the intended resolution feeds.

## Evidence directly stated by source

- The market page explicitly states the full-emergence standard.
- The market page explicitly states the ET date logic.
- The market page explicitly states the outage fallback, which can detach resolution date from actual hatch date.
- The YouTube metadata directly states both pages are live content under the Great Lakes Bald Eagle Cam channel.

## What is uncertain

- The market page excerpt available through direct fetch does not itself show expected hatch timing or exact egg-laying chronology.
- No direct extraction here establishes whether April 11 is the modal biological hatch date versus April 10 or April 12.
- The livestream timestamp implementation and any delay/latency are not independently audited here.

## Why this source may matter

This is the highest-priority source because it governs what counts. For a date-specific market with a high implied probability, the biggest risk may come from contract mechanics rather than biology: full emergence versus pip, ET cutoffs, timestamp conventions, and outage fallback rules.

## Possible impact on the question

This source reduces confidence in any extreme probability on a single date unless there is unusually strong evidence about exact timing. Even if a hatch is biologically likely near April 11, the contract can still resolve differently because of partial-emergence timing or a dual-stream outage scenario.

## Reliability notes

High reliability on the rule text because it is the governing market source. Medium reliability on inferred operational implications because stream delay, timestamp behavior, and practical monitoring conditions are not independently audited in this note.