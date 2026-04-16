---
type: source_note
case_key: case-20260415-bebdf03e
dispatch_id: dispatch-case-20260415-bebdf03e-20260415T221944Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-21
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-21 close above 72000?
driver: reliability
date_created: 2026-04-15
source_name: Kraken BTC/USD public ticker and OHLC API
source_type: contextual-market-data
source_url: https://api.kraken.com/0/public/Ticker?pair=XBTUSD
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: medium
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-bebdf03e/researcher-analyses/2026-04-15/dispatch-case-20260415-bebdf03e-20260415T221944Z/personas/variant-view.md]
tags: [kraken, cross-venue, context, btc]
---

# Summary

Kraken public market data provides an independent contextual check that BTC is trading in roughly the same mid-75k area across a second major venue, reducing concern that the Binance reading is an exchange-specific outlier at the time of research.

## Key facts extracted

- Kraken ticker API returned last trade around **75,031.2**.
- Kraken day range in the same response showed a high around **75,280** and low around **73,558.1**.
- Kraken 1-minute OHLC endpoint is available and returns minute-by-minute candles, confirming that minute-resolution BTC price variation is ordinary and nontrivial.

## Evidence directly stated by source

- Ticker response included last trade `c: 75031.20000`.
- Ticker response included high `h: 75280.00000` and low `l: 73558.10000` for the daily window.
- OHLC endpoint returned rolling 1-minute bars for XBTUSD.

## What is uncertain

- Kraken is not the governing source of truth for this contract.
- BTC/USD on Kraken is not identical to BTC/USDT on Binance, so this source should not be used for settlement, only context.

## Why this source may matter

This source helps assess whether the market is relying on a broadly consistent BTC level or on a venue-specific anomaly. It also shows that while BTC is comfortably above 72k now, intraday and minute-level moves of hundreds to over a thousand dollars remain plausible, which matters for a date-specific noon-close contract.

## Possible impact on the question

The cross-venue check supports the broad bullish baseline because the spot level is not unique to Binance. At the same time, the observed daily range reminds us the contract is still vulnerable to a several-percent drawdown by the deadline, which is the core credible variant against an 81.5% implied probability.

## Reliability notes

- Kraken public API is credible for contextual market pricing.
- It is meaningfully independent from Polymarket and from Binance as a separate venue, though all crypto spot venues are linked by the same underlying global market.
- Useful for context and independence, not for contract interpretation or settlement.