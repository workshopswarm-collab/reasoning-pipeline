---
type: source_note
case_key: case-20260416-653ab0f8
dispatch_id: dispatch-case-20260416-653ab0f8-20260416T090226Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-18
question: Will the Binance BTC/USDT 1-minute candle close at 12:00 PM ET on 2026-04-18 above 72000?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket rules page plus Binance spot/API checks
source_type: primary_market_rule_and_primary_price_source
source_url: https://polymarket.com/event/bitcoin-above-on-april-18
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-653ab0f8/researcher-analyses/2026-04-16/dispatch-case-20260416-653ab0f8-20260416T090226Z/personas/catalyst-hunter.md]
tags: [polymarket, binance, contract, resolution, btc]
---

# Summary

This note captures the governing contract wording from Polymarket and a direct verification of live Binance BTCUSDT spot/API levels and candle-field semantics.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 in ET on 2026-04-18 has a final Close strictly higher than 72,000.
- The relevant timestamp is noon ET on 2026-04-18, which converts to 2026-04-18T16:00:00Z.
- Current spot reference during this pass was roughly 74.67k on Binance spot and ~74.72k on CoinGecko, leaving BTC about 2.6k above the strike with about two days to resolution.
- Binance API responses confirm the kline structure includes a Close field and that BTCUSDT is actively trading with tight order book spread and large 24h quote volume.
- Polymarket page showed the 72,000 line trading around 88% at fetch time, consistent with the assignment baseline of 0.875.

## Evidence directly stated by source

From Polymarket rules page:
- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/BTC_USDT with \"1m\" and \"Candles\" selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

From Binance API spot checks on 2026-04-16:
- ticker price: 74682.81
- 24h stats included high 75425.00, low 73580.85, last 74669.88, quote volume about 1.00B USDT
- depth endpoint showed a 0.01 USDT top-of-book spread at check time

## What is uncertain

- This note does not itself prove the 2026-04-18 12:00 ET close; it only verifies the governing mechanism and the current buffer above strike.
- Binance web UI extraction failed in the fetch tool, so the live API was used to verify current price mechanics instead of the rendered chart page.
- Exchange-specific operational incidents, sudden weekend macro shocks, or a sharp risk-off move could still pull BTC below 72k by the relevant minute.

## Why this source may matter

This is the most important source set because the market is explicitly settled off Binance BTCUSDT 1-minute close data, not generalized BTC/USD pricing. It also anchors the current distance from strike and verifies the exact timing window.

## Possible impact on the question

The direct implication is that the strike is currently meaningfully in the money for Yes. Any bearish catalyst before Saturday noon ET would need to move Binance BTCUSDT down more than roughly 3.5% from the checked level, and the final minute close matters more than broader daily averages or other exchanges.

## Reliability notes

- Polymarket contract wording is the governing settlement description and therefore authoritative for interpretation.
- Binance API is highly relevant as the named source-of-truth venue, though final settlement is based on the web-visible Binance BTCUSDT candle close referenced in the contract.
- Evidence independence is medium: both sources point to the same venue/market, which is appropriate here because the contract is explicitly venue-specific.