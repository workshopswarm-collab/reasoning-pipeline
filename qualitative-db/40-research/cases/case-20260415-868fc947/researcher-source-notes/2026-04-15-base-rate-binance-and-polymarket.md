---
type: source_note
case_key: case-20260415-868fc947
dispatch_id: dispatch-case-20260415-868fc947-20260415T090047Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-16 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT API + Polymarket market page
source_type: primary_market_and_resolution_source
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5 ; https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-868fc947/researcher-analyses/2026-04-15/dispatch-case-20260415-868fc947-20260415T090047Z/personas/base-rate.md]
tags: [source-note, binance, polymarket, resolution-source, btc]
---

# Summary

This note captures the governing contract mechanics and a spot verification of the live Binance BTC/USDT price relative to the 72,000 threshold.

## Key facts extracted

- Polymarket shows the 72,000 outcome around 88%, implying roughly 0.875-0.88 market probability for "Yes" on this threshold.
- The contract resolves from the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on 2026-04-16, using the final Close value only.
- Binance spot API returned BTCUSDT around 74,110 on 2026-04-15 during this run, already about 2,110 above the threshold.
- Recent Binance 1-minute klines in the verification pass all sat above 74,100, indicating no immediate proximity to the strike.

## Evidence directly stated by source

- Polymarket rule text: market resolves "Yes" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the specified date has a final Close price higher than 72,000.
- Binance ticker endpoint returned `{"symbol":"BTCUSDT","price":"74110.01000000"}` during the run.
- Binance recent 1-minute kline endpoint showed closes clustered around 74,110-74,167 during the verification pass.

## What is uncertain

- This is a spot snapshot roughly one day before resolution, not the settlement candle itself.
- The exact Binance UI candle label behavior in ET is inferred from the contract text plus API availability, not independently screen-verified from the interactive chart.
- Short-horizon crypto volatility can still move BTC back below 72,000 by the relevant noon ET minute.

## Why this source may matter

It directly anchors both the market-implied baseline and the authoritative settlement source. For a narrow date-and-time market, contract mechanics matter almost as much as the current spot level.

## Possible impact on the question

Because BTC was already materially above the strike and the governing source is Binance spot BTC/USDT rather than a broader index, the base rate for remaining above 72,000 over the next roughly 27 hours appears favorable unless there is a meaningful drawdown or exchange-specific distortion.

## Reliability notes

- Binance is the stated source of truth, so its relevance is highest even if exchange-specific idiosyncrasies exist.
- Polymarket page text is useful for contract interpretation but is not itself the settlement authority.
- Evidence independence is limited because both the contract and the live price context orbit the same market setup; a separate contextual source is still useful for volatility/base-rate framing.
