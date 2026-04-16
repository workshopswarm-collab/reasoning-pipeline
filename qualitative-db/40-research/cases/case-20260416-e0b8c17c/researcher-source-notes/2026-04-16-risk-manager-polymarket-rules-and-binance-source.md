---
type: source_note
case_key: case-20260416-e0b8c17c
dispatch_id: dispatch-case-20260416-e0b8c17c-20260416T050131Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-e0b8c17c | risk-manager
question: Will the price of Bitcoin be above $72,000 on April 20?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market rules page and Binance BTCUSDT direct market data
source_type: primary-plus-direct-market-data
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-e0b8c17c/researcher-analyses/2026-04-16/dispatch-case-20260416-e0b8c17c-20260416T050131Z/personas/risk-manager.md]
tags: [polymarket, binance, settlement, timing, btc]
---

# Summary

This source note combines the contract rules from the Polymarket market page with a direct verification pass against Binance BTC/USDT data. The key point is that settlement is not based on a daily close, other exchanges, or an average; it is based on the final Close of the Binance 1-minute BTC/USDT candle for 12:00 ET on April 20, 2026.

## Key facts extracted

- Polymarket rules say the market resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 20 has a final Close strictly higher than 72,000.
- The relevant official source of truth is Binance BTC/USDT with 1m candles selected.
- Price precision is determined by the number of decimals shown by the source.
- Noon ET on April 20, 2026 converts to 16:00 UTC because New York is on EDT at that date.
- Direct Binance API checks on 2026-04-16 show BTC/USDT trading around 75,000, materially above the threshold.
- Recent Binance daily candles show BTC/USDT closed above 72,000 on most recent days except April 12.
- A 14-day hourly sample from Binance showed 111 of 336 hourly closes above 72,000, indicating the threshold is currently above spot but still exposed to path risk and intraday volatility.

## Evidence directly stated by source

From the Polymarket rules page:
- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance, specifically the BTC/USDT 'Close' prices currently available at https://www.binance.com/en/trade/BTC_USDT with '1m' and 'Candles' selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

From direct Binance API checks:
- Recent 1-minute closes around the research time were near 74,900-75,010.
- Recent daily candles included closes of roughly 74,418 on Apr 13, 74,132 on Apr 14, 74,810 on Apr 15, and about 75,010 at the current partial Apr 16 reading.

## What is uncertain

- The market settles on a single future 1-minute close, so even if BTC remains above 72,000 on most surrounding periods, a fast selloff into 12:00 ET on April 20 could still flip the outcome.
- The browser page and direct API are not identical surfaces, so a reviewer should remember that the market text names the browser candle view as the governing settlement display even though direct API data is highly useful contextual verification.
- Crypto trades continuously; weekend and overnight path risk remains relevant before April 20 noon ET.

## Why this source may matter

This is the governing contract source plus the closest direct market data surface. It defines the exact settlement mechanics and validates that the current price cushion above 72,000 is real rather than inferred from other exchanges or stale commentary.

## Possible impact on the question

This source supports a Yes-lean because BTC/USDT is currently trading well above 72,000 on Binance, but it also sharpens the main risk-manager objection: the contract is fragile because resolution depends on one exact 1-minute Binance close at a specific timestamp rather than a broader daily average or end-of-day level.

## Reliability notes

- Polymarket rules page is the authoritative contract-definition source for this market.
- Direct Binance market data is highly credible for context and timing checks, though final settlement is described in terms of the Binance trading interface candle display.
- Independence is only medium because both pieces ultimately point back to the same exchange/source-of-truth family.