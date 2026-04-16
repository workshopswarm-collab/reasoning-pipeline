---
type: evidence_map
case_key: case-20260414-3ae5a275
dispatch_id: dispatch-case-20260414-3ae5a275-20260414T202946Z
research_run_id: aba2b3ed-314f-4205-8682-609e33f2bd99
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-20
question: "Will the price of Bitcoin be above $70,000 on April 20?"
driver: reliability
date_created: 2026-04-14
agent: orchestrator
status: draft
confidence: medium
conflict_status: low-direct-conflict
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-3ae5a275/researcher-analyses/2026-04-14/dispatch-case-20260414-3ae5a275-20260414T202946Z/personas/market-implied.md"]
tags: ["evidence-map", "market-implied", "bitcoin"]
---

# Summary

The market’s 85.5% Yes price is directionally supported by current Binance spot and recent realized trading above the threshold, but the exact-minute settlement rule prevents treating current spot as near-certain proof.

## Question being evaluated

Whether Binance BTC/USDT will have a final 1-minute close above 70,000 at 12:00 ET on April 20, 2026.

## Current lean

Lean Yes, with high-but-not-extreme confidence.

## Prior / starting view

Starting from market prior: 85.5% Yes implied by current price.

## Evidence supporting the claim

- Binance spot ticker at run time was 74,258.65.
  - Source: Binance API source note.
  - Why it matters causally: settlement uses Binance BTC/USDT, so current venue-specific level matters directly.
  - Direct vs indirect: direct contextual evidence, not direct settlement evidence.
  - Weight: high.
- Recent Binance daily closes were mostly above 70,000 for more than a week.
  - Source: Binance API source note.
  - Why it matters causally: suggests persistence in the above-70k regime, not a one-off print.
  - Direct vs indirect: direct contextual evidence.
  - Weight: medium-high.
- Polymarket contract wording is narrow and explicit rather than ambiguous.
  - Source: contract/timing source note.
  - Why it matters causally: reduces interpretive uncertainty and supports focusing on threshold persistence.
  - Direct vs indirect: direct contract evidence.
  - Weight: high.

## Evidence against the claim

- The contract resolves on one exact minute, not daily close or general trading range.
  - Source: contract/timing source note.
  - Why it matters causally: exact-timestamp markets are more fragile than broad level markets.
  - Direct vs indirect: direct contract evidence.
  - Weight: high.
- Recent downside test on Binance reached about 70,505.88 on April 11.
  - Source: Binance API source note.
  - Why it matters causally: shows that even in the current regime, a drop of a few thousand dollars in days is plausible.
  - Direct vs indirect: direct contextual evidence.
  - Weight: medium-high.
- Crypto volatility can easily move several percent in under a week.
  - Source: inferred from recent Binance range plus general market structure.
  - Why it matters causally: a 5.7% gap from 74.26k to 70k is meaningful but not remotely unreachable for BTC.
  - Direct vs indirect: mixed/direct contextual.
  - Weight: medium.

## Ambiguous or mixed evidence

- Secondary cross-check from CoinGecko supports broad consistency with a high BTC regime, but adds limited independent causal information versus Binance.

## Conflict between inputs

There was no major factual conflict across checked sources. The main tension is weighting-based: how much current distance-from-strike should dominate versus exact-minute volatility risk.

## Key assumptions

- BTC remains in the current above-70k regime into April 20.
- No exchange-specific Binance anomaly dominates the settlement minute.

## Key uncertainties

- Exact noon-ET price path on April 20.
- Whether a broad risk-off move occurs between April 14 and April 20.

## Disconfirming signals to watch

- A daily close back below 72k.
- Repeated intraday tests near or below 70k.
- Exchange operational issues or unusual Binance-specific dislocation.

## What would increase confidence

- Additional days closing above 72k to 74k on Binance.
- A tighter independent cross-check preserving explicit price history closer to settlement.

## Net update logic

Starting from the market prior, the direct Binance data made the high Yes price look broadly reasonable rather than overextended. But the precise settlement minute and BTC’s demonstrated ability to retrace several thousand dollars kept the estimate below the market’s 85.5%.

## Suggested downstream use

Use as orchestrator synthesis input and as an audit trail showing why this run roughly agrees with, but slightly discounts, the market.