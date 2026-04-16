---
type: assumption_note
case_key: case-20260416-66f6f47e
dispatch_id: dispatch-case-20260416-66f6f47e-20260416T141457Z
research_run_id: 6e5f4e1f-3d3f-4191-9dc5-ba1afbf0d6cf
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin-threshold-daily-close-window
entity: bitcoin
topic: "persistence above threshold into exact settlement minute"
question: "Will the Binance BTC/USDT 1-minute candle close at 12:00 ET on April 21 be above 72000?"
driver: reliability
date_created: 2026-04-16
agent: base-rate
status: active
certainty: medium
importance: high
time_horizon: short
related_entities: ["binance", "bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-66f6f47e/researcher-analyses/2026-04-16/dispatch-case-20260416-66f6f47e-20260416T141457Z/personas/base-rate.md"]
tags: ["assumption-note", "btc", "threshold-market", "settlement-minute"]
---

# Assumption

The key assumption is that BTC will continue trading near its current regime and still be above 72000 on Binance at the exact April 21 12:00 ET 1-minute close.

## Why this assumption matters

The market is already near-realized in a broad sense because BTC is currently above the threshold, but resolution still depends on persistence into one exact future minute close.

## What this assumption supports

- A Yes probability above 50%
- Agreement or rough agreement with the market leaning Yes
- Treating current price level as meaningful evidence rather than irrelevant noise

## Evidence or logic behind the assumption

- BTC is already materially above 72000 on Binance.
- Recent Binance candles show repeated trading above the threshold rather than a one-off spike.
- For a highly liquid 24/7 asset, a threshold already cleared several days ahead often remains within the plausible trading band unless a meaningful reversal occurs.

## What would falsify it

- A broad crypto selloff that pushes BTC back below 72000 and keeps it there into April 21.
- Exchange-specific dislocation on Binance BTC/USDT around the settlement minute.
- New macro or crypto-specific shock that changes regime over the remaining days.

## Early warning signs

- BTC losing 72000 and failing repeated retests.
- Rising realized volatility with lower highs into April 20-21.
- Binance-specific basis moving materially below other large BTC/USD venues.

## What changes if this assumption fails

The case would shift from a persistence question to a reacquisition question, and the probability should fall materially because the market resolves on one exact minute rather than any intraday touch.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260416-66f6f47e/researcher-analyses/2026-04-16/dispatch-case-20260416-66f6f47e-20260416T141457Z/personas/base-rate.md