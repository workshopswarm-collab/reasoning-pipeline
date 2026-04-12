---
type: source_note
case_key: case-20260411-6669dcdb
dispatch_id: dispatch-case-20260411-6669dcdb-20260411T003353Z
analysis_date: 2026-04-11
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260411-6669dcdb | risk-manager
question: Will the Binance BTC/USDT 1m candle for 2026-04-11 12:00 ET close above 72000?
driver: reliability
date_created: 2026-04-10
source_name: Cross-exchange BTC spot context (CoinGecko, Coinbase, Kraken) with Binance 24h ticker
source_type: market data aggregators and exchange spot APIs
source_url: https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true&include_last_updated_at=true
source_date: 2026-04-11
credibility: medium-high
recency: high
stance: slightly supportive
certainty: medium
importance: medium
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [risk-manager finding, risk-manager evidence map]
tags: [spot-price, context, cross-exchange, volatility]
---

# Summary

Independent spot references broadly agreed that BTC was trading near 72.9k at research time, modestly above the 72k threshold. This supports a mild Yes lean but also shows the margin is small enough that intraday volatility still matters.

## Key facts extracted

- Binance `ticker/24hr` showed BTCUSDT last price 72887.79, 24h high 73434.00, low 71426.15, and +1.50% over 24h.
- CoinGecko simple price returned bitcoin at 72898 USD with +1.46% 24h change.
- Coinbase spot returned BTC-USD at 72912.815.
- Kraken ticker returned XBTUSD last trade around 72905.2 and 24h low/high roughly 72850 / 72973.8 in the short snapshot shown.
- A 1000-minute Binance 1m sample used for quick realized-volatility context had closes ranging from 71433.12 to 73412.25, with about 80.7% of sampled minute closes above 72k.

## Evidence directly stated by source

- Independent sources all placed BTC very near 72.9k at research time.
- Binance 24h range shows 72k was breached on the downside within the last day, so the threshold is not trivially safe.

## What is uncertain

- Coinbase and Kraken are contextual only; they do not settle the market.
- The 1000-minute sample is only a recent window and should not be over-read as a literal probability forecast.
- Cross-exchange price consistency does not eliminate the possibility of Binance-specific divergence at the exact resolution minute.

## Why this source may matter

These sources provide an independence check on the current level and help gauge whether the threshold is comfortably in the money or only narrowly so.

## Possible impact on the question

The evidence supports a Yes lean because BTC is currently above 72k across venues, but the recent range shows enough volatility that a drop below 72k by the noon ET minute remains plausible.

## Reliability notes

- Good as contextual confirmation because the sources are recent and independent of the Polymarket page.
- Not authoritative for settlement because only Binance BTCUSDT counts.