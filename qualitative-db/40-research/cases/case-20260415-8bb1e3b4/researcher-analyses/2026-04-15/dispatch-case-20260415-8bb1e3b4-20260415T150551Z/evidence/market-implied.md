---
type: evidence_map
case_key: case-20260415-8bb1e3b4
dispatch_id: dispatch-case-20260415-8bb1e3b4-20260415T150551Z
research_run_id: d2b8458e-af56-45d8-8214-33b2e44804d3
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-binance-btc-usdt-1-minute-candle-at-12-00-et-on-2026-04-20-close-above-70000
question: "Will the Binance BTC/USDT 1-minute candle at 12:00 ET on 2026-04-20 close above 70000?"
driver: reliability
date_created: 2026-04-15
agent: market-implied
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-8bb1e3b4/researcher-analyses/2026-04-15/dispatch-case-20260415-8bb1e3b4-20260415T150551Z/personas/market-implied.md"]
tags: ["evidence-map", "bitcoin", "market-implied", "threshold"]
---

# Summary

The market's high-Yes price is mostly explained by simple distance-to-threshold math plus short time-to-expiry, but that logic needs a small discount for single-minute timing risk and Binance-specific settlement risk.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle at 12:00 ET on April 20, 2026 have a final close above 70,000?

## Current lean

Lean Yes, but slightly less strongly than the market.

## Prior / starting view

Starting view was that an 88% price might be a bit rich for a single-minute snapshot contract, but the market should be treated seriously because BTC was already believed to be in the 70k+ regime.

## Evidence supporting the claim

- **Current Binance spot materially above threshold** — source note: `2026-04-15-market-implied-binance-spot-context.md`; direct; high weight. BTCUSDT around 74,044 means roughly a 5.5% cushion.
- **Recent 24h Binance range stayed above threshold** — same note; direct/contextual; medium-high weight. Even the recent low near 73,514 remained above 70,000.
- **Independent contextual confirmation from CoinGecko** — source note: `2026-04-15-market-implied-coingecko-context.md`; indirect/contextual; medium weight. Confirms BTC broadly trades around 74.1k.
- **Short time to settlement** — derived from contract date; contextual; medium weight. Five days is not much time for a large regime change absent a catalyst.
- **Market aggregation itself** — Polymarket source note; contextual; medium weight. 88% likely reflects traders already doing the same distance-to-threshold math.

## Evidence against the claim

- **Single-minute contract fragility** — Polymarket contract note; direct contract interpretation; medium weight. A temporary dump exactly at noon ET could flip settlement even if BTC is above 70k before and after.
- **Binance-specific source risk** — Polymarket and Binance notes; direct/contextual; low-medium weight. This is not an average of exchanges; exchange-specific microstructure matters.
- **BTC can move >5% in a few days** — contextual market knowledge supported by current negative 24h move and crypto volatility regime; indirect; medium weight.

## Ambiguous or mixed evidence

- The current 24h move is negative but modest. It slightly increases caution without seriously threatening the threshold.
- CoinGecko confirms the general price level, but because settlement is Binance-only, it cannot rule out venue-specific issues.

## Conflict between inputs

No major factual conflict. The main disagreement is weighting-based: whether the market's 88% adequately discounts single-minute and venue-specific resolution risk.

## Key assumptions

- BTC remains in the current low-to-mid 70k regime.
- No major macro or crypto shock forces a selloff before April 20 noon ET.
- Binance prints remain representative and operationally normal at settlement.

## Key uncertainties

- Exact volatility over the next five days.
- Event risk from macro headlines or crypto-specific news.
- Whether noon ET on April 20 coincides with abnormal volatility.

## Disconfirming signals to watch

- BTC breaking materially below 73k and staying heavy.
- Sudden spike in realized volatility.
- Binance operational issues or unusual cross-venue divergence.

## What would increase confidence

- BTC holding or expanding above 74k through the next 24-48 hours.
- Another day where Binance lows stay comfortably above 70k.
- No sign of exchange-specific disruption into settlement.

## Net update logic

The evidence moved the view from "88% may be too optimistic for a one-minute print" to "high-70s / low-80s is still too low given current spot and short horizon." The market is directionally right, but I still trim the probability modestly because this is a narrow timestamped contract, not a broad price-range call.

## Suggested downstream use

- orchestrator synthesis input
- forecast update
- decision-maker review