---
type: evidence_map
case_key: case-20260415-0c8ac7fd
dispatch_id: dispatch-case-20260415-0c8ac7fd-20260415T190844Z
research_run_id: 4f5c0429-380f-4d57-9a0d-33d2e9379c67
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: btc-threshold-close
entity: bitcoin
topic: noon-et-close-above-threshold-risk-netting
question: "Will the price of Bitcoin be above $72,000 on April 17?"
driver: operational-risk
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["binance", "bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-source-notes/2026-04-15-risk-manager-binance-polymarket-resolution-context.md", "qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-analyses/2026-04-15/dispatch-case-20260415-0c8ac7fd-20260415T190844Z/assumptions/risk-manager.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-analyses/2026-04-15/dispatch-case-20260415-0c8ac7fd-20260415T190844Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "close-market", "polymarket"]
---

# Summary

Net evidence favors **Yes**, but with a meaningful warning that this is a **precise-timestamp Binance close** market and not a touch market.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for **12:00 ET on 2026-04-17** have a final close above **72,000**?

## Current lean

Lean **Yes**.

## Prior / starting view

Starting view was that a high-80s market price might be a little rich unless current BTC levels were comfortably above the threshold and the rules clearly confirmed this was a close market rather than some broader average.

## Evidence supporting the claim

- **Current Binance BTCUSDT context is materially above threshold**
  - Source: source note on Binance 1m klines.
  - Why it matters: current closes near 74.6k-74.7k leave about a 3.7% cushion.
  - Directness: indirect for settlement, direct for current state.
  - Weight: high.

- **Market ladder coherence**
  - Source: Polymarket event surface showing 72k around 87-88% while 74k is around upper-50s.
  - Why it matters: internal ladder shape is broadly consistent with spot around 74.7k and suggests the 72k line is safely in-the-money but not locked.
  - Directness: contextual.
  - Weight: medium.

- **Mechanics are simple and specific**
  - Source: Polymarket rules.
  - Why it matters: fewer interpretive branches than a vague macro market; no need to infer from multiple venues.
  - Directness: direct on contract interpretation.
  - Weight: medium.

## Evidence against the claim

- **Single-minute close risk remains real**
  - Source: Polymarket rules / source note.
  - Why it matters: the market can resolve No even if BTC spends most of the next two days above 72k, so long as the exact Binance 12:00 ET close prints below.
  - Directness: direct on mechanism.
  - Weight: high.

- **Event has not yet occurred**
  - Source: timing facts.
  - Why it matters: current spot evidence is not settlement proof.
  - Directness: direct.
  - Weight: high.

- **Binance-specific surface matters**
  - Source: Polymarket rules.
  - Why it matters: cross-venue strength does not settle the contract if Binance diverges at the resolving minute.
  - Directness: direct.
  - Weight: medium.

## Ambiguous or mixed evidence

- The market price itself can be read two ways: informed crowd wisdom or overconfidence induced by current spot being comfortably above threshold.
- Recent BTC strength supports Yes but also means downside could be driven by short-horizon volatility rather than a deep thesis reversal.

## Conflict between inputs

There is no major factual conflict. The main disagreement is weighting-based: how much discount should remain for timestamp-specific and venue-specific risk when spot is already well above the threshold.

## Key assumptions

- BTC retains enough cushion into noon ET on Apr 17.
- No material Binance-specific dislocation undermines the broader bullish spot picture.

## Key uncertainties

- Short-horizon BTC volatility into the exact resolving minute.
- Whether macro/news flow creates a sharp selloff before noon ET on Apr 17.
- Whether Binance price action specifically underperforms broader spot at settlement.

## Disconfirming signals to watch

- BTC trading back toward 72k before the settlement window.
- Late-morning ET weakness on Apr 17.
- Any Binance-specific operational or pricing anomaly.

## What would increase confidence

- Continued Binance closes above mid-74k into Apr 16-17.
- A fresh verification pass close to settlement showing Binance still comfortably above 72k.

## Net update logic

The evidence moved the view toward **Yes** because current Binance spot is not marginally but materially above 72k, and the contract mechanics are clear. However, the exact resolving minute and exchange-specific close requirement prevent a near-certainty conclusion.

## Suggested downstream use

Use as forecast-update input and synthesis input, with explicit emphasis that the biggest underpriced risk is **timing/venue precision**, not a broad bearish BTC thesis.