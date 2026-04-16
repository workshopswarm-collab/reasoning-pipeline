---
type: source_note
case_key: case-20260415-e4a8d83c
dispatch_id: dispatch-case-20260415-e4a8d83c-20260415T230345Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: exchange-market-data
entity: btc
topic: case-20260415-e4a8d83c | risk-manager
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: reliability
date_created: 2026-04-15
source_name: Binance public API ticker and 1-minute klines
source_type: exchange market data / direct source
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: mildly supportive
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-e4a8d83c/researcher-analyses/2026-04-15/dispatch-case-20260415-e4a8d83c-20260415T230345Z/personas/risk-manager.md]
tags: [binance, api, btcusdt, kline, settlement-source]
---

# Summary

Direct Binance API checks showed BTC/USDT around 74,807.29 at capture time, above the 74,000 threshold, and returned recent 1-minute kline data with close values and timestamps. This is useful because the market settles specifically on a Binance 1-minute candle close, not a generic cross-exchange BTC quote.

## Key facts extracted

- Binance ticker endpoint returned: `{\"symbol\":\"BTCUSDT\",\"price\":\"74807.29000000\"}`.
- Recent 1-minute kline data were accessible directly from Binance public API.
- The checked sample klines showed close prices in the high 74.7k-74.8k range at capture time, comfortably above 74,000.
- Independent timezone verification mapped **2026-04-17 12:00:00 ET** to **2026-04-17 16:00:00 UTC**, which matters for selecting the correct settlement minute if using API timestamps.

## Evidence directly stated by source

- Ticker price capture: 74,807.29.
- Sample recent kline closes included values such as 74,813.92, 74,766.00, 74,760.01, 74,820.01, and 74,807.29.

## What is uncertain

- This check is a point-in-time observation about current levels, not a forecast guarantee for the April 17 noon ET settlement minute.
- Short-horizon BTC volatility can easily move the price by more than the roughly 800-point current cushion before settlement.
- API data confirm mechanics and current cushion but do not alone establish path stability into settlement.

## Why this source may matter

This is the closest thing to a direct resolution-source verification short of the final settlement candle itself. It reduces ambiguity around whether the contract can be audited programmatically and confirms that the threshold is currently in-the-money.

## Possible impact on the question

The direct source supports a Yes lean because BTC/USDT is currently above the threshold. But for a risk-manager view, it also highlights fragility: the live cushion is not huge relative to routine BTC daily movement, so a narrow time-specific settlement can still fail despite current spot being above 74k.

## Reliability notes

High reliability for current Binance state and for verifying accessible kline mechanics. Evidence independence versus Polymarket rules is medium rather than high, because Polymarket explicitly references Binance as the settlement source; still, Binance is the authoritative external source for the actual price series.