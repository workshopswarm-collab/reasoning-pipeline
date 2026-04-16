---
type: evidence_map
case_key: case-20260415-0c8ac7fd
dispatch_id: dispatch-case-20260415-0c8ac7fd-20260415T190844Z
research_run_id: 203d3f16-4f99-4c4c-8c8c-8a55fc1f3750
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin-threshold-close
entity: bitcoin
topic: "evidence netting for BTC above 72k on Apr 17 noon ET"
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle on Apr 17 close above 72000?"
driver: operational-risk
date_created: 2026-04-15
agent: market-implied
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["binance", "bitcoin"]
related_drivers: ["operational-risk"]
proposed_entities: []
proposed_drivers: ["threshold-close mechanics"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-source-notes/2026-04-15-market-implied-binance-btcusdt-price-and-1m-klines.md", "qualitative-db/50-learnings/case-reviews/case-20260414-4e668883/review.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-analyses/2026-04-15/dispatch-case-20260415-0c8ac7fd-20260415T190844Z/personas/market-implied.md"]
tags: ["evidence-map", "bitcoin", "market-implied", "threshold-close"]
---

# Summary

Evidence supports a high Yes probability because BTC is already comfortably above the strike on the governing source family, but the contract is a specific-minute close market, so it is less forgiving than a touch/high market and should not be pushed to near-certainty yet.

## Question being evaluated

Will Binance BTC/USDT close above 72,000 on the 1-minute candle corresponding to Apr 17 12:00 ET?

## Current lean

Lean Yes, high confidence relative to ordinary markets but still short of certainty.

## Prior / starting view

Start from the market-implied 0.87 Yes price as an information-rich prior.

## Evidence supporting the claim

- Direct Binance spot check near 74.65k.
  - Source: source note on Binance API.
  - Why it matters: current spot is already about 3.7% above the strike.
  - Directness: direct.
  - Weight: high.

- Recent Binance 1-minute closes clustered around mid-74.6k.
  - Source: source note on Binance API klines.
  - Why it matters: recent minute-level behavior is far above 72k and normal minute noise is small relative to cushion.
  - Directness: direct.
  - Weight: medium-high.

- Polymarket rules explicitly specify Binance BTC/USDT 1-minute close at 12:00 ET.
  - Source: Polymarket market page.
  - Why it matters: narrows mechanism and reduces ambiguity about exchange and field.
  - Directness: direct contract evidence.
  - Weight: high.

## Evidence against the claim

- This is a close-above market at one exact minute, not a touch/high market.
  - Source: Polymarket rules.
  - Why it matters: a temporary earlier trade above 72k is irrelevant if BTC sells off into the exact resolving minute.
  - Directness: direct contract evidence.
  - Weight: high.

- BTC can move several percent in two days.
  - Source: general market behavior inferred from asset class; not directly quantified in this run.
  - Why it matters: the current 3.7% cushion is meaningful but not invulnerable.
  - Directness: contextual.
  - Weight: medium.

- Exact governing surface remains slightly ambiguous because the rules reference the Binance trading UI with 1m candles selected, while this run verified Binance API endpoints from the same source family rather than the exact final UI state at resolution.
  - Source: source note + Polymarket rules.
  - Why it matters: small operational ambiguity remains until the actual resolving minute.
  - Directness: mixed.
  - Weight: low-medium.

## Ambiguous or mixed evidence

- The market may already price current spot cushion efficiently, leaving little edge.
- Absence of a bearish catalyst in this run is not strong evidence by itself; crypto can still sell off abruptly.

## Conflict between inputs

No major factual conflict. The main tension is weighting-based: whether a 3.7% cushion with ~2 days remaining is enough to justify 87% versus something modestly lower because of exact-minute-close risk.

## Key assumptions

- Current cushion to strike is materially informative.
- No major selloff or exchange-specific dislocation occurs before Apr 17 noon ET.
- The Binance API data is a valid near-governing verification pass for current state even though final settlement references the trading surface.

## Key uncertainties

- BTC path over the next ~2 days.
- Whether any macro or crypto-specific volatility event arrives before resolution.
- Exact operational mapping of the 12:00 ET candle on the final UI surface.

## Disconfirming signals to watch

- Binance BTC/USDT trading persistently near or below 72k on Apr 16-17.
- Sudden downside momentum or liquidation cascade.
- Any sign of resolution-surface mismatch.

## What would increase confidence

- Another direct Binance check closer to Apr 17 noon ET showing BTC still well above 72k.
- Stronger direct confirmation of the exact candle/time mapping on the Binance interface.

## Net update logic

The market’s 0.87 prior survives scrutiny. Direct governing-source-family data shows BTC already above the strike by a meaningful margin, which is the main support for Yes. But because the market resolves on one exact 1-minute close rather than a touch, I do not upgrade to near-certainty.

## Suggested downstream use

Use as synthesis input and as audit support for why this persona roughly agrees with the market while keeping a small discount for exact-close and operational-surface risk.