---
type: evidence_map
case_key: case-20260415-9c95ce3a
dispatch_id: dispatch-case-20260415-9c95ce3a-20260415T173129Z
research_run_id: c5bd52bd-355b-4d95-8916-04e3c4df69f6
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-binance-btc-usdt-12-00-et-1-minute-candle-close-on-2026-04-17-be-above-72000
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-17 be above 72000?"
driver: reliability
date_created: 2026-04-15
agent: market-implied
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: ["binance-btcusdt-market"]
proposed_drivers: ["resolution-window-fragility"]
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "market-implied", "crypto"]
---

# Summary

Evidence nets to a clear Yes lean, but with some downweighting versus the live market because the contract resolves on one narrow minute rather than a daily level.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-17 above 72,000?

## Current lean

Yes, with probability around the high-70s.

## Prior / starting view

Starting from the market prior, the natural baseline was about 82-83% Yes.

## Evidence supporting the claim

- **Binance spot around 74,156 on the resolving venue**  
  - Source: Binance ticker / kline source note  
  - Why it matters: gives a >2.1k cushion over the threshold on the exact venue used for settlement  
  - Direct vs indirect: direct contextual evidence  
  - Weight: high

- **Recent 1-minute closes clustered around 74.1k**  
  - Source: Binance ticker / kline source note  
  - Why it matters: shows the market is not merely barely above threshold at check time  
  - Direct vs indirect: direct contextual evidence  
  - Weight: medium-high

- **Recent daily Binance closes mostly above 72k**  
  - Source: Binance ticker / kline source note  
  - Why it matters: places 72k inside the recent trading regime  
  - Direct vs indirect: indirect/contextual  
  - Weight: medium

- **Smooth Polymarket strike ladder**  
  - Source: Polymarket rules / pricing source note  
  - Why it matters: suggests the crowd is pricing a plausible distribution centered near 74k, not mispricing one isolated strike  
  - Direct vs indirect: indirect but highly relevant for market-efficiency interpretation  
  - Weight: medium-high

## Evidence against the claim

- **A 2k+ move is not large for BTC over ~43 hours**  
  - Source: inference from current cushion and crypto volatility  
  - Why it matters: downside path to No does not require an extreme event  
  - Direct vs indirect: indirect  
  - Weight: high

- **Single-minute resolution risk**  
  - Source: Polymarket contract wording  
  - Why it matters: even a temporary dip at the wrong minute can settle No despite broader strength  
  - Direct vs indirect: direct contract-interpretation evidence  
  - Weight: high

## Ambiguous or mixed evidence

- CoinGecko confirmed broadly similar spot levels, which is reassuring, but because settlement is Binance-specific it adds only limited independent value.

## Conflict between inputs

There is little factual conflict. The main disagreement is weighting-based: how much confidence should be assigned to today's >2k cushion over a threshold that will be checked at one precise minute nearly two days later?

## Key assumptions

- Current Binance spot remains a decent anchor for the April 17 noon distribution.
- No fresh catalyst causes a rapid downside repricing.
- Binance operational reliability stays sufficient for clean settlement interpretation.

## Key uncertainties

- Short-horizon BTC volatility into the resolving window.
- Whether a macro or crypto-specific headline emerges before Friday noon ET.
- Whether the crowd's confidence is slightly overstating precision for a narrow-minute event.

## Disconfirming signals to watch

- Sustained Binance trading below 73k.
- Sudden broad crypto selloff or macro risk-off shock.
- Venue-specific anomalies around Binance pricing or candle integrity.

## What would increase confidence

- BTC holding 74k+ on Binance into late April 16 / early April 17.
- Continued coherence of nearby strike prices without abrupt bearish repricing.

## Net update logic

The evidence did not overthrow the market prior; it largely validated it. The adjustment came from contract structure rather than contrary facts: a narrow one-minute resolving condition deserves slightly more downside allowance than the raw current spot cushion alone might imply.

## Suggested downstream use

Use as orchestrator synthesis input emphasizing that the market appears broadly efficient, with the main caveat being single-window timing risk rather than a clear informational miss.