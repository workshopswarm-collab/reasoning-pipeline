---
type: source_note
case_key: case-20260416-143465dc
dispatch_id: dispatch-case-20260416-143465dc-20260416T191321Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: market-structure
entity: sol
topic: solana-reach-90-april-13-19
question: "Will Solana reach $90 April 13-19?"
driver: operational-risk
date_created: 2026-04-16
source_name: Binance SOLUSDT API resolution-context check
source_type: exchange-api
source_url: https://api.binance.com/api/v3/klines?symbol=SOLUSDT&interval=1m&startTime=1776052800000&endTime=1776657600000&limit=1000
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: high
agent: variant-view
related_entities: [sol, solana]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, solusdt, threshold-market, venue-specific, evidence-floor]
---

# Summary

This source note captures the governing exchange-level evidence for the April 13-19 touch market. The contract resolves from Binance SOL/USDT 1-minute candle highs, so Binance minute data is the most decision-relevant direct evidence available before settlement.

## Key facts extracted

- Polymarket rules specify the market resolves **Yes** if **any Binance SOL/USDT 1-minute candle** from **2026-04-13 00:00 ET through 2026-04-19 23:59 ET** has a final **High** of **90.00 or greater**.
- A full pull of Binance 1-minute klines across that window returned **5,237 minutes** checked.
- The **maximum recorded high** in that pulled window was **89.15**.
- The timestamp of that maximum high was **1776366000000**, which converts to **2026-04-16 15:00:00 ET**.
- The minimum low in the pulled window was **81.54**.
- Binance 24h ticker context at check time showed:
  - `lastPrice`: **88.91**
  - `highPrice`: **89.15**
  - `lowPrice`: **83.80**
  - `priceChangePercent`: **4.563%**
- A focused verification pass around the peak minute showed multiple nearby candles with highs between **89.04 and 89.15**, confirming the peak zone was real rather than a single obviously malformed print.

## Evidence directly stated by source

- The highest direct Binance 1-minute high found in the relevant contract window was **89.15**, which is **below 90**.
- Binance therefore had **not yet touched 90** in the checked window as of this run.
- Current Binance trading context was close enough to the strike that a touch remained plausible within the remaining time.

## What is uncertain

- This note does not prove what will happen after the pull time and before the market window ends.
- The contract wording shown on Polymarket says Binance 1-minute candle **High** controls; if exchange backfill, chart-vs-API presentation differences, or rounding/display conventions matter at the exact threshold, that could still affect later review.
- I did not independently verify Binance web-chart UI output against API formatting at the exact boundary because the API already gives direct venue data and there was no >=90 print in the checked sample.

## Why this source may matter

This is the most important direct source because the market is explicitly venue-specific and threshold-specific. General spot commentary is much less useful than directly checking whether Binance actually printed a 90 handle in the contract window.

## Possible impact on the question

This source supports a variant view against simple consensus confidence: the market may price a near-touch as highly likely, but the best direct evidence currently says the event has **not yet happened** and that the peak so far remains **85 cents short** of resolution. That keeps Yes live but preserves meaningful downside to the current 74% market price.

## Reliability notes

- Reliability is **high** because Binance is the governing source named by contract.
- Independence is **low-to-medium** relative to the settlement source because it is the same venue, but that is appropriate here rather than a flaw.
- Main limitation: this is a pre-resolution snapshot, not final settlement proof.