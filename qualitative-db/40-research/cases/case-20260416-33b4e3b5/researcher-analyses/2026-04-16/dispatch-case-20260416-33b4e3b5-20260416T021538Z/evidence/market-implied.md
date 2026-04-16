---
type: evidence_map
case_key: case-20260416-33b4e3b5
dispatch_id: dispatch-case-20260416-33b4e3b5-20260416T021538Z
research_run_id: 424bd7fa-d01e-4cc7-93d0-1e4111ca84a9
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: tokens
entity: sol
topic: will-the-price-of-solana-be-above-80-on-april-19
question: "Will the price of Solana be above $80 on April 19?"
driver: reliability
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["sol", "solana"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-33b4e3b5/researcher-analyses/2026-04-16/dispatch-case-20260416-33b4e3b5-20260416T021538Z/personas/market-implied.md"]
tags: ["evidence-netting", "threshold-market", "short-horizon"]
---

# Summary

This evidence map nets the direct settlement mechanics against current price regime evidence for the April 19 SOL>$80 question.

## Question being evaluated

Will the Binance SOL/USDT 1-minute candle at 12:00 ET on April 19, 2026 have a final close above 80.00?

## Current lean

Lean Yes, with a high but not extreme-conviction probability.

## Prior / starting view

The starting view was the market-implied probability of 89.5%, which deserves respect because the threshold is below current spot and the market is usually efficient on simple crypto threshold contracts.

## Evidence supporting the claim

- Direct Binance spot price around 84.80 during research.
  - Source: `2026-04-16-market-implied-binance-solusdt-market-state.md`
  - Why it matters causally: current spot is materially above the threshold, so Yes does not require further appreciation.
  - Direct or indirect: direct market-state evidence.
  - Weight: high.

- Recent Binance daily closes mostly above 80, including multiple closes in the 83 to 86 range.
  - Source: `2026-04-16-market-implied-binance-solusdt-market-state.md`
  - Why it matters causally: suggests the current regime has sustained clearance above 80 rather than a one-off spike.
  - Direct or indirect: direct exchange evidence, but indirect for the exact settlement minute.
  - Weight: medium-high.

- Recent 1-hour Binance trading near the research time remained largely in the mid-84s to mid-85s.
  - Source: `2026-04-16-market-implied-binance-solusdt-market-state.md`
  - Why it matters causally: shows threshold distance is currently several dollars, reducing immediate knife-edge risk.
  - Direct or indirect: direct exchange evidence, indirect for the exact settlement minute.
  - Weight: medium.

- CoinGecko cross-check near 84.95.
  - Source: `2026-04-16-market-implied-coingecko-cross-check.md`
  - Why it matters causally: corroborates that Binance was not showing an obviously isolated price outlier.
  - Direct or indirect: contextual verification.
  - Weight: low-medium.

## Evidence against the claim

- Settlement depends on one exact 12:00 ET one-minute Binance close, not the broader day or week.
  - Source: market rules and Binance resolution-source logic in `2026-04-16-market-implied-binance-solusdt-market-state.md`
  - Why it matters causally: even if SOL spends most of the period above 80, a sharp move at or before noon ET could still settle No.
  - Direct or indirect: direct contract-mechanics evidence.
  - Weight: high.

- The current cushion over threshold is only about 4.8 to 5.0 dollars, which is meaningful but not huge for a three-day crypto horizon.
  - Source: same note.
  - Why it matters causally: crypto can traverse that distance on macro or idiosyncratic shocks.
  - Direct or indirect: inference from direct price evidence.
  - Weight: medium-high.

## Ambiguous or mixed evidence

- Recent trading above 80 is supportive, but it can also be over-read if volatility rises into the exact settlement window.
- Cross-venue corroboration is useful for freshness checking, but it does not reduce Binance-specific settlement dependence.

## Conflict between inputs

There is no major factual conflict between inputs. The main tension is weighting-based: whether recent price stability deserves something closer to 90% or a more conservative high-70s / low-80s estimate given single-minute settlement fragility.

## Key assumptions

- SOL remains broadly in its current trading regime through April 19 noon ET.
- No meaningful Binance-specific market-structure issue distorts the settlement candle.

## Key uncertainties

- How much short-horizon crypto volatility should be priced over the next roughly three days.
- Whether the noon ET timestamp adds meaningful event/timing fragility versus a generic daily close.

## Disconfirming signals to watch

- SOL trading back toward 82 and repeatedly failing to reclaim higher levels.
- A sharp crypto-wide risk-off move before the settlement day.
- Binance-specific disruption or unusual exchange divergence.

## What would increase confidence

- Continued Binance trading above 84 into April 18-19.
- Lower realized intraday volatility approaching the settlement window.

## Net update logic

The evidence supports a Yes lean because the threshold is below current spot and below most recent closes, so the market does not need to be pricing a rally. But the exact-one-minute settlement mechanic makes 89.5% feel a bit rich relative to a simple "current spot minus threshold" intuition. The main down-adjustment comes from respecting crypto short-horizon volatility and timestamp fragility rather than from any bearish fundamental thesis.

## Suggested downstream use

Use as orchestrator synthesis input and as an audit trail for why a market-respecting researcher can still shade slightly below the live market price without becoming outright contrarian.