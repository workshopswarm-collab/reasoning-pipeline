---
type: evidence_map
case_key: case-20260416-63fb3082
dispatch_id: dispatch-case-20260416-63fb3082-20260416T145628Z
research_run_id: e0f959a1-35b0-43f4-b819-54ad318b66a4
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-68-000-on-april-21
question: "Will the price of Bitcoin be above $68,000 on April 21?"
driver: reliability
date_created: 2026-04-16
agent: market-implied
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-63fb3082/researcher-analyses/2026-04-16/dispatch-case-20260416-63fb3082-20260416T145628Z/personas/market-implied.md"]
tags: ["evidence-map", "bitcoin", "threshold-market"]
---

# Summary

The evidence nets to a high-Yes lean with modest skepticism about whether 95% is a touch too rich for a five-day crypto price threshold market.

## Question being evaluated

Will Binance BTC/USDT’s 1-minute candle for 12:00 ET on April 21, 2026 close above 68,000?

## Current lean

Lean Yes, high probability but not quite as high as the live market.

## Prior / starting view

Starting prior was the live market at roughly 95% Yes.

## Evidence supporting the claim

- Binance direct spot and recent 1-minute klines around 73.9k.
  - Source: `2026-04-16-market-implied-binance-spot-and-exchange-metadata.md`
  - Why it matters causally: current distance to barrier is about 8%, meaning BTC can fall materially and still settle Yes.
  - Direct or indirect: direct to instrument and venue.
  - Weight: high.

- Polymarket neighboring strikes show a coherent local distribution.
  - Source: `2026-04-16-market-implied-polymarket-rules-and-market-state.md`
  - Why it matters causally: 70k ~88%, 72k ~71%, 74k ~48% makes 68k ~95% directionally consistent rather than isolated.
  - Direct or indirect: direct to market pricing, indirect to fundamental truth.
  - Weight: medium-high.

- Secondary quote check from CNBC near 73.9k.
  - Source: `2026-04-16-market-implied-cnbc-context-price-check.md`
  - Why it matters causally: reduces risk that the Binance read is stale or aberrant.
  - Direct or indirect: indirect/contextual.
  - Weight: low-medium.

## Evidence against the claim

- The contract settles on one exact minute close at a fixed time, not on average price or intraday range.
  - Why it matters causally: single-minute, date-specific contracts can fail on short-lived weakness even if the broader trend remains bullish.
  - Direct or indirect: direct to contract mechanics.
  - Weight: medium.

- Bitcoin is a volatile asset and five days is enough time for an 8% drawdown.
  - Why it matters causally: the present cushion is meaningful but not overwhelming in crypto terms.
  - Direct or indirect: indirect/contextual.
  - Weight: medium.

## Ambiguous or mixed evidence

- Exchange-specific operational or data issues on Binance seem low probability but matter more than usual because Binance is explicitly the sole source of truth.
- Cross-venue price checks support the general level but do not perfectly map to Binance BTC/USDT settlement.

## Conflict between inputs

No major factual conflict. The main disagreement is interpretive: whether the current cushion and ladder coherence justify something as high as 95%, or whether that is slightly overconfident for a five-day BTC threshold contract.

## Key assumptions

- Current BTC spot level remains the dominant predictor over the next five days.
- No major macro or crypto-specific shock occurs before April 21 noon ET.
- Binance remains a reliable settlement source with no meaningful anomaly at the settlement minute.

## Key uncertainties

- Near-term BTC volatility regime over the next five days.
- Any catalyst capable of pushing BTC below 68k before the settlement minute.
- Whether market participants may be slightly underpricing single-minute close risk.

## Disconfirming signals to watch

- BTC quickly trading below 72k, shrinking the cushion.
- Broad risk-off move in crypto or macro assets.
- Binance operational or market-structure irregularity around the event window.

## What would increase confidence

- BTC holding or expanding above 74k into the weekend.
- Continued coherence across Binance and secondary market quotes.
- No new adverse catalyst for crypto risk sentiment.

## Net update logic

The main update is that the market’s high Yes price looks understandable because the threshold is materially below spot and the strike ladder is internally coherent. The remaining discount from 95% to a slightly lower personal estimate comes from contract structure: one precise minute close on a volatile asset still leaves meaningful tail risk.

## Suggested downstream use

Use as synthesis input and as audit support for why the market-implied persona stayed broadly with the market instead of forcing a contrarian take.