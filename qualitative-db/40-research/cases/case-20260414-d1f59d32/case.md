---
type: research_case
case_key: case-20260414-d1f59d32
case_id: e2710ad6-5fc2-47f8-b9de-2413fbc7f8f8
market_id: ccfc6b7f-7f5a-41d1-949f-49a0b794fe00
platform: polymarket
external_market_id: 0xfb00ff35de120017fabe413f445c7260fcbbe3c17b11d69108f953ab573b7c92
slug: bitcoin-above-74k-on-april-15
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $74,000 on April 15?

## Case identity
- case_key: `case-20260414-d1f59d32`
- case_id: `e2710ad6-5fc2-47f8-b9de-2413fbc7f8f8`
- market_id: `ccfc6b7f-7f5a-41d1-949f-49a0b794fe00`
- platform: `polymarket`
- external_market_id: `0xfb00ff35de120017fabe413f445c7260fcbbe3c17b11d69108f953ab573b7c92`
- slug: `bitcoin-above-74k-on-april-15`

## Market context
- current_price: `0.815`
- closes_at: `2026-04-15T12:00:00-04:00`
- resolves_at: `2026-04-15T12:00:00-04:00`

## Description
This market will resolve to "Yes" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final "Close" price higher than the price specified in the title. Otherwise, this market will resolve to "No".

The resolution source for this market is Binance, specifically the BTC/USDT "Close" prices currently available at https://www.binance.com/en/trade/BTC_USDT with "1m" and "Candles" selected on the top bar.

Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs.

Price precision is determined by the number of decimal places in the source.

## Case surfaces
- `researcher-swarm-current.md` = latest/current researcher swarm pointers
- `timeline.md` = programmatic lifecycle summary
- `researcher-source-notes/` = case-level source provenance across researcher analyses
- `researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/...` = append-only researcher analysis generations
