---
type: source_note
case_key: case-20260414-082b1b3f
dispatch_id: dispatch-case-20260414-082b1b3f-20260414T171716Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: spot-market
entity: sol
topic: case-20260414-082b1b3f | market-implied
question: Will the Binance SOL/USDT 1-minute candle at 12:00 PM ET on 2026-04-17 close above 80?
driver: reliability
date_created: 2026-04-14
source_name: Binance API + Binance market page / Polymarket rules
source_type: exchange primary data + market rules
source_url: https://api.binance.com/api/v3/klines?symbol=SOLUSDT&interval=1m&limit=5
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [sol, solana]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, polymarket, source-of-truth, contract-check]
---

# Summary

This source note captures the governing resolution mechanics and the live Binance spot data that the market is implicitly pricing.

## Key facts extracted

- Polymarket rules say the market resolves from the Binance SOL/USDT **1-minute candle labeled 12:00 in ET timezone (noon)** on 2026-04-17.
- Resolution condition is strict: the final Binance candle **Close** must be **higher than 80**; equality or any close below 80 resolves No.
- Binance API spot checks on 2026-04-14 showed SOL/USDT trading around **85.25**.
- Recent 1-minute Binance closes sampled via API were **85.27, 85.32, 85.23, 85.23, 85.25**.
- Binance 5-minute average endpoint returned **85.27249116**, consistent with the minute-level sample.

## Evidence directly stated by source

- Direct contract wording from Polymarket: source of truth is Binance SOL/USDT with 1m candles; relevant field is the final close of the 12:00 ET candle on the specified date.
- Direct market data from Binance API: current spot price is materially above the 80 threshold with a spot level near 85.25 at research time.

## What is uncertain

- Current spot level does not directly settle the April 17 noon ET candle; SOL can easily move more than 6% in ~3 days.
- The Polymarket page is authoritative for contract wording but not for future price path.
- Need to map Binance timestamps to the ET noon resolution window at settlement time; current research only verifies the stated timezone requirement, not the final settlement candle.

## Why this source may matter

It is the highest-quality combination available for this case: direct exchange data from the stated resolution venue plus the exact contract wording from the prediction market.

## Possible impact on the question

This source strongly supports why the market is priced at an extreme Yes probability: the contract threshold is currently well in-the-money relative to live Binance spot, so the market only needs SOL to avoid a roughly >6% drawdown by the relevant noon ET minute.

## Reliability notes

- Binance is the governing source of truth for settlement, so exchange-specific price behavior matters more than broad crypto averages.
- API outputs are machine-readable and directly tied to the exchange named in the rules.
- Independence is only medium because both the live price and the settlement reference come from the same venue; for contextual cross-checking, secondary market summaries can help but do not override Binance.
