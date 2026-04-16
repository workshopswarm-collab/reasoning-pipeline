---
type: source_note
case_key: case-20260416-bbc8ed19
dispatch_id: dispatch-case-20260416-bbc8ed19-20260416T072336Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-bbc8ed19 | variant-view
question: Will the Binance BTC/USDT 1-minute candle at 12:00 ET on 2026-04-20 close above 72000?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page and Binance BTCUSDT API snapshots
source_type: primary-market-rules plus exchange-market-data
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-bbc8ed19/researcher-analyses/2026-04-16/dispatch-case-20260416-bbc8ed19-20260416T072336Z/personas/variant-view.md]
tags: [polymarket, binance, settlement-rules, btc]
---

# Summary

This note captures the direct rule surface for the market and a contemporaneous Binance price snapshot. The key takeaway is that resolution is not based on a broad daily BTC level or another exchange; it is specifically the final close of the Binance BTC/USDT 1-minute candle corresponding to 12:00 ET on 2026-04-20.

## Key facts extracted

- Polymarket states the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on the specified date has a final close above 72000.
- Polymarket states the governing source is Binance BTC/USDT with 1m candles selected.
- Price precision is determined by the source decimals.
- On 2026-04-16, Polymarket showed the 72000 line around 84%-85% Yes, matching the assignment current_price of 0.845.
- Binance public API snapshots on 2026-04-16 showed BTCUSDT around 74909.73, about 4.0% above 72000.
- Recent daily Binance closes from April 13 to April 16 were 74417.99, 74131.55, 74809.99, and ~74909.73 intraday, indicating BTC has recently traded above the threshold but with meaningful multi-day volatility.
- Recent hourly Binance data showed 0 of the last 24 hourly closes below 72000, but 31 of the last 96 hourly closes were below 72000, showing that a four-day horizon is still path-sensitive.

## Evidence directly stated by source

From the market rules page:
- Resolution is based on the Binance BTC/USDT 1-minute candle at 12:00 ET.
- The metric used is the final Close price.
- The source is Binance, not other exchanges or pairs.

From Binance API data:
- BTCUSDT last price on 2026-04-16 snapshot: 74909.73.
- 24h high/low snapshot: 75425.00 / 73514.00.

## What is uncertain

- The market page is clear about the governing surface, but the exact UTC timestamp mapping of the 12:00 ET candle on April 20 depends on daylight-saving handling; in EDT that should correspond to 16:00 UTC.
- Current price level does not settle the market; the position four days later at the exact one-minute close can still differ materially.
- Binance front-end chart presentation could differ from API display formatting even if underlying candles match.

## Why this source may matter

This is the core source set for contract interpretation. It establishes the exact thing that must happen for Yes to win and highlights that a short intraday exchange-specific close, rather than a looser daily price narrative, governs settlement.

## Possible impact on the question

The direct rule surface supports a more cautious estimate than a simple 'BTC is already well above 72k' narrative would imply. Because resolution depends on one exact 1-minute Binance close at a specified local time four days in the future, short-horizon volatility, exchange-specific pricing, and timing mechanics matter more than they would in a broad end-of-day or multi-exchange market.

## Reliability notes

- Polymarket is the authoritative source for contract wording.
- Binance is the authoritative source-of-truth for the observed settlement value.
- These two sources are not independent, but together they are the correct direct evidence set for a rule-sensitive price market.
- Independence for directional probability still remains limited without broader contextual market sources; this note should therefore be paired with explicit caveats rather than treated as a complete forecasting basis.