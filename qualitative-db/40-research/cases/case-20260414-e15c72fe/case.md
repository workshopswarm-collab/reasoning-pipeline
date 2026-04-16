---
type: research_case
case_key: case-20260414-e15c72fe
case_id: 1ec499ae-1b30-465a-9092-02798586cc06
market_id: 551a0230-0ffb-42cc-9103-4bea5dc0cb4e
platform: polymarket
external_market_id: 0x73f9d7c48acbeefbe93bdcdc747947e2e8573945f11720617290fe672bf997d2
slug: bitcoin-above-70k-on-april-20
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $70,000 on April 20?

## Case identity
- case_key: `case-20260414-e15c72fe`
- case_id: `1ec499ae-1b30-465a-9092-02798586cc06`
- market_id: `551a0230-0ffb-42cc-9103-4bea5dc0cb4e`
- platform: `polymarket`
- external_market_id: `0x73f9d7c48acbeefbe93bdcdc747947e2e8573945f11720617290fe672bf997d2`
- slug: `bitcoin-above-70k-on-april-20`

## Market context
- current_price: `0.845`
- closes_at: `2026-04-20T12:00:00-04:00`
- resolves_at: `2026-04-20T12:00:00-04:00`

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
