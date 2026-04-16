---
type: research_case
case_key: case-20260416-2ab48f50
case_id: a1cf777c-25e6-4057-8f20-070dddab486f
market_id: 367ed8d7-c08e-4588-a449-c83aead47ec3
platform: polymarket
external_market_id: 0x0457acf7468ed957f2422686cf5e63fb54d69fb116b67f74f6b64fd8e8b377dc
slug: bitcoin-above-74k-on-april-17
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $74,000 on April 17?

## Case identity
- case_key: `case-20260416-2ab48f50`
- case_id: `a1cf777c-25e6-4057-8f20-070dddab486f`
- market_id: `367ed8d7-c08e-4588-a449-c83aead47ec3`
- platform: `polymarket`
- external_market_id: `0x0457acf7468ed957f2422686cf5e63fb54d69fb116b67f74f6b64fd8e8b377dc`
- slug: `bitcoin-above-74k-on-april-17`

## Market context
- current_price: `0.62`
- closes_at: `2026-04-17T12:00:00-04:00`
- resolves_at: `2026-04-17T12:00:00-04:00`

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
