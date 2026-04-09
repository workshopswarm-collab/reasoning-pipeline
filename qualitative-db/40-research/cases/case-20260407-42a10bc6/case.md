---
type: research_case
case_key: case-20260407-42a10bc6
case_id: af8252c9-6c0c-4d2a-b2ba-09e72921a263
market_id: 2dc46bde-6ea2-469e-95d2-a4d942b08936
platform: polymarket
external_market_id: 0x8f797219cc6712b3939973f31f5bff6ed087ec51b766b84b5c2b7a87c89ac43f
slug: bitcoin-above-68k-on-april-7
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $68,000 on April 7?

## Case identity
- case_key: `case-20260407-42a10bc6`
- case_id: `af8252c9-6c0c-4d2a-b2ba-09e72921a263`
- market_id: `2dc46bde-6ea2-469e-95d2-a4d942b08936`
- platform: `polymarket`
- external_market_id: `0x8f797219cc6712b3939973f31f5bff6ed087ec51b766b84b5c2b7a87c89ac43f`
- slug: `bitcoin-above-68k-on-april-7`

## Market context
- current_price: `0.845`
- closes_at: `2026-04-07T12:00:00-04:00`
- resolves_at: `2026-04-07T12:00:00-04:00`

## Description
This market will resolve to "Yes" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final "Close" price higher than the price specified in the title. Otherwise, this market will resolve to "No".

The resolution source for this market is Binance, specifically the BTC/USDT "Close" prices currently available at https://www.binance.com/en/trade/BTC_USDT with "1m" and "Candles" selected on the top bar.

Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs.

Price precision is determined by the number of decimal places in the source.

## Case surfaces
- `researcher-swarm-current.md` = latest/current researcher swarm pointers
- `timeline.md` = programmatic lifecycle summary
- `researcher-source-notes/` = case-level source provenance across analyses
- `researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/...` = append-only analysis generations
