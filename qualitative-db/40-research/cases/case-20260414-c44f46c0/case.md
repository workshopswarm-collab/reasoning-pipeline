---
type: research_case
case_key: case-20260414-c44f46c0
case_id: 69d39235-2e21-4036-b541-4b8c20af5668
market_id: cacd25f7-9569-4f26-ac38-8ed6365ea5b2
platform: polymarket
external_market_id: 0xa4a43a5eeecd0a184c18a49762c0dd14e576caac659cc081f7dae4c909063ea3
slug: bitcoin-above-68k-on-april-19
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $68,000 on April 19?

## Case identity
- case_key: `case-20260414-c44f46c0`
- case_id: `69d39235-2e21-4036-b541-4b8c20af5668`
- market_id: `cacd25f7-9569-4f26-ac38-8ed6365ea5b2`
- platform: `polymarket`
- external_market_id: `0xa4a43a5eeecd0a184c18a49762c0dd14e576caac659cc081f7dae4c909063ea3`
- slug: `bitcoin-above-68k-on-april-19`

## Market context
- current_price: `0.9575`
- closes_at: `2026-04-19T12:00:00-04:00`
- resolves_at: `2026-04-19T12:00:00-04:00`

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
