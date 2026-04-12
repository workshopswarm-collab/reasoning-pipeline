---
type: research_case
case_key: case-20260407-56d31eea
case_id: 7c68130a-b08c-4a85-81d9-5f5366271b48
market_id: aa8953af-93e5-41d1-8da2-6a5bc5e2f5ad
platform: polymarket
external_market_id: 0x4feab9c6b38e1be4f0cf364ef579f58334e611e29dc08d46293bd8ce8da7b8b6
slug: bitcoin-above-66k-on-april-7
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $66,000 on April 7?

## Case identity
- case_key: `case-20260407-56d31eea`
- case_id: `7c68130a-b08c-4a85-81d9-5f5366271b48`
- market_id: `aa8953af-93e5-41d1-8da2-6a5bc5e2f5ad`
- platform: `polymarket`
- external_market_id: `0x4feab9c6b38e1be4f0cf364ef579f58334e611e29dc08d46293bd8ce8da7b8b6`
- slug: `bitcoin-above-66k-on-april-7`

## Market context
- current_price: `0.9595`
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
