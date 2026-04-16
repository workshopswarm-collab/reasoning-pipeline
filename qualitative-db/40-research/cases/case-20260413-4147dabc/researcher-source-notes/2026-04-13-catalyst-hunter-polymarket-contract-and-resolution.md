---
type: source_note
case_key: case-20260413-4147dabc
dispatch_id: dispatch-case-20260413-4147dabc-20260413T183547Z
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: animals-and-nature
subdomain: wildlife-cams-and-date-resolution
entity: polymarket
topic: first-eaglet-hatch-date-resolution
question: Will the first eaglet hatch on April 11, 2026?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket market context and resolution rules for Great Lakes Bald Eagle Cam hatch market
source_type: market-contract
source_url: https://polymarket.com/event/when-will-the-first-eaglet-hatch
source_date: 2026-04-13
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [polymarket]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [source-note, polymarket, resolution-rules, date-sensitive, wildlife-cam]
---

# Summary

This source note captures the contract mechanics for a date-specific wildlife-cam market. Its main value is not biological forecasting but resolution logic: the contract resolves to the ET calendar date of the first *fully emerged* eaglet visible on the named livestreams, with a special outage clause if both streams are unavailable.

## Key facts extracted

- The market resolves according to the **calendar date in ET** on which the first eaglet hatches.
- A qualifying **"hatch"** is the first moment an eaglet is **visibly fully emerged from its shell**.
- A **pip** or **partial emergence** does **not** qualify.
- If no eaglet hatches by **April 16, 2026, 11:59 PM ET**, the market resolves to **No Hatch before April 17**.
- The governing source of truth is the **Great Lakes Bald Eagle Cam livestreams** at the two named YouTube URLs.
- If **both** livestreams are unavailable and a hatch occurred while they were down, the market resolves to the ET calendar date on which a stream later returns and shows that the qualifying hatch occurred while the streams were unavailable.
- If both streams remain unavailable through April 16, 2026 11:59 PM ET, the market resolves to **No Hatch before April 17** regardless of what happened off-screen.

## Evidence directly stated by source

- The contract text explicitly names the two YouTube livestream URLs as the resolution source.
- The contract text explicitly defines the qualifying event as **full emergence**, excluding pip and partial emergence.
- The contract text explicitly makes **ET** the relevant date standard.
- The contract text explicitly includes a **dual-stream outage** contingency that can shift the recorded date away from the unseen biological hatch time and toward the stream-return date.

## What is uncertain

- The contract text does not provide nest-specific incubation dates or expected hatch timing.
- The extracted market page available here does not provide a full public audit trail for prior egg-lay dates.
- The outage language leaves some practical ambiguity about how clearly a later stream return must demonstrate that a qualifying hatch occurred during downtime.

## Why this source may matter

This is the governing contract and therefore the primary source for what conditions must hold for an April 11 resolution. In a narrow date market, contract mechanics can dominate biological intuition because a hatch that is biologically near April 11 can still miss contract qualification if it is only a pip, only partial emergence, or only inferred while both streams are unavailable.

## Possible impact on the question

The market can resolve to April 11 only if **all** of the following happen:
1. at least one egg reaches the point of **full visible emergence**,
2. that first qualifying full emergence occurs on **April 11 ET**, and
3. that timing is established under the livestream-based source-of-truth rules rather than invalidated or shifted by a dual-stream outage scenario.

## Reliability notes

- High relevance and high authority for resolution mechanics.
- Medium credibility only in the sense that it is a market host page rather than the livestream itself for the terminal fact; still primary for contract wording.
- Best used together with the actual named livestream sources and any independent nest-timing context.