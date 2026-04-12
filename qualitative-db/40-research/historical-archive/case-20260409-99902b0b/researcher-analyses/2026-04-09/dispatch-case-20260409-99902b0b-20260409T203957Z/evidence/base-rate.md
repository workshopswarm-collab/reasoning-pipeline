---
type: evidence_map
case_key: case-20260409-99902b0b
dispatch_id: dispatch-case-20260409-99902b0b-20260409T203957Z
research_run_id: 8cf42efa-ac6e-4464-9882-e88bf5c272f3
analysis_date: 2026-04-09
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-70-000-on-april-10
question: "Will the price of Bitcoin be above $70,000 on April 10?"
driver: reliability
date_created: 2026-04-09
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260409-99902b0b/researcher-analyses/2026-04-09/dispatch-case-20260409-99902b0b-20260409T203957Z/personas/base-rate.md"]
tags: ["evidence-map", "btc", "threshold-market"]
---

# Summary

Direct exchange data and contract wording both point to a straightforward Yes lean, but the market may still be somewhat overconfident because a sub-24-hour 3% drawdown is not rare enough to ignore.

## Question being evaluated

Whether Binance BTC/USDT will have a final 1-minute candle close above 70,000 at 12:00 ET on April 10, 2026.

## Current lean

Lean Yes.

## Prior / starting view

Starting outside view: if BTC is already several percent above the threshold with less than a day to resolution, Yes should usually be favored, but very short-horizon crypto moves are volatile enough that prices in the mid-90s require checking rather than blind acceptance.

## Evidence supporting the claim

- Binance spot price was 72,363.48 near 16:40 ET on April 9.
  - Source: Binance ticker API source note.
  - Why it matters: the resolving venue already sits meaningfully above the threshold.
  - Direct or indirect: direct.
  - Weight: high.
- Binance 1-minute klines around the fetch window closed around 72.36k to 72.39k.
  - Source: Binance kline API source note.
  - Why it matters: this is mechanically close to the contract's actual settlement object.
  - Direct or indirect: direct.
  - Weight: high.
- CoinGecko cross-check showed bitcoin around 72,390.
  - Source: CoinGecko cross-check note.
  - Why it matters: independent contextual confirmation that Binance was not showing an outlier print.
  - Direct or indirect: contextual.
  - Weight: medium.

## Evidence against the claim

- The event resolves on a single future 1-minute close, not on current spot or average daily price.
  - Source: Polymarket rules note.
  - Why it matters: one downside spike at the relevant minute is enough for No.
  - Direct or indirect: direct contract interpretation.
  - Weight: high.
- BTC can move more than 3% over a sub-24-hour window without requiring an extraordinary regime change.
  - Source: base-rate reasoning from asset class behavior; not directly quantified in this run.
  - Why it matters: this is the main reason not to simply mirror a 95% market price.
  - Direct or indirect: contextual.
  - Weight: medium.

## Ambiguous or mixed evidence

- Market price around 95% is itself informative, but it partly reflects the same public spot information and may overstate certainty because threshold markets attract momentum-chasing when spot is comfortably above strike.

## Conflict between inputs

There is no major factual conflict. The main disagreement is weighting-based: how much probability mass to assign to a roughly 3.3% overnight drawdown into one specific resolving minute.

## Key assumptions

- Binance remains the operative exchange and does not experience a settlement-relevant anomaly.
- BTC remains in roughly the same price regime overnight rather than suffering a sharp downside break.

## Key uncertainties

- Short-horizon realized volatility between now and noon ET tomorrow.
- Whether any exchange-specific dislocation appears on Binance even if broader BTC pricing stays above 70k.

## Disconfirming signals to watch

- BTC trades toward 71k or below before the morning of April 10.
- A broad crypto liquidation or macro risk-off shock develops overnight.
- Binance shows unusual divergence from other liquid BTC venues.

## What would increase confidence

- Another direct Binance check late on April 9 or early on April 10 still showing a comfortable cushion above 70k.
- Evidence on recent overnight BTC downside frequencies showing fewer than 1-in-10 moves of this magnitude from similar starting conditions.

## Net update logic

The prior already favored Yes because the asset sits above the strike with little time left. Direct Binance evidence keeps the lean intact. The only meaningful downward adjustment versus the market comes from not wanting to ignore crypto's ability to move several percent in less than a day, especially when resolution depends on one exact minute.

## Suggested downstream use

Use as orchestrator synthesis input and as an auditable explanation for why a Yes view can coexist with mild skepticism toward a mid-90s market price.