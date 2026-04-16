---
type: source_note
case_key: case-20260415-04e7318a
dispatch_id: dispatch-case-20260415-04e7318a-20260415T145259Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-04e7318a | risk-manager
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules for Bitcoin above 70000 on April 20
source_type: market-rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [risk-manager-finding, risk-manager-evidence-map]
tags: [polymarket, rules, binance, resolution, timezone]
---

# Summary

This source is the governing contract/rules surface for the market. It defines the exact threshold test, exchange, trading pair, timestamp convention, and price field used for settlement.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for **12:00 in ET timezone (noon)** on **April 20, 2026** has a final **Close** price **higher than 70,000**.
- Otherwise it resolves No.
- The resolution source is Binance, specifically the BTC/USDT chart with **1m** candles.
- The market is explicitly about **Binance BTC/USDT**, not other exchanges or other pairs.
- Price precision is determined by the number of decimal places visible in the source.

## Evidence directly stated by source

Direct rule text from the market page:
- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/BTC_USDT with \"1m\" and \"Candles\" selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The public market page does not itself provide the future April 20 candle, only the settlement rule.
- The page does not explain operational contingencies such as exchange UI/API outages, though it does specify Binance as source of truth.
- The wording references the 12:00 ET candle, so a timing misread between ET, UTC, and candle-open/candle-close conventions remains an implementation risk for researchers if not checked separately.

## Why this source may matter

This source governs the contract and therefore outranks general BTC spot-price commentary. A correct research note must analyze the probability that the specific Binance BTC/USDT 12:00 ET 1-minute candle on April 20 closes above 70,000, not merely whether BTC is generally bullish.

## Possible impact on the question

The rules reduce some ambiguity because they specify exchange, pair, interval, timezone, and field. They also create a narrow operational/timing risk: a thesis can be directionally right on BTC while still missing on the exact noon ET one-minute close.

## Reliability notes

- High reliability as the governing source of truth for settlement.
- Not independent evidence about future BTC price direction; it is authoritative on mechanics, not on outcome forecasting.
- Should be paired with at least one direct or contextual price source for forecasting.