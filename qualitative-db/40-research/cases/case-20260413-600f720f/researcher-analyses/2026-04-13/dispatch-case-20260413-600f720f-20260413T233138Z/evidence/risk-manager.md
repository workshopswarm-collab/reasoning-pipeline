---
type: evidence_map
case_key: case-20260413-600f720f
dispatch_id: dispatch-case-20260413-600f720f-20260413T233138Z
research_run_id: 515387fd-76f8-4191-a227-9e7d882e6bb4
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: markets
entity: bitcoin
topic: will-bitcoin-reach-76k-april-13-19
question: "Will Bitcoin reach $76,000 April 13-19?"
date_created: 2026-04-13
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["short-horizon-crypto-path-risk"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-600f720f/researcher-analyses/2026-04-13/dispatch-case-20260413-600f720f-20260413T233138Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "path-risk"]
driver:
---

# Summary

This case is mostly about path and timing risk rather than deep fundamental disagreement. The evidence leans Yes, but the key question is whether the market is pricing too much confidence into a still-unmet threshold.

## Question being evaluated

Will Bitcoin print at least one Binance BTC/USDT 1-minute candle high at or above $76,000 between 12:00 AM ET on Apr 13, 2026 and 11:59 PM ET on Apr 19, 2026?

## Current lean

Lean Yes, but slightly less confidently than market pricing.

## Prior / starting view

Starting view was that a nearly full week and a touch-based contract should favor Yes if BTC begins close to the threshold.

## Evidence supporting the claim

- Polymarket contract terms only require a **1-minute Binance high**, not a close or cross-exchange confirmation.
  - Source: `2026-04-13-risk-manager-polymarket-market-terms.md`
  - Why it matters: lowers the mechanical bar to resolution.
  - Direct vs indirect: direct.
  - Weight: high.

- Binance BTCUSDT spot snapshot around **$74,815.78**, with Coinbase spot near the same level.
  - Source: `2026-04-13-risk-manager-btc-price-context.md`
  - Why it matters: target is only about **1.6%** away, which is very reachable for BTC over a week.
  - Direct vs indirect: direct for current distance, indirect for future hit probability.
  - Weight: high.

- Nearly full week remains in the contract window.
  - Source: Polymarket contract metadata and case dates.
  - Why it matters: multiple trading sessions increase odds of at least one probe higher.
  - Direct vs indirect: direct.
  - Weight: medium.

## Evidence against the claim

- BTC had **not** yet reached the threshold at observation; the market is pricing a future path event, not an already-achieved result.
  - Source: Binance/Coinbase snapshot note.
  - Why it matters: timing failure remains very live.
  - Direct vs indirect: direct.
  - Weight: high.

- Market price around **0.74-0.75** may embed stronger confidence than the available evidence warrants.
  - Source: Polymarket market terms note plus external price snapshot.
  - Why it matters: current evidence mostly supports plausibility, not inevitability.
  - Direct vs indirect: interpretive.
  - Weight: medium.

- No additional volatility, momentum, or catalyst evidence was collected that would clearly justify treating a 1.6% move as highly likely rather than just reasonably likely.
  - Source: evidence set limitation.
  - Why it matters: thin evidence can make the market look more precise than justified.
  - Direct vs indirect: indirect.
  - Weight: medium.

## Ambiguous or mixed evidence

- Cross-exchange spot consistency is reassuring, but it does not itself say whether Binance will print a qualifying high later.
- The touch-based structure helps Yes, but also means a short-lived rejection just below $76k still resolves No.

## Conflict between inputs

No major factual conflict. The disagreement is mainly weighting-based: how much confidence should be assigned to a reachable but still unachieved threshold.

## Key assumptions

- Short-horizon BTC volatility remains sufficient to generate at least one upside probe.
- No major negative shock prevents BTC from testing the upper 75k/76k area this week.

## Key uncertainties

- Near-term realized volatility.
- Whether BTC trend/momentum is strengthening or stalling just below the threshold.
- Whether a late-week drawdown could close the window before a touch occurs.

## Disconfirming signals to watch

- BTC loses the mid-$74k area and spends time materially lower.
- Repeated failures near ~$75k without extension.
- A broad crypto or macro risk-off move early in the week.

## What would increase confidence

- Evidence of an early-week Binance print above recent highs.
- Stronger momentum evidence or fresh catalyst flow.
- Updated Binance candle/high data showing the market is already probing close to $76k.

## Net update logic

The contract mechanics and the small required move push the base case toward Yes. The main reason not to simply endorse the market is that the evidence set proves reachability, not inevitability. That is enough for a moderate-to-high probability but not enough for very high confidence.

## Suggested downstream use

Use as synthesis input for a modestly cautious stance: likely Yes, but treat market confidence as slightly rich unless later evidence shows strengthening upside momentum.