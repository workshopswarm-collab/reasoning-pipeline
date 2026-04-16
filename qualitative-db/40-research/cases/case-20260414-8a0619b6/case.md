---
type: research_case
case_key: case-20260414-8a0619b6
case_id: f1beab02-dafc-44e2-8dbf-b8dc200f52d3
market_id: 0bf3deba-41d6-4ff1-abd8-0ffe3f4a6588
platform: polymarket
external_market_id: 0x55dfaab5bde3bdc44eac96354731aaee8e35ab1341f92cd7de8e50186fa24d1d
slug: bitcoin-above-70k-on-april-18
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $70,000 on April 18?

## Case identity
- case_key: `case-20260414-8a0619b6`
- case_id: `f1beab02-dafc-44e2-8dbf-b8dc200f52d3`
- market_id: `0bf3deba-41d6-4ff1-abd8-0ffe3f4a6588`
- platform: `polymarket`
- external_market_id: `0x55dfaab5bde3bdc44eac96354731aaee8e35ab1341f92cd7de8e50186fa24d1d`
- slug: `bitcoin-above-70k-on-april-18`

## Market context
- current_price: `0.89`
- closes_at: `2026-04-18T12:00:00-04:00`
- resolves_at: `2026-04-18T12:00:00-04:00`

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
