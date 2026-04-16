---
type: evidence_map
case_key: case-20260415-540d9abf
dispatch_id: dispatch-case-20260415-540d9abf-20260415T234706Z
research_run_id: 27910ae0-c812-48f3-b288-9374e12ff432
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: solana
entity: sol
topic: solana-above-80-on-april-19
question: "Will the Binance SOL/USDT 12:00 ET one-minute candle close above 80 on April 19, 2026?"
driver: reliability
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["sol"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-540d9abf/researcher-analyses/2026-04-15/dispatch-case-20260415-540d9abf-20260415T234706Z/personas/market-implied.md"]
tags: ["evidence-map", "market-vs-own-view", "binance"]
---

# Summary

Evidence nets to a bullish lean for Yes, with the market likely directionally right but somewhat overconfident relative to a still-volatile multi-day crypto horizon.

## Question being evaluated

Whether Binance SOL/USDT will print a final one-minute candle close above 80 at 12:00 ET on Apr 19, 2026.

## Current lean

Lean Yes.

## Prior / starting view

Start from the live market prior around 90% because the strike is below current spot and the market may be efficiently aggregating simple distance-to-strike information.

## Evidence supporting the claim

- Binance spot around 84.86-84.87.
  - Source: Binance ticker endpoints.
  - Why it matters causally: current price is already about 6% above strike.
  - Direct or indirect: direct for current price, indirect for Apr 19 noon outcome.
  - Weight: high.

- Binance 24h low around 82.65, still above strike.
  - Source: Binance 24hr endpoint.
  - Why it matters causally: recent realized downside has not threatened 80.
  - Direct or indirect: indirect.
  - Weight: medium-high.

- Recent daily closes in fetched sample all above 80.
  - Source: Binance daily klines.
  - Why it matters causally: recent regime is already above strike, so Yes does not require a fresh breakout.
  - Direct or indirect: indirect.
  - Weight: medium.

- Polymarket rules define a narrow Binance-specific settlement, reducing cross-exchange ambiguity.
  - Source: Polymarket market page.
  - Why it matters causally: clarifies that only Binance SOL/USDT noon ET 1m close matters.
  - Direct or indirect: direct for contract interpretation.
  - Weight: high for mechanics, neutral-to-supportive for direction.

## Evidence against the claim

- The market resolves several days after analysis, and crypto can move more than 6% in that window.
  - Source: general interpretation from recent volatility plus crypto market behavior.
  - Why it matters causally: current cushion is meaningful but not huge.
  - Direct or indirect: indirect.
  - Weight: high.

- Contract depends on a single one-minute close at a specific timestamp.
  - Source: Polymarket rules.
  - Why it matters causally: even if SOL trades above 80 generally, a brief dip at noon ET could still resolve No.
  - Direct or indirect: direct for mechanics.
  - Weight: medium-high.

- Binance-specific print risk remains, even if small.
  - Source: contract wording plus exchange dependence.
  - Why it matters causally: market is not based on a broader index.
  - Direct or indirect: direct for mechanics.
  - Weight: low-medium.

## Ambiguous or mixed evidence

- Web fetch for the Binance webpage itself did not cleanly extract readable content, so API endpoints served as the verification surface instead.
- The Polymarket page showed extreme probabilities across many strikes, which is consistent with current price levels but also reminds us these ladder markets can become mechanically one-sided.

## Conflict between inputs

No major factual conflict. The main disagreement is weighting-based: whether the current spot cushion and recent range justify something as high as 90% over a multi-day horizon.

## Key assumptions

- Current spot-to-strike cushion remains mostly intact into Apr 19 noon ET.
- No major SOL-specific or crypto-wide downside shock occurs.
- Binance API and settlement surface remain consistent with the described market rules.

## Key uncertainties

- Multi-day crypto volatility between now and Apr 19.
- Exact ET-to-Binance timestamp mapping for the final settlement candle, though the market wording is clear enough for practical interpretation.
- Whether the market is incorporating additional tacit information not visible here.

## Disconfirming signals to watch

- SOLUSDT revisiting or breaking below 80 before Apr 19.
- Significant risk-off move in majors/alts.
- Binance-specific operational or pricing anomalies near settlement time.

## What would increase confidence

- Continued Binance trading above roughly 82-83 into Apr 18-19.
- Evidence that noon ET candles do not show unusual transient downside behavior.
- Confirmation from an additional Binance documentation source on kline timestamp interpretation.

## Net update logic

The evidence mostly supports the market's direction: SOL is already above the strike and recent Binance trading has not challenged 80. The main reason not to fully endorse the 90% price is that the contract is still a single-minute print several days out in a volatile asset, so tail downside is not trivial.

## Suggested downstream use

Use as forecast update and orchestrator synthesis input, mainly to argue that any contrarian No case needs stronger evidence than simple hand-waving about crypto volatility.