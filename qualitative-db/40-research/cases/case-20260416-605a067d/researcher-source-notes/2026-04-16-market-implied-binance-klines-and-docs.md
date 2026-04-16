---
type: source_note
case_key: case-20260416-605a067d
dispatch_id: dispatch-case-20260416-605a067d-20260416T142910Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: threshold-close-markets
entity: ethereum
topic: Binance ETHUSDT live pricing and kline documentation for noon-close settlement
question: Will the Binance ETH/USDT 12:00 ET 1-minute candle close on April 17 be above 2200?
driver: reliability
date_created: 2026-04-16
source_name: Binance Spot API klines endpoint and live ETHUSDT market data
source_type: exchange documentation plus live market data
source_url: https://developers.binance.info/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-16
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [ethereum]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-605a067d/researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/personas/market-implied.md
tags: [binance, klines, ethusdt, source-note]
---

# Summary

This source pair confirms how Binance defines one-minute klines and provides a live check that ETH/USDT was trading well above 2200 on April 16 morning ET, though with meaningful intraday downside versus the prior day’s highs.

## Key facts extracted

- Binance documentation states that `/api/v3/klines` returns candlestick bars and that klines are identified by open time.
- The response format explicitly includes open, high, low, and close, so the close field is mechanically aligned with the Polymarket rule.
- A live Binance API check at about 10:30 ET on April 16 showed ETH/USDT recent one-minute closes around 2294-2297, well above 2200.
- The recent 60-minute window in the same check showed a decline from about 2345 to about 2298, with a one-hour low near 2285.1.
- Binance 24h ticker data at the time of check showed lastPrice about 2298.33, 24h high about 2385.61, low about 2285.10, and daily change about -1.78%.

## Evidence directly stated by source

- Binance docs: "GET /api/v3/klines" returns "Kline/candlestick bars for a symbol" and the response includes "Close price".
- Binance docs: klines can be queried at interval `1m`.
- Live API output showed recent ETHUSDT close prints above 2288 and up to about 2296.57 in the sampled window.

## What is uncertain

- The API endpoint is a practical verification surface, but the Polymarket rule references the Binance trading UI specifically; these usually align, but the exact settlement review may rely on the UI-visible candle.
- Current price being above 2200 one day early does not guarantee the specific April 17 12:00 ET close will stay above 2200.
- Crypto can move materially in 24 hours, especially around round-number thresholds.

## Why this source may matter

This is the strongest direct contextual check for whether the market’s high Yes price is sensible. It also confirms the mechanism-specific meaning of a one-minute candle close, which is critical because this is a close-above contract, not a touch contract.

## Possible impact on the question

Supports a bullish prior because ETH is already about 4%+ above the threshold, so the market is not pricing a heroic move. But it also preserves a nontrivial path to No because the contract depends on one exact future minute close and recent drift has been downward from higher levels.

## Reliability notes

High reliability. Documentation is primary for endpoint semantics. Live API data is primary for current exchange pricing. The main caveat is settlement-surface ambiguity between Binance API output and the UI candle the contract explicitly cites, so this should be treated as strong verification rather than perfect legal finality.