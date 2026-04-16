---
type: source_note
case_key: case-20260415-3d3080df
dispatch_id: dispatch-case-20260415-3d3080df-20260415T002239Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-3d3080df | market-implied
question: Will the Binance BTC/USDT 12:00 ET 1m candle close be above 70000 on April 20, 2026?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket event page and rules
source_type: market page / resolution rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: market-implied
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-3d3080df/researcher-analyses/2026-04-15/dispatch-case-20260415-3d3080df-20260415T002239Z/personas/market-implied.md]
tags: [polymarket, rules, resolution, binance, btc]
---

# Summary

The Polymarket event page provides both the live market ladder and the governing contract language. For the 70,000 strike on April 20, the displayed market price is about 85% to 86% Yes, implying the market sees BTC/USDT staying above 70,000 at the specified Binance 1-minute close. The rules are materially important because this is not a generic spot-price question; it resolves off the Binance BTC/USDT 12:00 ET one-minute candle close.

## Key facts extracted

- The specific contract resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 20, 2026 has a final close price higher than 70,000.
- Otherwise it resolves No.
- The page emphasizes Binance BTC/USDT only, not other exchanges or pairs.
- Price precision is determined by the number of decimals shown by the source.
- The event ladder shows the 70,000 line trading around 85% to 86% Yes at time of review.
- Nearby strikes imply a smooth-ish distribution: 68k ~94%, 72k ~73%, 74k ~54%, 76k ~32%.

## Evidence directly stated by source

- The source of truth is Binance, specifically the BTC/USDT close prices with 1m candles selected.
- The relevant timestamp is 12:00 in ET timezone on the specified date.
- The market is pricing a high probability that the close exceeds 70,000.

## What is uncertain

- The web fetch reflects the page content but is not itself the direct exchange source for the future resolving candle.
- The displayed odds can move quickly.
- The page does not itself prove Binance operational continuity at resolution time; it only defines the intended source.

## Why this source may matter

This is the governing market/rules source. It defines the exact settlement mechanics and also reveals the market-implied probability that the persona is meant to interrogate.

## Possible impact on the question

This source establishes the baseline: any contrarian view has to overcome a market-implied probability in the mid-80s, plus the probability ladder suggests the market currently centers BTC somewhere in the low-to-mid 70ks for the target time window.

## Reliability notes

Reliable for contract wording and the current market price snapshot, but not sufficient alone for the underlying BTC outlook. Needs independent price/context verification and an explicit timing check because the contract is narrow and date-sensitive.