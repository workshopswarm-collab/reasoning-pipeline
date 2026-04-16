---
type: assumption_note
case_key: case-20260415-0c8ac7fd
dispatch_id: dispatch-case-20260415-0c8ac7fd-20260415T190844Z
research_run_id: 4f5c0429-380f-4d57-9a0d-33d2e9379c67
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: btc-threshold-close
entity: bitcoin
topic: cushion-above-threshold-persists-into-noon-et-close
question: "Will the price of Bitcoin be above $72,000 on April 17?"
driver: operational-risk
date_created: 2026-04-15
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: "through 2026-04-17T12:00:00-04:00"
related_entities: ["binance", "bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-source-notes/2026-04-15-risk-manager-binance-polymarket-resolution-context.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-analyses/2026-04-15/dispatch-case-20260415-0c8ac7fd-20260415T190844Z/personas/risk-manager.md"]
tags: ["assumption-note", "btc", "threshold", "close-market"]
---

# Assumption

Bitcoin will retain enough price cushion that the **Binance BTC/USDT 12:00 ET 1-minute close on April 17** remains above 72,000.

## Why this assumption matters

The finding is bullish largely because BTC is currently trading materially above the threshold; if that cushion disappears before the exact resolving minute, the market can still resolve No despite being above 72,000 now.

## What this assumption supports

- A Yes probability materially above 50%
- A view that the market is roughly right but slightly overconfident
- A risk framing centered on path and timing risk rather than directional bearishness today

## Evidence or logic behind the assumption

- Current Binance 1-minute closes are around 74.6k-74.7k, leaving roughly a 2.6k-2.7k cushion versus the 72k threshold.
- The live Polymarket ladder also prices 74k near coin-flip while 72k remains in the high-80s, implying the market sees substantial but not complete downside buffer.
- BTC would need a noticeable selloff before the precise settlement minute for Yes to fail.

## What would falsify it

- Binance BTCUSDT trades back below 72,000 and stays weak into late morning ET on April 17.
- A sharp macro or crypto-specific shock compresses BTC quickly enough that the noon ET close prints below 72,000.
- Exchange-specific dislocation on Binance causes that venue's close to diverge below threshold even if broader spot markets remain stronger.

## Early warning signs

- Repeated failures to hold above ~74k and a loss of recent intraday support.
- BTC sliding toward low-73k / high-72k ahead of the event.
- Elevated volatility or risk-off headlines close to the settlement window.
- Binance-specific price weakness versus other major venues.

## What changes if this assumption fails

The view should move materially toward No or at least toward market parity, because the contract is a precise timestamp close market rather than a broad-window or touch market.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-analyses/2026-04-15/dispatch-case-20260415-0c8ac7fd-20260415T190844Z/personas/risk-manager.md
- qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-analyses/2026-04-15/dispatch-case-20260415-0c8ac7fd-20260415T190844Z/evidence/risk-manager.md