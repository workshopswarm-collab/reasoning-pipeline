---
type: source_note
case_key: case-20260415-1e5e80f9
dispatch_id: dispatch-case-20260415-1e5e80f9-20260415T080017Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT spot API price check
source_type: exchange_api
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [variant-view.md, variant-view.sidecar.json]
tags: [binance, btcusdt, direct-source, resolution-context]
---

# Summary

Direct Binance API spot check during the run returned BTCUSDT at 73,711.71 on 2026-04-15 around 08:02Z / 04:02 ET, already above the 72,000 threshold but only about 24 hours before the relevant settlement candle.

## Key facts extracted

- Endpoint queried: `https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT`
- HTTP status: 200
- Returned payload: `{\"symbol\":\"BTCUSDT\",\"price\":\"73711.71000000\"}`
- Observed spot price is about 1,711.71 above the target threshold.

## Evidence directly stated by source

- Binance reported a live BTCUSDT price of 73,711.71 at query time.

## What is uncertain

- This is not the settlement value. The market resolves from the Binance 1-minute candle close at 12:00 ET on 2026-04-16, not from a spot API snapshot on 2026-04-15.
- API spot price and the later specified 1-minute candle close can diverge materially over a 24-hour window.
- The note does not by itself prove what candle timestamp Binance will display on the web chart, only that Binance is the relevant venue and BTC is currently trading above the threshold.

## Why this source may matter

- It is the most direct currently accessible Binance-origin signal in the run.
- It tests whether the market’s 82.5% implied probability is directionally plausible versus live exchange price.
- It also highlights a variant risk: only a ~2.3% move down from the observed price would push the settlement candle below 72,000.

## Possible impact on the question

- Supports a baseline lean toward Yes because BTC is currently above the threshold on the actual exchange family used for resolution.
- Also supports a less-bullish-than-market interpretation because the buffer above 72,000 is not large for a 24-hour crypto window.

## Reliability notes

- High credibility for contemporaneous Binance spot price.
- Medium relevance to final settlement because contract resolution depends on a specific later 1-minute close on the Binance chart surface rather than a generic live API tick.