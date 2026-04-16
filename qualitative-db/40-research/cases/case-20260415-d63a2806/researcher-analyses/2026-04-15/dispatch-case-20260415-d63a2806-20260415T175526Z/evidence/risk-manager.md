---
type: evidence_map
case_key: case-20260415-d63a2806
dispatch_id: dispatch-case-20260415-d63a2806-20260415T175526Z
research_run_id: fb9863c0-2f1f-4188-8b6c-875f7445bbb6
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin-threshold-close
entity: bitcoin
topic: "Netting support vs fragility for BTC > 72000 at Binance noon ET close on April 17"
question: "Will the Binance BTC/USDT 1 minute candle for 12:00 ET on April 17, 2026 close above 72000?"
driver: operational-risk
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-d63a2806/researcher-source-notes/2026-04-15-risk-manager-polymarket-rules.md", "qualitative-db/40-research/cases/case-20260415-d63a2806/researcher-source-notes/2026-04-15-risk-manager-binance-price-context.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-d63a2806/researcher-analyses/2026-04-15/dispatch-case-20260415-d63a2806-20260415T175526Z/personas/risk-manager.md"]
tags: ["evidence-map", "bitcoin", "polymarket", "binance", "timing-risk"]
---

# Summary

Evidence nets to a Yes lean, but the main underappreciated risk is not directional thesis failure; it is timestamp-specific close risk on a single governing venue.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle corresponding to 12:00 ET on April 17, 2026 have a final close above 72,000?

## Current lean

Lean Yes, but with lower confidence than the market price suggests.

## Prior / starting view

Starting baseline from the market was about 83% Yes.

## Evidence supporting the claim

- Current Binance BTC/USDT spot around 74,121.29.
  - Source: Binance ticker API source note.
  - Why it matters: gives nearly 3% cushion above the threshold.
  - Direct or indirect: direct contextual evidence from the governing venue/pair.
  - Weight: high.
- Multiple recent Binance daily closes above 72,000.
  - Source: Binance kline API source note.
  - Why it matters: shows BTC is not merely spiking above the line; it has recently sustained closes over it.
  - Direct or indirect: direct contextual evidence from the governing venue/pair.
  - Weight: medium-high.
- Contract is close-above 72,000, not new-high dependent.
  - Source: Polymarket rules note.
  - Why it matters: the threshold is below current spot, so the event only needs maintenance rather than breakout continuation.
  - Direct or indirect: direct contract interpretation.
  - Weight: high.

## Evidence against the claim

- The market resolves on one exact one-minute close at one exact timestamp.
  - Source: Polymarket rules note.
  - Why it matters causally: even a temporary dip into the high-71k range at the wrong minute is enough to resolve No.
  - Direct or indirect: direct contract interpretation.
  - Weight: high.
- Recent Binance daily range has been wide enough to include sub-72k territory.
  - Source: Binance kline API source note.
  - Why it matters causally: ordinary BTC volatility over 24-48 hours is large enough to erase the current cushion.
  - Direct or indirect: direct contextual evidence.
  - Weight: medium-high.
- Current evidence is still pre-event and not the governing candle itself.
  - Source: both source notes.
  - Why it matters causally: the main thesis could fail without any contradiction in current bullish context.
  - Direct or indirect: methodological / timing constraint.
  - Weight: medium.

## Ambiguous or mixed evidence

- Market price around 83% could reflect informed traders correctly valuing the current 2.9% cushion, or it could reflect overconfidence carried over from broader bullish BTC sentiment rather than the narrow timestamp mechanics.

## Conflict between inputs

- No major factual conflict.
- Main difference is weighting-based: whether the current spot buffer should dominate, or whether single-minute timing risk should be discounted less aggressively.
- Evidence that would resolve this best would be additional high-frequency volatility context closer to the event or explicit BTC path deterioration before April 17.

## Key assumptions

- BTC remains above 72,000 through the target minute despite normal volatility.
- Binance BTC/USDT remains representative enough that exchange-specific deviation risk is small.

## Key uncertainties

- Magnitude of BTC volatility over the next ~43 hours.
- Whether noon ET prints are especially vulnerable to short-lived retracements.
- Whether broad bullish context is already sufficiently priced into the 83% market.

## Disconfirming signals to watch

- Sustained loss of 73,000 support on Binance.
- Repeated pushes lower into April 16-17 with weakening closes.
- A sharp risk-off move that returns BTC to the low 71k range.

## What would increase confidence

- BTC holding above 73,500-74,000 into late April 16 and early April 17.
- Additional Binance intraday evidence showing stable support above 72,000 during U.S. morning trading.
- Reduced realized volatility approaching the target minute.

## Net update logic

The market starts from a sensible bullish base because spot is already above the threshold on the governing venue. The reason to price below the market is not bearish conviction on BTC broadly; it is the recognition that a single-minute close contract is fragile to even modest retracement. That timing fragility matters more than it would in a weekly touch market.

## Suggested downstream use

Use as orchestrator synthesis input and as a guardrail against treating this as a simple trend-following Yes. The case is mostly about maintenance risk and timestamp mechanics.
