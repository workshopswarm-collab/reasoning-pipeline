---
type: evidence_map
case_key: case-20260414-1b10f4b2
dispatch_id: dispatch-case-20260414-1b10f4b2-20260414T201759Z
research_run_id: 3caad19e-18d1-4cb9-96c3-50359757c0df
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: "catalyst map for BTC > 68k on 2026-04-20"
driver: operational-risk
date_created: 2026-04-14
agent: catalyst-hunter
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-1b10f4b2/researcher-analyses/2026-04-14/dispatch-case-20260414-1b10f4b2-20260414T201759Z/personas/catalyst-hunter.md"]
tags: ["evidence-map", "catalysts", "timing", "btc"]
---

# Summary

The market is primarily a short-window threshold-holding question. The evidence map leans Yes because current Binance BTC/USDT is well above 68k and the remaining scheduled catalyst calendar looks relatively light.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle at 12:00 ET on 2026-04-20 close above 68,000?

## Current lean

Lean Yes, with high but not near-certain odds.

## Prior / starting view

Starting view: market may be directionally right because BTC is already above threshold, but a 94% market price is high enough to require explicit checks on settlement mechanics and near-term catalysts.

## Evidence supporting the claim

- **Binance spot materially above threshold**  
  - Source: Binance public ticker / kline APIs and source note 2026-04-14-catalyst-hunter-binance-price-context  
  - Why it matters causally: the market only needs BTC to hold, not to break a fresh upside level  
  - Direct or indirect: direct  
  - Weight: high

- **Recent daily closes have remained comfortably above 68k**  
  - Source: same Binance API note  
  - Why it matters causally: suggests current regime is not hovering right at the boundary  
  - Direct or indirect: direct  
  - Weight: medium-high

- **No scheduled FOMC decision before resolution**  
  - Source: Federal Reserve 2026 meeting calendar and source note 2026-04-14-catalyst-hunter-resolution-and-calendars  
  - Why it matters causally: removes one of the most obvious macro repricing catalysts inside the window  
  - Direct or indirect: contextual  
  - Weight: medium

- **No CPI release before resolution**  
  - Source: BLS CPI schedule and resolution/calendar source note  
  - Why it matters causally: removes another major scheduled macro volatility event inside the window  
  - Direct or indirect: contextual  
  - Weight: medium

## Evidence against the claim

- **BTC can still move 8-10% in a few days**  
  - Source: Binance recent daily highs/lows and general observed volatility in recent sample  
  - Why it matters causally: current cushion is meaningful but not impregnable  
  - Direct or indirect: direct/contextual mix  
  - Weight: high

- **Exact settlement depends on one minute on one venue**  
  - Source: Polymarket rule text  
  - Why it matters causally: a broader BTC market level above 68k elsewhere would not matter if Binance prints below on the exact minute  
  - Direct or indirect: direct to contract interpretation  
  - Weight: medium-high

- **Unscheduled macro or crypto-native shock risk remains live**  
  - Source: inference from empty scheduled calendar rather than a direct source  
  - Why it matters causally: absence of scheduled catalysts does not eliminate weekend/event headline risk  
  - Direct or indirect: contextual  
  - Weight: medium

## Ambiguous or mixed evidence

- Lack of scheduled macro catalysts is bullish for holding the line, but it also means the market could simply be pricing current spot mechanically rather than missing some hidden catalyst.
- Market price at 93.5% may partly reflect correct threshold distance math rather than overconfidence.

## Conflict between inputs

No major factual conflict among checked sources. The main uncertainty is weighting-based: whether the roughly 9% cushion is enough to justify a price in the mid-90s over a six-day horizon.

## Key assumptions

- No major unscheduled shock before resolution.
- Binance venue behavior remains representative enough that current spot cushion is informative.
- The exact noon ET candle is not unusually vulnerable to transient distortion.

## Key uncertainties

- Weekend and headline risk.
- Whether BTC's current run-up is extended and prone to mean reversion before April 20.
- Whether hidden market-moving catalysts exist outside the checked Fed/BLS schedule.

## Disconfirming signals to watch

- Daily close back toward or below 70k.
- Sharp risk-off move in equities or crypto over the weekend.
- Venue-specific Binance operational issue or abnormal dislocation.

## What would increase confidence

- BTC continuing to close above 72k-73k into the weekend.
- Evidence of stable broad risk appetite without major macro surprises.
- Continued absence of crypto-specific regulatory or exchange stress headlines.

## Net update logic

The verification pass strengthened the initial Yes lean because it showed the market is not relying on an obvious imminent macro event to stay above threshold; instead the contract mainly asks whether BTC can avoid a sizeable drawdown from an already elevated spot level. That still leaves real one-minute and one-venue fragility, so the view stays below the market's implied probability.

## Suggested downstream use

Use as an orchestrator synthesis input and as audit support for why catalyst-hunter modestly underweights a 94% market price without flipping bearish.