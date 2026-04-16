---
type: evidence_map
case_key: case-20260415-9c95ce3a
dispatch_id: dispatch-case-20260415-9c95ce3a-20260415T173129Z
research_run_id: 961c9d0c-3650-4d67-8894-877c6586a16a
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-72-000-on-april-17
question: "Will the price of Bitcoin be above $72,000 on April 17?"
driver: operational-risk
date_created: 2026-04-15
agent: catalyst-hunter
related_entities: ["bitcoin"]
related_drivers: ["operational-risk"]
proposed_entities: []
proposed_drivers: ["macro-risk-sentiment"]
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "btc", "catalyst-hunter"]
---

# Evidence map

## Net view

Current direct evidence favors `Yes` because Binance BTC/USDT is trading above the strike with a meaningful but not enormous cushion. The main negative mechanism is a late macro/risk-off selloff or exchange-specific distortion near the exact reference minute.

## Evidence for Yes

- Polymarket contract wording is clear and narrow.
- Binance spot/API checks during the run show BTC/USDT around 74.15k, above 72k.
- Recent hourly sample stayed above 72k.
- No single dominant bearish crypto-native catalyst surfaced for the remaining window.

## Evidence for No

- BTC can move >3% in under two days.
- A single-minute close contract is more fragile than a daily-close-style intuition suggests.
- Macro data / risk sentiment remains the most plausible repricing catalyst.

## Main conflict or fragility

The core conflict is between current price cushion/inertia and the fact that a short-lived move at the exact wrong minute is sufficient for `No`.

## Why this map exists

This case is not complex enough to require a large evidence map, but this compact map preserves the exact netting logic for later audit.