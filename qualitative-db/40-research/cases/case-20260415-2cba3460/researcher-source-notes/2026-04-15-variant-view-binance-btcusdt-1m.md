---
type: source_note
case_key: case-20260415-2cba3460
dispatch_id: dispatch-case-20260415-2cba3460-20260415T115730Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-16 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT 1m klines API
source_type: exchange market data / direct source surface
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=20
source_date: 2026-04-15
credibility: high
recency: intraday
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-2cba3460/researcher-analyses/2026-04-15/dispatch-case-20260415-2cba3460-20260415T115730Z/personas/variant-view.md]
tags: [binance, btcusdt, minute-candle, resolution-source, direct-evidence]
---

# Summary

Direct Binance BTC/USDT one-minute kline data fetched on 2026-04-15 showed BTC trading materially above 72,000 immediately before 08:00 ET, with the latest sampled one-minute closes around 74,194. This is not itself the settling candle, but it verifies that the market is currently in-the-money by roughly 2,200 points and that the contract depends on a single future Binance one-minute close rather than a broader daily average.

## Key facts extracted

- Recent Binance 1m closes from 11:40:00 UTC through 11:59:59 UTC on 2026-04-15 were all above 74,000.
- The sampled close at 11:59 UTC was 74,194.00000000.
- This corresponds to 07:59 ET on 2026-04-15, about 28 hours before the contract resolves.
- The current spot cushion over the 72,000 threshold was therefore about 2,194 points at sampling time.

## Evidence directly stated by source

- Binance exposes BTCUSDT one-minute candlestick data directly via the klines endpoint.
- Each candle includes open time, close time, and final close price.
- The most recent sampled close prices were:
  - 11:57 UTC close: 74,173.23000000
  - 11:58 UTC close: 74,187.69000000
  - 11:59 UTC close: 74,194.00000000

## What is uncertain

- The source note does not establish where BTC will trade at 12:00 ET on 2026-04-16.
- It does not prove the Binance website UI will display identically to the API, although both refer to Binance BTC/USDT one-minute candles.
- It does not rule out a large downside move, exchange-specific dislocation, or operational issue before the settling minute.

## Why this source may matter

This is the closest direct source surface to the market’s governing resolution source. It verifies both current price regime and the relevant instrument/timescale. For a date-specific threshold contract, that is more decision-useful than generic BTC headlines.

## Possible impact on the question

Because BTC is currently well above 72,000 on the same exchange/pair used for settlement, the burden of proof for a "No" view is a sizeable downside move or a Binance-specific resolution problem before noon ET on Apr 16.

## Reliability notes

- High credibility for direct exchange pricing on Binance BTC/USDT.
- Still slightly weaker than observing the exact eventual website candle at settlement time, because the contract names the Binance trading surface specifically.
- Best used as direct current-state evidence plus resolution-mechanics verification, not as a full forecast by itself.
