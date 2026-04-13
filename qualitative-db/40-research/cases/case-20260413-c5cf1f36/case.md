---
type: research_case
case_key: case-20260413-c5cf1f36
case_id: 14e56c72-e6bb-45c4-be56-36a1376ec21f
market_id: 65e3d649-911e-4a10-8567-801e3558edcd
platform: polymarket
external_market_id: 0x329e36bc6f396a731d8417d57e598bdc8f099842797d239719a3b4f49794873b
slug: bitcoin-above-66k-on-april-15
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $66,000 on April 15?

## Case identity
- case_key: `case-20260413-c5cf1f36`
- case_id: `14e56c72-e6bb-45c4-be56-36a1376ec21f`
- market_id: `65e3d649-911e-4a10-8567-801e3558edcd`
- platform: `polymarket`
- external_market_id: `0x329e36bc6f396a731d8417d57e598bdc8f099842797d239719a3b4f49794873b`
- slug: `bitcoin-above-66k-on-april-15`

## Market context
- current_price: `0.9595`
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
