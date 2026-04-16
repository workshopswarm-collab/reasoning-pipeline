---
type: source_note
case_key: case-20260415-3d3080df
dispatch_id: dispatch-case-20260415-3d3080df-20260415T002239Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-3d3080df | market-implied
question: Will the Binance BTC/USDT 12:00 ET 1m candle close be above 70000 on April 20, 2026?
driver: reliability
date_created: 2026-04-14
source_name: Binance / Coinbase / Kraken spot and minute-price check
source_type: exchange APIs
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: market-implied
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-3d3080df/researcher-analyses/2026-04-15/dispatch-case-20260415-3d3080df-20260415T002239Z/personas/market-implied.md]
tags: [binance, coinbase, kraken, btc, price-check, verification]
---

# Summary

Direct exchange/API checks show BTC trading around 74.5k to 74.6k at review time, comfortably above the 70k threshold. Binance BTC/USDT printed about 74,534, Coinbase BTC-USD about 74,586, and Kraken XBT/USD about 74,577. Recent Binance one-minute candles also show BTC trading stably in the mid-74ks, which supports the market's high probability on a five-day-above-threshold framing.

## Key facts extracted

- Binance BTCUSDT ticker price: 74,534.16.
- Binance recent 1m candle closes in sampled output: roughly 74,470 to 74,633 before the latest 74,534 print.
- Coinbase spot BTC-USD: 74,586.545.
- Kraken XBT/USD last trade: 74,577.2.
- Cross-venue prices were tightly clustered within about 0.1% at the check time.

## Evidence directly stated by source

- Binance directly reports the exchange pair that governs settlement.
- Recent Binance minute candles indicate no immediate proximity risk to the 70k strike.
- Coinbase and Kraken corroborate the broader market level independently of Binance.

## What is uncertain

- These are current spot snapshots, not forecasts for April 20 noon ET.
- Cross-exchange agreement does not eliminate weekend/event risk between now and resolution.
- The contract settles on a single minute close, so intraday volatility near resolution could still matter even if the current level is well above the strike.

## Why this source may matter

This is the most direct available evidence for the market's current starting point. The fact that the governing Binance pair is already ~6.5% above the threshold helps explain why the market is pricing Yes at an extreme but not near-certainty level.

## Possible impact on the question

The current price level makes the market's optimistic baseline plausible. A Yes outcome does not require a rally; it mainly requires BTC to avoid a drawdown of roughly 6% to 7% over about five and a half days and to remain above the threshold at one specific settlement minute.

## Reliability notes

High reliability for current price verification because these are direct exchange/API reads, and independence is improved by checking multiple venues. Still, they are only indirect evidence for the future settlement condition.