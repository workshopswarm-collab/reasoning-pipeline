---
type: source_note
case_key: case-20260414-669935fa
dispatch_id: dispatch-case-20260414-669935fa-20260414T172940Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: will-bitcoin-reach-76000-april-13-19
question: Will Bitcoin reach $76,000 April 13-19?
date_created: 2026-04-14
source_name: Polymarket market page
source_type: market primary surface
source_url: https://polymarket.com/event/what-price-will-bitcoin-hit-april-13-19
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-669935fa/researcher-analyses/2026-04-14/dispatch-case-20260414-669935fa-20260414T172940Z/personas/base-rate.md]
tags: [polymarket, market-surface, resolution-surface]
---

# Summary

This source establishes the live market framing, current market-implied probability from the assigned price, and the governing settlement surface to consult for rules.

## Key facts extracted

- Assignment context gives current_price = 0.9995 for the relevant outcome, implying roughly 99.95% probability.
- The Polymarket event page is the primary market surface for the April 13-19 Bitcoin hit question.
- The fetched page text explicitly says traders should review the page Rules section for the resolution criteria and official data sources used to determine the result.

## Evidence directly stated by source

- The event page describes this as a prediction market on what price Bitcoin will hit during April 13-19.
- The page text states that the resolution rules define exactly what needs to happen and which official data sources govern settlement.

## What is uncertain

- The lightweight fetch did not expose the full rule text, only the existence of the Rules section.
- The fetched FAQ-like text appears generated/summary style rather than a clean export of the canonical rule body, so it should not be treated as a perfect transcript of the contract language.

## Why this source may matter

- It is the primary market source for the current market-implied view.
- It points to the governing source-of-truth surface for settlement mechanics, which matters because this is a date-bounded hit market.

## Possible impact on the question

- High implied probability means the market believes the threshold is effectively already reached or extremely likely to be reached during the stated window.
- Because the market is at an extreme, the assignment requires an extra verification pass against independent price data rather than trusting the market surface alone.

## Reliability notes

- Useful as the primary market/contract surface.
- Reliable for market price and existence of a Rules section.
- Less reliable for exact rule wording through this fetch path because the full text was not exposed cleanly.