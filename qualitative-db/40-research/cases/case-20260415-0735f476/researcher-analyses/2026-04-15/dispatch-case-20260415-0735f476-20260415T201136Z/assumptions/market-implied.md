---
type: assumption_note
case_key: case-20260415-0735f476
dispatch_id: dispatch-case-20260415-0735f476-20260415T201136Z
research_run_id: 9ee1999a-f097-4354-b2b9-6b4c0ca257df
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin-threshold-close
entity: bitcoin
topic: "persistence of BTC above 70000 into the specific resolution minute"
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 70000 on April 20, 2026?"
date_created: 2026-04-15
agent: market-implied
status: active
certainty: medium
importance: high
time_horizon: short-dated
related_entities: ["binance", "bitcoin"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["threshold-proximity", "resolution-surface-ambiguity"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-0735f476/researcher-source-notes/2026-04-15-market-implied-polymarket-rules-and-price.md", "qualitative-db/40-research/cases/case-20260415-0735f476/researcher-source-notes/2026-04-15-market-implied-binance-live-price-check.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-0735f476/researcher-analyses/2026-04-15/dispatch-case-20260415-0735f476-20260415T201136Z/personas/market-implied.md"]
tags: ["assumption", "btc", "binance", "threshold-close"]
driver:
---

# Assumption

BTC/USDT being roughly 6-7% above 70,000 on Binance on April 15 means the probability of still printing a noon ET 1-minute close above 70,000 on April 20 is very high, absent a material adverse move or exchange-specific anomaly.

## Why this assumption matters

The market's 93% pricing only makes sense if current distance from the threshold is a meaningful cushion rather than noise. My estimate depends on treating the current gap as large enough that ordinary short-term volatility is unlikely to erase it exactly at the resolution minute.

## What this assumption supports

- A high Yes probability estimate.
- Rough agreement with the market-implied view.
- The interpretation that the market is pricing persistence rather than hidden special information.

## Evidence or logic behind the assumption

- Binance is the governing venue, and current Binance spot is around 74,621.
- Recent 1m closes are also comfortably above 70,000.
- The threshold is not marginally close; it is thousands of dollars below spot.
- For a close-only market, a large existing cushion is still meaningful even though it is weaker than in a touch market.

## What would falsify it

- A sharp BTC selloff taking Binance BTC/USDT near or below 70,000 before April 20.
- Evidence that the relevant noon ET candle historically behaves with unusual one-minute dislocations around the resolution time.
- Exchange-specific execution, outage, or pricing anomalies affecting Binance BTCUSDT.

## Early warning signs

- BTC losing the 72,000-73,000 area with momentum.
- Macro or crypto-specific shock causing broad risk-off repricing.
- Unusual divergence between Binance and other major BTC/USD venues.

## What changes if this assumption fails

The market-implied 93% would look overstretched, and the probability should drop quickly toward a more balanced range if BTC revisits the threshold zone before resolution.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260415-0735f476/researcher-analyses/2026-04-15/dispatch-case-20260415-0735f476-20260415T201136Z/personas/market-implied.md
