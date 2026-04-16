---
type: source_note
case_key: case-20260414-4ed80a0a
dispatch_id: dispatch-case-20260414-4ed80a0a-20260414T174040Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: protocols
entity: ethereum
topic: eth-price-threshold
question: Will Ethereum reach $2,400 April 13-19?
date_created: 2026-04-14
source_name: Binance ETHUSDT 24hr ticker API
source_type: exchange market data
source_url: https://api.binance.com/api/v3/ticker/24hr?symbol=ETHUSDT
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [ethereum]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/personas/base-rate.md]
tags: [binance, market-data, verification, threshold]
---

# Summary

A direct Binance public ticker endpoint showed ETHUSDT highPrice of 2415.50 over the preceding 24 hours at fetch time, comfortably above the $2,400 threshold used by the contract.

## Key facts extracted

- Symbol: ETHUSDT
- lastPrice: 2331.08
- openPrice: 2235.60
- highPrice: 2415.50
- lowPrice: 2218.53
- closeTime/openTime indicate the 24-hour window covered the period around the Apr 14 verification check.

## Evidence directly stated by source

- Binance directly reported a 24-hour session high of 2415.50 for ETHUSDT.
- That high exceeds the contract threshold by 15.50.

## What is uncertain

- This endpoint is not the exact 1-minute candle table specified by the contract, so it is confirmatory rather than textually identical to the settlement source.
- The 24-hour rolling window does not by itself identify the exact qualifying minute within the Apr 13-19 ET contract window, though given the fetch timing it is highly consistent with the market having already resolved Yes.

## Why this source may matter

It is an independent direct exchange data check from the same exchange named in the rules. That makes it a strong extra-verification source for an extreme-probability market.

## Possible impact on the question

This materially supports a Yes view and strongly supports the market having correctly moved to ~100% / resolved Yes, because a reported Binance high above $2,400 is exactly the kind of evidence the contract requires.

## Reliability notes

High reliability as direct exchange data from the named resolution venue. Slightly lower than the exact specified 1-minute High source only because this is a summary ticker endpoint rather than the literal chart surface referenced by the rules.