---
type: source_note
case_key: case-20260414-3d24d01f
dispatch_id: dispatch-case-20260414-3d24d01f-20260414T184328Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-19
question: Will the Binance BTC/USDT 1-minute candle closing at 12:00 PM America/New_York on 2026-04-19 close above 70000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules
source_type: market page / resolution rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-19
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-3d24d01f/researcher-analyses/2026-04-14/dispatch-case-20260414-3d24d01f-20260414T184328Z/personas/market-implied.md]
tags: [polymarket, resolution-rules, market-pricing]
---

# Summary

This source provides the current market-implied baseline and the governing resolution mechanics for the contract.

## Key facts extracted

- The 70,000 line was trading around 89% on the fetched page, with buy-yes shown at 90¢ and buy-no at 12¢.
- The market resolves from the Binance BTC/USDT 1-minute candle for 12:00 in ET timezone on April 19, 2026.
- The contract resolves on the candle's final **Close** price, not intraminute high/low and not another venue.
- Price precision is determined by the Binance source.

## Evidence directly stated by source

- The rules explicitly name Binance BTC/USDT as the resolution source.
- The rules explicitly specify the 1-minute candle at 12:00 PM ET.
- The page shows the current crowd-implied pricing across multiple thresholds, with 70,000 at roughly 89%.

## What is uncertain

- The page is a market interface, not the underlying Binance data feed itself.
- The fetched webpage view may lag live trading by a small amount.
- The rules do not by themselves tell us whether Binance's public UI candle boundaries are ET-labeled or just translated from UTC; this needed separate verification.

## Why this source may matter

It is the contract-defining source for what counts, and it also gives the market's own implied probability baseline that this persona is meant to decode.

## Possible impact on the question

This source sets a high bar for contrarianism: any disagreement must overcome both the crowd's ~89% prior and the exact contract wording, especially the venue-specific and time-specific conditions.

## Reliability notes

Useful and necessary for market framing and rule interpretation, but not sufficient alone for a price forecast because it is neither the final resolution print nor an independent market-context source.