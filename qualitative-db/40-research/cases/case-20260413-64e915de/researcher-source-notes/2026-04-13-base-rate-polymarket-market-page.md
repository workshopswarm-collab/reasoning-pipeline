---
type: source_note
case_key: case-20260413-64e915de
dispatch_id: dispatch-case-20260413-64e915de-20260413T234340Z
analysis_date: 2026-04-13
persona: base-rate
domain: crypto
subdomain: protocols
entity: ethereum
topic: will-ethereum-reach-2400-april-13-19
question: Will Ethereum reach $2,400 April 13-19?
date_created: 2026-04-13
source_name: Polymarket market page
source_type: market page / primary contract surface
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
downstream_uses: []
tags: [polymarket, market-structure, source-note]
---

# Summary

The Polymarket event page is the primary source for the live market-implied probability on the "$2,400" bucket and for identifying the governing contract surface. It showed the "↑ 2,400" outcome trading around 92% at fetch time, with the page framing outcomes as discrete buckets for the week of April 13-19.

## Key facts extracted

- The market title is "What price will Ethereum hit April 13-19?"
- The page displayed "↑ 2,400" around 92% at fetch time.
- The page also displayed "↑ 2,300" as the leading outcome at 100%, which is directionally consistent with ETH already having exceeded $2,300.
- The page states that resolution rules and official data sources are specified in the Rules section on the page, making that contract surface the governing source of truth even though the fetch extract did not cleanly expose the full rules text.

## Evidence directly stated by source

- Crowd-implied probabilities for each outcome update in real time.
- The correct outcome is determined under the market's resolution rules and official data source specified on the page.

## What is uncertain

- The readability extract did not fully expose the detailed rules text or the exact official reference exchange/index used for settlement.
- The page text is a rendered market interface, not an independent price record.

## Why this source may matter

It is the primary source for the market-implied baseline and for identifying the authoritative contract surface that governs settlement.

## Possible impact on the question

A 92% price on the "$2,400" bucket implies the market viewed touching or exceeding $2,400 during the April 13-19 window as highly likely. That sets a high bar for disagreeing with the market unless outside verification suggests the touch had not occurred or the contract wording materially differs from the obvious interpretation.

## Reliability notes

Useful and necessary as the contract/market surface, but not sufficient alone for the truth of whether ETH actually traded to $2,400. It should be paired with an independent external price source.