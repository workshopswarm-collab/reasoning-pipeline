---
type: evidence_map
case_key: case-20260415-90641eba
dispatch_id: dispatch-case-20260415-90641eba-20260415T174326Z
research_run_id: 222526d8-e959-4e3a-9ba7-eb5ec3f17f0e
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: "Netting current price buffer versus date-specific noon-close risk"
question: "Will the Binance BTC/USDT 12:00 PM ET one-minute candle close on April 20 above $70,000?"
driver: operational-risk
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: ["threshold proximity"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-90641eba/researcher-source-notes/2026-04-15-catalyst-hunter-binance-polymarket-resolution-surface.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-90641eba/researcher-analyses/2026-04-15/dispatch-case-20260415-90641eba-20260415T174326Z/personas/catalyst-hunter.md"]
tags: ["evidence-map", "btc", "close-market", "settlement"]
---

# Summary

The net evidence favors Yes because BTC is already materially above the threshold and the contract only requires persistence to one exact future minute close, but the decisive risk is that the market is a narrow close-style contract rather than a permissive touch market.

## Question being evaluated

Will the Binance BTC/USDT one-minute candle that closes at 12:00 PM ET on 2026-04-20 print above $70,000?

## Current lean

Lean Yes, high but not extreme confidence.

## Prior / starting view

Starting prior was that 0.87 market-implied probability looked plausible but needed a direct rules/mechanics check because the contract is date-specific and source-sensitive.

## Evidence supporting the claim

- **Direct governing rules check confirms a close-above test on Binance BTCUSDT only.**
  - Source: Polymarket market page.
  - Why it matters: removes ambiguity about venue, pair, timing, and condition.
  - Type: direct.
  - Weight: high.

- **Current Binance BTCUSDT price is about 73,989, nearly 3,989 above the threshold.**
  - Source: direct Binance API spot/ticker check.
  - Why it matters: current state is comfortably above the line.
  - Type: direct contextual-to-state, not direct settlement proof.
  - Weight: high.

- **Recent Binance daily candles show sustained trading above 70k with recent highs up to 76,038.**
  - Source: direct Binance API daily klines.
  - Why it matters: supports the view that BTC is not merely flickering around the line; it currently has a real cushion.
  - Type: direct contextual.
  - Weight: medium-high.

## Evidence against the claim

- **The contract is about one exact minute close at noon ET on April 20, not today's price and not an intraday touch.**
  - Source: Polymarket rules.
  - Why it matters: close-only mechanics are stricter than touch-style mechanics and make timing more fragile.
  - Type: direct.
  - Weight: high.

- **Five days is long enough for a macro or crypto-specific drawdown larger than the current cushion.**
  - Source: market structure logic plus ordinary BTC volatility.
  - Why it matters: a ~5.7% cushion is meaningful but not invulnerable in BTC.
  - Type: indirect/contextual.
  - Weight: medium.

- **Binance-specific operational or pricing anomalies near resolution could matter because Binance is the governing source.**
  - Source: contract mechanics and exchange-specific settlement dependence.
  - Why it matters: this is a source-sensitive market, so venue-specific issues are not fully diversifiable away.
  - Type: indirect/contextual.
  - Weight: low-medium.

## Ambiguous or mixed evidence

- No single obvious scheduled upside catalyst appears necessary for Yes. That is mildly bearish from a catalyst-hunter perspective, but in practice it can also mean the current state already does most of the work.
- Third-party price sites are directionally consistent with BTC trading in the mid-70k area, but they are not the governing source.

## Conflict between inputs

No major factual conflict. The main disagreement is weighting-based: how much probability discount should be applied for five days of remaining BTC volatility in a close-only market.

## Key assumptions

- BTC remains comfortably above 70k into the final settlement window.
- No major risk-off catalyst emerges before April 20 noon ET.
- Binance remains a usable resolution surface.

## Key uncertainties

- Whether a macro headline or crypto liquidation event creates a fast 5%+ drawdown before the decisive minute.
- Whether the noon ET timestamp lines up with a vulnerable intraday window for BTC on April 20.

## Disconfirming signals to watch

- BTC loses 72k and then 71k before the weekend.
- Signs of macro stress or exchange-specific instability.
- A rapid repricing in adjacent Polymarket BTC close markets toward lower thresholds.

## What would increase confidence

- BTC still holding well above 72k on April 18-19.
- Stable Binance trading conditions near the event.
- Continued absence of obvious downside catalysts.

## Net update logic

The rules check mattered most because it confirmed this is a strict close-above market. That pulls probability below the hazard-like optimism often appropriate for touch markets. But the direct Binance price buffer and recent daily structure still leave Yes as the higher-probability outcome. The current lean is therefore moderately above market, but not by much.

## Suggested downstream use

Use as forecast update and synthesis input. The main live question is not what Bitcoin is in general, but whether any downside catalyst emerges before the specific noon ET settlement minute.
