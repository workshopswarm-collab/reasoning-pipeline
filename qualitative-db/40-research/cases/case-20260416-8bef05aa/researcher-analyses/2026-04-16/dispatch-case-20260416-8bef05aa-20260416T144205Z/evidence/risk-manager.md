---
type: evidence_map
case_key: case-20260416-8bef05aa
dispatch_id: dispatch-case-20260416-8bef05aa-20260416T144205Z
research_run_id: a8df6a32-3081-4b9c-a9e2-23f9c06c0571
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin-threshold-close
entity: bitcoin
topic: "Evidence netting for BTC above 72k on April 21 noon ET close"
question: "Will Binance BTC/USDT 1-minute candle close above 72,000 at 12:00 ET on April 21, 2026?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-8bef05aa/researcher-source-notes/2026-04-16-risk-manager-polymarket-rules-binance-source.md", "qualitative-db/40-research/cases/case-20260416-8bef05aa/researcher-source-notes/2026-04-16-risk-manager-binance-spot-and-recent-klines.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-8bef05aa/researcher-analyses/2026-04-16/dispatch-case-20260416-8bef05aa-20260416T144205Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "binance", "threshold-close"]
---

# Summary

Evidence nets to a moderate Yes lean, but the main underpriced risk is contract narrowness: the market does not ask whether BTC generally stays strong through April 21, only whether one exact Binance 1-minute noon ET close exceeds 72,000.

## Question being evaluated

Will Binance BTC/USDT close above 72,000 on the 12:00 ET 1-minute candle on April 21, 2026?

## Current lean

Lean Yes, but with lower confidence than a simple current-price-above-threshold framing suggests.

## Prior / starting view

Starting view was roughly in line with the market: being above 72k several days early is supportive, but a single-minute-close contract should trade below a generic spot-above-threshold intuition.

## Evidence supporting the claim

- **Current Binance spot is already above threshold**
  - Source: Binance ticker source note.
  - Why it matters: current state starts from a favorable level with roughly 2.8% buffer.
  - Direct vs indirect: direct venue-matched contextual evidence.
  - Weight: high.

- **Recent daily highs/closes show BTC has spent meaningful time above 72k**
  - Source: Binance kline source note.
  - Why it matters: suggests 72k is not an outlier price level needing a major breakout.
  - Direct vs indirect: direct venue-matched contextual evidence.
  - Weight: medium-high.

- **Market itself prices Yes near 70.5%**
  - Source: assignment context / Polymarket price.
  - Why it matters: crowd baseline reflects current consensus that threshold is more likely than not to hold at the relevant time.
  - Direct vs indirect: indirect decision benchmark, not proof.
  - Weight: medium.

## Evidence against the claim

- **Contract resolves on one exact minute close, not any touch or end-of-day average**
  - Source: Polymarket rules source note.
  - Why it matters causally: path risk remains high even when spot is currently above threshold.
  - Direct vs indirect: direct contract evidence.
  - Weight: high.

- **Recent intraday volatility is large enough to erase a ~2.8% buffer**
  - Source: Binance kline source note.
  - Why it matters causally: BTC can move more than the current cushion within ordinary 4h/daily ranges.
  - Direct vs indirect: direct venue-matched contextual evidence.
  - Weight: high.

- **There are still several days until the resolution minute**
  - Source: assignment timing plus contract rules.
  - Why it matters causally: more time for a macro/risk-off move or ordinary retracement to matter.
  - Direct vs indirect: direct timing condition.
  - Weight: medium-high.

## Ambiguous or mixed evidence

- **Being on Binance is both a strength and a risk**
  - Strength because current evidence is venue-matched.
  - Risk because exchange-specific prints and one-minute-close mechanics create narrow settlement dependence.

## Conflict between inputs

- No major factual conflict.
- Main disagreement is weighting-based: how much to discount current bullish price context because the contract is a narrow time-and-close question.
- What would resolve it: stronger directional evidence into April 20-21 or a materially larger buffer above 72k.

## Key assumptions

- Current price buffer remains informative through the next several days.
- Binance venue mechanics remain clean and unambiguous at settlement.
- No large adverse BTC move occurs into the noon ET window.

## Key uncertainties

- Whether BTC remains above 72k into the exact settlement minute.
- Whether risk-off or liquidation-style moves compress price near resolution.
- Whether April 21 noon ET tends to coincide with elevated intraday volatility.

## Disconfirming signals to watch

- BTC loses 72k on Binance and cannot reclaim it going into April 20-21.
- Repeated 4-hour closes trend downward toward low 72k / high 71k.
- Exchange-specific operational/data issues around the settlement window.

## What would increase confidence

- BTC holding above 74k into April 20.
- Additional direct Binance closing data near the relevant ET time showing stable cushion.
- Reduced realized volatility over the next few sessions.

## Net update logic

The net is not “BTC bullish therefore Yes.” The update is narrower: current venue-matched price and recent trading range make Yes more likely than not, but the contract’s one-minute-close requirement justifies a meaningful discount from naive spot-based confidence.

## Suggested downstream use

Use as forecast input and synthesis input. The key reusable contribution is the stress test on narrow settlement mechanics rather than a broad BTC market thesis.