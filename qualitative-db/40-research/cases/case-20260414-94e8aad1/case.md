---
type: research_case
case_key: case-20260414-94e8aad1
case_id: 95184dba-b597-4c48-9e7e-a88e62982683
market_id: b5021d2c-0b79-403b-a5df-3221dc962905
platform: polymarket
external_market_id: 0x24c9d39348a3ca9f3464ac85ac14826cd40c25fb2f4baf545602f1208baaf16c
slug: bitcoin-above-70k-on-april-16
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $70,000 on April 16?

## Case identity
- case_key: `case-20260414-94e8aad1`
- case_id: `95184dba-b597-4c48-9e7e-a88e62982683`
- market_id: `b5021d2c-0b79-403b-a5df-3221dc962905`
- platform: `polymarket`
- external_market_id: `0x24c9d39348a3ca9f3464ac85ac14826cd40c25fb2f4baf545602f1208baaf16c`
- slug: `bitcoin-above-70k-on-april-16`

## Market context
- current_price: `0.9595`
- closes_at: `2026-04-16T12:00:00-04:00`
- resolves_at: `2026-04-16T12:00:00-04:00`

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
