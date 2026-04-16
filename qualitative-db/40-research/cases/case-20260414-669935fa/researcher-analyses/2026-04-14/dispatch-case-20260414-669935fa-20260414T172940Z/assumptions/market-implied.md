---
type: assumption_note
case_key: case-20260414-669935fa
dispatch_id: dispatch-case-20260414-669935fa-20260414T172940Z
research_run_id: f0de5e16-6721-4223-9e92-c774680e3d0a
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-bitcoin-reach-76-000-april-13-19
question: "Will Bitcoin reach $76,000 April 13-19?"
date_created: 2026-04-14
agent: Orchestrator
status: active
certainty: high
importance: high
time_horizon: "through 2026-04-19 ET market close"
related_entities: ["bitcoin"]
related_drivers: []
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-669935fa/researcher-analyses/2026-04-14/dispatch-case-20260414-669935fa-20260414T172940Z/personas/market-implied.md"]
tags: ["assumption", "binance", "settlement", "btc"]
driver:
---

# Assumption

A Binance BTC/USDT hourly candle high above $76,000 during the valid window is sufficient practical evidence that at least one qualifying Binance 1-minute candle also printed a high at or above $76,000.

## Why this assumption matters

The main finding moves from "very likely Yes" to "effectively already satisfied" only if the hourly high can be treated as strong evidence of an underlying qualifying 1-minute high.

## What this assumption supports

- A near-certain own probability estimate for Yes.
- Agreement with the market's near-100% pricing.
- The claim that the market is probably efficient rather than merely optimistic.

## Evidence or logic behind the assumption

Binance hourly klines aggregate underlying trades and shorter-interval candles. If an hourly candle reports a high of 76,038, then some trade within that hour printed at that level, implying the underlying minute-level high should also be at least that high unless there is an exchange-data inconsistency.

## What would falsify it

- A Binance 1-minute chart review showing no minute candle high at or above 76,000 during the relevant hour despite the hourly kline high above 76,000.
- Exchange correction or data restatement that revises the 14:00 UTC hourly high below 76,000.
- A Polymarket clarification that some special data-cleaning rule excludes that print.

## Early warning signs

- Settlement remains delayed or disputed despite the threshold appearing crossed.
- Polymarket or Binance publishes a correction notice.
- Traders materially sell the contract away from ~1.00 after the crossing claim.

## What changes if this assumption fails

The probability should fall back from near-certainty to a normal forward-looking estimate based on remaining time, realized volatility, and distance to threshold, because the current evidence would no longer show the event already happened.

## Notes that depend on this assumption

- `qualitative-db/40-research/cases/case-20260414-669935fa/researcher-analyses/2026-04-14/dispatch-case-20260414-669935fa-20260414T172940Z/personas/market-implied.md`