---
type: source_note
case_key: case-20260415-2cb747e6
dispatch_id: dispatch-case-20260415-2cb747e6-20260415T122916Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: reliability
date_created: 2026-04-15
source_name: Binance public BTCUSDT ticker and 1m kline spot-check, with Coinbase and Kraken context
source_type: exchange API / market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, coinbase, kraken, spot-price, verification]
---

# Summary

This note captures a live spot-check of the actual settlement venue plus two independent exchange references. It does not settle the contract, but it materially supports the view that the market's ~89.5% pricing is grounded in a large current cushion above the 72k threshold.

## Key facts extracted

- Binance public ticker at research time returned `BTCUSDT = 74212.76`.
- Recent Binance 1-minute candles around the fetch window were all above 74.1k, including a candle closing at `74212.76` at `2026-04-15T12:30:59.999Z`.
- Coinbase spot at the same pull was about `74238.005` USD.
- Kraken last trade / best quote context was around `74199.8-74199.9` USD.
- Cross-venue prices were tightly clustered within roughly a few dozen dollars, suggesting no major venue-specific dislocation at the check time.
- The current Binance spot level implies a cushion of roughly `+2.21k` versus the 72k threshold, about `3.1%` above the strike.

## Evidence directly stated by source

- Direct current price on the actual settlement venue/pair.
- Direct recent 1-minute candle closes on Binance.
- Direct external exchange spot references showing broadly similar BTC/USD pricing.

## What is uncertain

- This is only a point-in-time verification on April 15, not the settlement candle on April 16 at noon ET.
- BTC can move materially intraday; a 3% cushion is meaningful but not invulnerable.
- Coinbase and Kraken are contextual because the contract resolves only on Binance BTC/USDT.

## Why this source may matter

It answers the main market-implied question directly: whether the current live price environment plausibly supports a ~90% chance of staying above 72k by the specific settlement time tomorrow.

## Possible impact on the question

Strongly supportive of the market's bullish baseline. The market only needs BTC/USDT to avoid a drop of a bit more than 3% by the settlement minute. The external exchange checks reduce the risk that Binance is showing an isolated erroneous print or unusual basis.

## Reliability notes

High reliability for the Binance API check because it is the stated resolution venue and pair. Evidence independence is medium because Coinbase/Kraken are separate venues but still reflect the same global BTC market. Good extra-verification value for an extreme-probability case.