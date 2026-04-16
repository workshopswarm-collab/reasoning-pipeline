---
type: source_note
case_key: case-20260416-5baa54ee
dispatch_id: dispatch-case-20260416-5baa54ee-20260416T032738Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-5baa54ee | risk-manager
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-20 above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT API plus Polymarket market rules
source_type: primary+resolution-context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-5baa54ee/researcher-analyses/2026-04-16/dispatch-case-20260416-5baa54ee-20260416T032738Z/personas/risk-manager.md]
tags: [binance, polymarket, resolution, btc]
---

# Summary

This note captures the direct resolution mechanics and current exchange context for the April 20 BTC-above-70k contract.

## Key facts extracted

- Polymarket rules say the market resolves from the Binance BTC/USDT 1-minute candle at **12:00 ET** on the date in the title.
- The winning condition is that the candle's final **Close** price is **strictly higher than 70,000**.
- The market is specifically about **Binance BTC/USDT**, not other exchanges or pairs.
- Binance spot API at research time returned BTCUSDT around **75,029.99**.
- Binance daily kline data for recent sessions shows BTC/USDT has recently closed above 70,000 each day in the fetched sample, with closes ranging roughly from **70,740.98** to **75,045.78**.

## Evidence directly stated by source

- Polymarket rule text explicitly defines the source of truth, time window, instrument, and threshold condition.
- Binance API directly reports current BTCUSDT price and recent daily klines.

## What is uncertain

- This note does not establish what the exact 12:00 ET 1-minute close will be on April 20.
- Binance web UI wording in the rule points to the website chart surface; API output is strongly indicative but not itself the expressly named visual surface.
- Intraday volatility, exchange microstructure events, or a sharp weekend move could still push the relevant minute close below 70,000 even if spot is comfortably above it today.

## Why this source may matter

This is the highest-value source set for a narrow, date-specific crypto resolution question because it identifies the governing source of truth and shows current distance from the strike.

## Possible impact on the question

Current exchange level being roughly 7% above the threshold supports a high Yes probability, but the contract remains fragile to path risk because only one exact minute close matters.

## Reliability notes

- Polymarket rules are the direct contract-resolution context and should govern interpretation.
- Binance API is a credible direct exchange source for current BTCUSDT context, but the contract names the Binance chart close specifically, so final settlement should still be checked against the designated Binance candle surface.
- Independence is limited because both direct pieces point back to the same exchange/source family.