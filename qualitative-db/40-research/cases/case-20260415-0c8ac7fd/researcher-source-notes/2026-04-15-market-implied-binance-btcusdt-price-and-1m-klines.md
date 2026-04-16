---
type: source_note
case_key: case-20260415-0c8ac7fd
dispatch_id: dispatch-case-20260415-0c8ac7fd-20260415T190844Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: Binance BTC/USDT spot price and 1-minute candle mechanics before Apr 17 noon ET close-threshold market
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on Apr 17 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance spot API (ticker price and 1m klines)
source_type: exchange / primary market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: supports-yes
certainty: medium
importance: high
novelty: low
agent: market-implied
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-analyses/2026-04-15/dispatch-case-20260415-0c8ac7fd-20260415T190844Z/personas/market-implied.md
  - qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-analyses/2026-04-15/dispatch-case-20260415-0c8ac7fd-20260415T190844Z/evidence/market-implied.md
tags: [source-note, binance, btc, 1m-candle, governing-source]
---

# Summary

Direct Binance API checks show BTC/USDT trading materially above the 72,000 threshold on 2026-04-15, about two days before the relevant Apr 17 12:00 ET resolving candle. The same source family also returns recent 1-minute klines, confirming both that the governing market surface is accessible and that the relevant contract condition is a close-above test on a specific 1-minute candle rather than a touch/high test.

## Key facts extracted

- Binance ticker endpoint returned `{"symbol":"BTCUSDT","price":"74646.66000000"}` during this run.
- This spot level is about 3.7% above the 72,000 strike.
- Binance 1-minute klines endpoint returned recent candles with closes around `74603.99`, `74665.09`, `74647.99`, `74679.83`, and `74646.65`.
- The recent klines show ordinary minute-to-minute variation measured in tens of dollars, not thousands.
- Because the contract resolves on the final `Close` of the `12:00 ET` 1-minute candle on Apr 17, the key mechanism is whether BTC remains above 72,000 at that exact minute close on Binance, not whether it trades above earlier in the day.

## Evidence directly stated by source

- Binance ticker price at time of check: `74646.66000000`.
- Recent Binance 1-minute candle closes remained in the mid-74.6k area.
- Binance is the explicit governing source named in the contract rules.

## What is uncertain

- The source does not itself say what the Apr 17 noon ET close will be.
- The exact Apr 17 resolving candle is still in the future.
- API accessibility does not guarantee the website UI will display identically, though both are Binance surfaces.

## Why this source may matter

This is the most direct available source because the contract explicitly resolves against Binance BTC/USDT 1-minute candle close data. It supports the market’s high Yes probability by showing BTC comfortably above the strike with modest recent minute volatility relative to the 2.6k cushion.

## Possible impact on the question

If BTC remains in roughly the current area, the Yes outcome should resolve comfortably. A No outcome likely requires a meaningful drawdown before or by the exact Apr 17 12:00 ET close, not merely normal intraminute noise.

## Reliability notes

- High credibility for the contract’s specific mechanism because Binance is the named resolution source.
- Operational caveat: the rule text references the Binance trading interface with 1m candles selected, while this note uses Binance API endpoints as an additional direct surface from the same source family. That is close to the governing source but not literally a screenshot of the exact resolving UI state. This lowers ambiguity somewhat but does not eliminate it fully.