---
type: source_note
case_key: case-20260413-64e915de
dispatch_id: dispatch-case-20260413-64e915de-20260413T234340Z
analysis_date: 2026-04-13
persona: market-implied
domain: crypto
subdomain: protocols
entity: ethereum
topic: case-20260413-64e915de | market-implied
question: Will Ethereum reach $2,400 April 13-19?
driver:
date_created: 2026-04-13
source_name: Polymarket event page
source_type: market page / contract surface
source_url: https://polymarket.com/event/what-price-will-ethereum-hit-april-13-19
source_date: 2026-04-13
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [ethereum]
related_drivers: []
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260413-64e915de/researcher-analyses/2026-04-13/dispatch-case-20260413-64e915de-20260413T234340Z/personas/market-implied.md
tags: [polymarket, market-odds, contract-surface]
---

# Summary

The Polymarket event page is the governing market surface for current implied odds and the first place to inspect resolution framing for the weekly Ethereum price-band question.

## Key facts extracted

- The assigned current price for the ↑ 2,400 outcome is 0.905, implying about 90.5%.
- The event page fetched during this run also described ↑ 2,400 as the second-leading outcome at roughly 92%, with ↑ 2,300 as effectively certain on the public page snapshot.
- The page states that complete resolution criteria live in the Rules section on the page, even though the readability fetch did not cleanly expose the detailed rules text.

## Evidence directly stated by source

- Polymarket represents the crowd-implied probability for this exact contract.
- The page confirms this is a multi-outcome weekly Ethereum price-hit market covering April 13-19.

## What is uncertain

- The simplified fetch did not expose the full rules text, so exact source-of-truth mechanics for the weekly high need to be inferred from standard Polymarket market structure unless separately verified.
- The page copy appears partially promotional / FAQ-style rather than a full raw rules export.

## Why this source may matter

This is the primary source for the market-implied baseline. For a market-implied persona, the key question is whether public evidence supports a probability near 90%+ for ETH touching $2,400 during the week.

## Possible impact on the question

A 90%+ implied probability means the market is effectively saying that a $2,400 touch is expected, not merely possible. Any non-market view has to explain why live spot and expected weekly range do not support that level of confidence.

## Reliability notes

Useful and necessary for price/implied probability, but not fully sufficient alone for final interpretation because the rules text was not fully extracted in the fetch. Reliability for current price is high enough; reliability for full resolution mechanics from the extracted text is only medium.