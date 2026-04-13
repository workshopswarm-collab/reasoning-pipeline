---
type: research_case
case_key: case-20260413-f68a8c5c
case_id: 72ac64c8-296a-4156-aecf-f166716b1781
market_id: 0d431c73-55d6-4d66-88de-3ecde384b28b
platform: polymarket
external_market_id: 0x0047decf5a127be6ec0ba4eee78c9b224eb2d5445aff6241377272eacd42114f
slug: bitcoin-above-68k-on-april-14
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $68,000 on April 14?

## Case identity
- case_key: `case-20260413-f68a8c5c`
- case_id: `72ac64c8-296a-4156-aecf-f166716b1781`
- market_id: `0d431c73-55d6-4d66-88de-3ecde384b28b`
- platform: `polymarket`
- external_market_id: `0x0047decf5a127be6ec0ba4eee78c9b224eb2d5445aff6241377272eacd42114f`
- slug: `bitcoin-above-68k-on-april-14`

## Market context
- current_price: `0.9595`
- closes_at: `2026-04-14T12:00:00-04:00`
- resolves_at: `2026-04-14T12:00:00-04:00`

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
