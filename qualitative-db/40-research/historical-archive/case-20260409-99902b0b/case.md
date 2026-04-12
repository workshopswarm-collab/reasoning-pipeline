---
type: research_case
case_key: case-20260409-99902b0b
case_id: 7ca18805-5e58-43f9-aabb-e1dcca482acf
market_id: 78e378dc-438f-4fb9-bac6-b058eb003d73
platform: polymarket
external_market_id: 0xbf2a3a8ede9dbe4bf934c2109366fcad96a1d89288265cb3ff451bc2f7a0a205
slug: bitcoin-above-70k-on-april-10
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $70,000 on April 10?

## Case identity
- case_key: `case-20260409-99902b0b`
- case_id: `7ca18805-5e58-43f9-aabb-e1dcca482acf`
- market_id: `78e378dc-438f-4fb9-bac6-b058eb003d73`
- platform: `polymarket`
- external_market_id: `0xbf2a3a8ede9dbe4bf934c2109366fcad96a1d89288265cb3ff451bc2f7a0a205`
- slug: `bitcoin-above-70k-on-april-10`

## Market context
- current_price: `0.885`
- closes_at: `2026-04-10T12:00:00-04:00`
- resolves_at: `2026-04-10T12:00:00-04:00`

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
