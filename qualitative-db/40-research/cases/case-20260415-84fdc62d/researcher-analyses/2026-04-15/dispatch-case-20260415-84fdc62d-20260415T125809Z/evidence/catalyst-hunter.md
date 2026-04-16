---
type: evidence_map
case_key: case-20260415-84fdc62d
dispatch_id: dispatch-case-20260415-84fdc62d-20260415T125809Z
research_run_id: e5d88500-22c1-41d7-9001-5f63ddf7a26b
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-20
question: "Will the price of Bitcoin be above $70,000 on April 20?"
driver: reliability
date_created: 2026-04-15
agent: catalyst-hunter
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["catalyst-hunter.md", "catalyst-hunter.sidecar.json"]
tags: ["evidence-map", "btc", "catalyst-calendar"]
---

# Summary
Evidence nets to a Yes lean, but with a narrower margin than the 86% market price implies because this is a one-minute noon snapshot on a volatile asset.

## Question being evaluated
Will Binance BTC/USDT close above $70,000 on the 12:00 ET one-minute candle on April 20, 2026?

## Current lean
Yes, moderately strong but not overwhelming.

## Prior / starting view
Starting view was that a market at 87.5% likely embeds both current price cushion and a belief that no near-term catalyst will break the regime.

## Evidence supporting the claim
- Binance spot around $74.2k on April 15.
  - Source: Binance API source note.
  - Why it matters: direct exchange-level cushion of roughly 6% versus threshold.
  - Direct/indirect: near-direct.
  - Weight: high.
- Recent daily Binance closes mostly above $70k.
  - Source: Binance API source note.
  - Why it matters: shows current regime is already consistently above threshold rather than needing a fresh breakout.
  - Direct/indirect: near-direct contextual.
  - Weight: medium-high.
- Major scheduled U.S. macro catalysts are not concentrated inside the remaining window.
  - Source: Fed calendar + BLS CPI schedule source note.
  - Why it matters causally: fewer obvious timed repricing triggers before resolution.
  - Direct/indirect: contextual.
  - Weight: medium.
- Contract wording uses a single Binance BTC/USDT candle, reducing ambiguity about what must happen.
  - Source: Polymarket rules note.
  - Why it matters: avoids diffuse interpretation; if regime holds, Yes should settle cleanly.
  - Direct/indirect: direct for contract logic.
  - Weight: medium.

## Evidence against the claim
- The contract is a narrow noon-ET one-minute close, not a daily close or average.
  - Source: Polymarket rules note.
  - Why it matters causally: increases sensitivity to intraday volatility and wick risk.
  - Direct/indirect: direct.
  - Weight: high.
- BTC remains a volatile asset with recent multi-thousand-dollar daily ranges.
  - Source: Binance daily candles.
  - Why it matters causally: a 6% cushion is solid but not bulletproof over five days.
  - Direct/indirect: near-direct contextual.
  - Weight: high.
- Fear & Greed at 23 / Extreme Fear.
  - Source: Alternative.me in macro-calendar note.
  - Why it matters causally: suggests weak risk appetite and higher downside fragility if bad news hits.
  - Direct/indirect: indirect.
  - Weight: low-medium.

## Ambiguous or mixed evidence
- Absence of scheduled macro catalysts is supportive, but unscheduled catalysts dominate crypto tails.
- Current high spot level supports Yes, but also means a lot of optimism is already embedded.

## Conflict between inputs
There is little factual conflict. The real tension is weighting-based: current price regime argues strongly for Yes, while contract narrowness and BTC volatility argue that the market may still be somewhat overconfident.

## Key assumptions
- No unscheduled negative shock large enough to break $70k before noon ET April 20.
- Binance market functioning remains normal enough that the noon close reflects broad price conditions rather than a venue-specific disruption.

## Key uncertainties
- Weekend headline risk before Monday resolution.
- Whether a transient wick could matter more than broader BTC level.
- Whether sentiment fragility signals hidden downside convexity.

## Disconfirming signals to watch
- BTC trading back below $71k before April 19-20.
- Evidence of exchange stress or unusual Binance-specific dislocation.
- A fresh macro or regulatory shock that pushes crypto into a fast deleveraging move.

## What would increase confidence
- BTC holding above roughly $72k through the weekend.
- Continued absence of major negative catalysts.
- Stable Binance trading conditions with no venue-specific anomalies.

## Net update logic
I started near the market because spot is already comfortably above the threshold. I moved modestly below market confidence because the contract is narrower than a generic price call: a noon one-minute close on Binance can fail on volatility even if BTC is broadly strong. The lack of obvious scheduled catalysts keeps the lean on Yes, but not enough to justify full agreement with an 86%-87.5% price.

## Suggested downstream use
Use as orchestrator synthesis input and as an audit trail for why this persona agrees on direction but discounts market confidence due to timing and narrow settlement mechanics.
