---
type: research_case
case_key: case-20260416-653ab0f8
case_id: e2993e71-6a46-440b-b55a-b5fea18970e4
market_id: 7778dd4c-fd44-4778-8eb2-7a5cbaac96b6
platform: polymarket
external_market_id: 0xad1812c9d570c11e3511619da4b6ecc865d7f9b326dc0241d441b7e172dffa2e
slug: bitcoin-above-72k-on-april-18
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $72,000 on April 18?

## Case identity
- case_key: `case-20260416-653ab0f8`
- case_id: `e2993e71-6a46-440b-b55a-b5fea18970e4`
- market_id: `7778dd4c-fd44-4778-8eb2-7a5cbaac96b6`
- platform: `polymarket`
- external_market_id: `0xad1812c9d570c11e3511619da4b6ecc865d7f9b326dc0241d441b7e172dffa2e`
- slug: `bitcoin-above-72k-on-april-18`

## Market context
- current_price: `0.875`
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
