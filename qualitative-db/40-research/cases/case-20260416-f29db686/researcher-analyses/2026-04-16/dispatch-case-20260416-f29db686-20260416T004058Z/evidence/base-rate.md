---
type: evidence_map
case_key: case-20260416-f29db686
dispatch_id: dispatch-case-20260416-f29db686-20260416T004058Z
research_run_id: f3df4fb0-1303-4d8f-8f7b-07c8dd6ed0e7
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-74-000-on-april-17
question: "Will the price of Bitcoin be above $74,000 on April 17?"
driver: reliability
date_created: 2026-04-16
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
downstream_uses: []
tags: ["btc", "threshold-market", "short-horizon"]
---

# Summary

The evidence nets to a moderate Yes lean: BTC is already above the threshold and has recently closed above it several times, but the threshold is close enough to spot that ordinary BTC day-scale volatility still leaves a substantial No path.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17, 2026 have a final close above 74,000?

## Current lean

Lean Yes, but only moderately.

## Prior / starting view

For a one-day BTC threshold market with spot only about 1% above the strike, the base prior should be near a coin flip with a modest upward tilt if recent regime and momentum are supportive.

## Evidence supporting the claim

- **Current spot above threshold on Binance**  
  - Source: Binance recent 1m/1h/1d candles; source note `2026-04-16-base-rate-binance-and-cross-exchange-context.md`  
  - Why it matters causally: the event only needs BTC to remain above 74k at one narrow future timestamp, and current price is already above that level.  
  - Direct or indirect: direct settlement-adjacent evidence.  
  - Weight: high.

- **Recent daily closes above 74k**  
  - Source: Binance daily candles for Apr 13-15.  
  - Why it matters causally: indicates BTC has recently sustained this regime rather than merely touching it once.  
  - Direct or indirect: direct settlement-adjacent context.  
  - Weight: medium-high.

- **Cross-venue price alignment**  
  - Source: CoinGecko market chart and Kraken ticker; same source note.  
  - Why it matters causally: reduces concern that Binance is idiosyncratically rich versus the broader market.  
  - Direct or indirect: indirect/contextual.  
  - Weight: medium.

## Evidence against the claim

- **Margin above threshold is small**  
  - Source: Binance spot around 74.8k versus 74k threshold.  
  - Why it matters causally: BTC can easily move more than ~1% over a day, so current in-the-money status is far from decisive.  
  - Direct or indirect: direct settlement-adjacent context.  
  - Weight: high.

- **BTC short-horizon volatility remains meaningful**  
  - Source: Binance daily/hourly candles showing swings of several hundred to a few thousand dollars intraday.  
  - Why it matters causally: even in a supportive regime, noise alone can flip a noon snapshot market.  
  - Direct or indirect: contextual/base-rate evidence.  
  - Weight: high.

## Ambiguous or mixed evidence

- **Recent upward regime** cuts toward Yes, but may also mean some near-term upside is already reflected and vulnerable to pullback.
- **Market price near 61%** is informative as a crowd baseline, but may partly reflect the same currently-above-threshold observation rather than deeper structural edge.

## Conflict between inputs

No major factual conflict. The main disagreement is weighting: how much to trust current above-threshold spot versus normal BTC one-day volatility.

## Key assumptions

- BTC remains in the present mid-74k regime into the April 17 noon ET window.
- Binance remains a reliable source of price formation near settlement.
- No major macro or crypto-specific shock hits before settlement.

## Key uncertainties

- Overnight macro/news flow.
- Whether a modest pullback below 74k develops before the exact settlement minute.
- Precise mapping of the noon ET candle in Binance time displays is operationally clear in rule text but still deserves a settlement-time check.

## Disconfirming signals to watch

- Sustained trading back below 74k on Binance before the morning of Apr 17.
- Broader crypto weakness confirmed across Kraken/CoinGecko-tracked spot.
- Exchange disruption or unusual Binance dislocation near settlement.

## What would increase confidence

- Continued hourly closes above 74k into Apr 17.
- Spot widening to a more comfortable cushion above 74k.
- Absence of macro or crypto-specific negative catalysts into settlement.

## Net update logic

The base-rate start is close to 50/50 because this is a very short-horizon threshold on a volatile asset. Current spot and recent closes above 74k justify moving above that prior, but only to the low 60s because the threshold is still close enough for routine volatility to matter.

## Suggested downstream use

Use as an input favoring a modest Yes lean, not a high-conviction one. This should be netted with any catalyst/momentum or microstructure researcher views before final synthesis.