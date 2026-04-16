---
type: evidence_map
case_key: case-20260414-f6393095
dispatch_id: dispatch-case-20260414-f6393095-20260414T222237Z
research_run_id: 9b35b600-8057-4185-9660-1d306c860004
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-17
question: "Will the Binance BTC/USDT 12:00 ET one-minute candle close above 70000 on April 17, 2026?"
driver: operational-risk
date_created: 2026-04-14
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "bitcoin", "timing-risk"]
---

# Summary

This evidence map nets out a high-probability Yes view with explicit attention to timing and exchange-specific fragility.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for Apr. 17, 2026 at 12:00 ET close strictly above 70,000?

## Current lean

Lean Yes, but with less confidence than the market's 93.9% baseline because one-minute timing risk and crypto volatility still matter.

## Prior / starting view

Starting view: likely Yes because BTC is currently well above 70k, but extreme market confidence requires stress testing.

## Evidence supporting the claim

- Binance spot/ticker context around 74,066 with nearby 1-minute closes around 74,062 to 74,085.
  - Source: Binance source note.
  - Why it matters: direct distance from strike is about 4,000 points / 5.5%.
  - Direct or indirect: direct.
  - Weight: high.
- Binance 24h range roughly 73,795 to 76,038.
  - Source: Binance source note.
  - Why it matters: even recent downside stayed meaningfully above 70k.
  - Direct or indirect: direct contextual.
  - Weight: medium-high.
- CoinGecko and Coinbase cross-check also showed BTC around 74.1k.
  - Source: cross-exchange context note.
  - Why it matters: reduces concern that Binance alone is printing an anomalously high price.
  - Direct or indirect: indirect/contextual.
  - Weight: medium.

## Evidence against the claim

- The contract settles on one exact 12:00 ET one-minute Binance close, not an average daily level.
  - Source: Polymarket rules note.
  - Why it matters causally: a brief selloff or venue-specific dip at the wrong minute can flip the market.
  - Direct or indirect: direct contract interpretation.
  - Weight: high.
- BTC can move 5%+ over two days in risk-off conditions.
  - Source: inference from crypto volatility plus recent intraday range.
  - Why it matters causally: current cushion is large but not unbreakable.
  - Direct or indirect: indirect/contextual.
  - Weight: medium-high.
- Binance-specific operational or pricing idiosyncrasy matters more than broad market consensus because Binance BTC/USDT alone governs settlement.
  - Source: Polymarket rules note and Binance source note.
  - Why it matters causally: cross-exchange comfort cannot fully hedge exchange-specific resolution risk.
  - Direct or indirect: direct.
  - Weight: medium.

## Ambiguous or mixed evidence

- Cross-venue alignment is reassuring, but because only Binance BTC/USDT counts, it only partly reduces risk.
- Recent 24h range staying above 70k is supportive, but crypto volatility can expand quickly around macro or liquidation events.

## Conflict between inputs

There is no meaningful factual conflict across the checked sources. The main issue is weighting: how much confidence a 4k cushion deserves over a short but still volatile horizon.

## Key assumptions

- BTC does not suffer a roughly 5.5% drawdown into the exact settlement minute.
- Binance remains a usable and representative source at resolution time.
- No major exchange-specific dislocation opens between Binance and broader BTC references.

## Key uncertainties

- Short-horizon volatility between now and Apr. 17 noon ET.
- Event-driven downside shocks.
- Exact-minute path dependence.

## Disconfirming signals to watch

- BTC/USDT on Binance falling through 72k before Apr. 17.
- Rising cross-exchange divergence with Binance trading weak.
- Market structure deterioration causing sharp downside wicks around noon ET.

## What would increase confidence

- BTC holding above 73k into late Apr. 16 / early Apr. 17.
- Continued tight alignment between Binance and other large venues.
- Lower realized volatility into the resolution window.

## Net update logic

The direct exchange data keeps the case solidly in Yes territory, but the contract wording and exact-minute settlement push against treating 93.9% as near-certain. The evidence supports trimming confidence somewhat rather than flipping direction.

## Suggested downstream use

- orchestrator synthesis input
- forecast update
- decision-maker review