---
type: research_case
case_key: case-20260416-63fb3082
case_id: c1cf2dc2-4a7b-4a76-b283-d8fb2ead083e
market_id: 8e484c02-63d0-4bdc-83ee-fab3c26e0c4c
platform: polymarket
external_market_id: 0xc6f68e3d5ce9efabbba7123bcceba0316b81e07707390869587a967ad4f87b16
slug: bitcoin-above-68k-on-april-21
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $68,000 on April 21?

## Case identity
- case_key: `case-20260416-63fb3082`
- case_id: `c1cf2dc2-4a7b-4a76-b283-d8fb2ead083e`
- market_id: `8e484c02-63d0-4bdc-83ee-fab3c26e0c4c`
- platform: `polymarket`
- external_market_id: `0xc6f68e3d5ce9efabbba7123bcceba0316b81e07707390869587a967ad4f87b16`
- slug: `bitcoin-above-68k-on-april-21`

## Market context
- current_price: `0.9525`
- closes_at: `2026-04-21T12:00:00-04:00`
- resolves_at: `2026-04-21T12:00:00-04:00`

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
