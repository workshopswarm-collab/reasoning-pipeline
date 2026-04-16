---
type: source_note
case_key: case-20260416-8bef05aa
dispatch_id: dispatch-case-20260416-8bef05aa-20260416T144205Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: Binance BTC/USDT recent daily and 1-minute price context
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-21 close above 72000?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance API klines for BTCUSDT
source_type: exchange market data
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=10
source_date: 2026-04-16
credibility: high
recency: high
stance: bullish-threshold-context
certainty: medium
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-8bef05aa/researcher-analyses/2026-04-16/dispatch-case-20260416-8bef05aa-20260416T144205Z/personas/catalyst-hunter.md
tags: [binance, btcusdt, source-note, threshold-market, price-context]
---

# Summary

Direct Binance market data shows BTC/USDT has already been trading well above 72,000 in the days immediately preceding the Apr 21 noon-ET observation window, with daily closes from Apr 13-15 all above 74,000 and a recent 1-minute snapshot around 74,000-74,032 on Apr 16.

## Key facts extracted

- Binance daily klines fetched on 2026-04-16 showed:
  - 2026-04-13 close: 74,417.99; high: 74,900.00
  - 2026-04-14 close: 74,131.55; high: 76,038.00
  - 2026-04-15 close: 74,809.99; high: 75,425.00
  - 2026-04-16 intraday daily kline snapshot: open 74,809.99; high 75,267.85; low 73,309.85; current close field snapshot 74,000.01 at fetch time
- Binance 1-minute klines fetched on 2026-04-16 showed five most recent closes between 73,906.22 and 74,030.67.
- The specific future governing candle for 2026-04-21 12:00 ET is not yet available; querying Binance for the exact future minute returned an empty result, confirming the event has not yet occurred rather than merely being unverified.

## Evidence directly stated by source

- Binance API returned recent BTCUSDT daily and 1-minute kline rows directly from the exchange market data endpoint.
- Binance API returned no row yet for the exact future minute corresponding to 2026-04-21 12:00 ET / 16:00 UTC.

## What is uncertain

- This source does not say why BTC is above 72,000 or whether it will remain there through Apr 21 noon ET.
- Exchange API availability here is used as direct context, but the contract text references the Binance trading interface candle display as the formal resolution surface.

## Why this source may matter

This is the closest available direct evidence for the governing market source. It establishes both the correct source-of-truth family (Binance BTC/USDT candles) and the key current state: BTC is already comfortably above the 72,000 threshold with several days left before the relevant candle prints.

## Possible impact on the question

The source materially supports a Yes-lean because the market only requires the Apr 21 noon-ET 1-minute close to be above 72,000, and current Binance spot levels are already roughly 2,000 above that threshold. The relevant catalyst question becomes whether any near-term event or volatility regime could push BTC back below 72,000 by the specific observation minute.

## Reliability notes

- High credibility for direct price context because Binance is the named resolution source family.
- Moderate source-of-truth caveat: the contract cites the Binance UI candle display, while this note uses Binance's API endpoint rather than a screenshot of the UI. The pricing venue is the same, but final settlement should still defer to the stated Binance candle surface at the target minute.