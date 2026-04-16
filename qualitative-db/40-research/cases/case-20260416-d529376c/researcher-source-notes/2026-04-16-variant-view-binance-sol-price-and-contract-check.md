---
type: source_note
case_key: case-20260416-d529376c
dispatch_id: dispatch-case-20260416-d529376c-20260416T030247Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: token-price
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle close above 80 on April 19, 2026?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance API + Polymarket market rules
source_type: primary_and_resolution_context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-15T23:04:36-04:00
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [sol, solana]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [variant-view-finding]
tags: [binance, polymarket, resolution-check, timing-check]
---

# Summary

This note captures the direct source-of-truth surface for the market (Binance SOL/USDT 1m candles) and the contract mechanics stated on Polymarket. It also records the current Binance spot context relevant to the April 19 >80 threshold.

## Key facts extracted

- Polymarket states the market resolves from the Binance SOL/USDT 1-minute candle at **12:00 ET (noon)** on April 19, using the final **Close** price.
- The contract is specifically about **Binance SOL/USDT**, not other exchanges or pairs.
- A recent Binance API spot quote showed **SOLUSDT = 85.30000000**.
- Recent Binance 1-minute klines around the observation time showed closes in the **85.14-85.30** range.
- Binance 24h ticker showed **lastPrice 85.28**, **high 85.83**, **low 82.65**, and **24h change +2.303%**.
- A local timestamp conversion check confirmed recent 1-minute kline timestamps mapped cleanly from UTC into ET; e.g. 1776308640000 = **2026-04-15 23:04 ET**.

## Evidence directly stated by source

- Polymarket rules explicitly define all material conditions for resolution: Binance, SOL/USDT, 1-minute candle, 12:00 ET, and final close above 80.
- Binance API directly reported current SOLUSDT spot and recent 1-minute candle closes above 80.

## What is uncertain

- The market resolves on April 19 noon ET, so the relevant uncertainty is future price path over ~3.5 days, not current price level alone.
- The web-fetch path could not render Binance's human trading page; API endpoints were used instead for direct exchange data verification.
- Current price being above 80 does not guarantee the April 19 noon candle will still be above 80.

## Why this source may matter

This is the governing contract/source pair. It defines both what counts for settlement and the most direct present-state evidence about whether the threshold is currently in/out of the money.

## Possible impact on the question

The direct evidence supports a bullish baseline because SOL is already about 5+ dollars above the strike with modest 24h upward momentum. The main variant angle is not that the threshold is currently missed, but that the market may be somewhat overconfident about the durability of that cushion over a multi-day horizon.

## Reliability notes

- Binance API is a strong direct source for spot and kline data and is closely aligned with the stated settlement source.
- Polymarket market page is a strong source for contract wording but not for independent market context.
- Evidence independence is limited because settlement mechanics and direct price source are tightly linked; a separate contextual source is still useful for verification.