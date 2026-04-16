---
type: evidence_map
case_key: case-20260414-91430615
dispatch_id: dispatch-case-20260414-91430615-20260414T235247Z
research_run_id: 094c848f-851d-497a-92a7-760978ddacfc
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-binance-btc-usdt-12-00-et-1-minute-candle-on-2026-04-19-close-above-70000
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-19 close above 70000?"
driver: operational-risk
date_created: 2026-04-14
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-91430615/researcher-analyses/2026-04-14/dispatch-case-20260414-91430615-20260414T235247Z/personas/catalyst-hunter.md"]
tags: ["evidence-map", "btc", "catalyst", "resolution"]
---

# Summary

This market currently leans Yes because BTC/USDT on Binance is already materially above 70000, but the path to settlement still runs through a single weekend-adjacent one-minute print, so downside shock and source-specific execution risk remain the main reasons not to treat 90%+ as certainty.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle at 12:00 ET on April 19, 2026 close strictly above 70000?

## Current lean

Lean Yes, but less confidently than the market.

## Prior / starting view

Starting view: if BTC was only slightly above 70000, this would be close to a coin-flip over five days; if it was comfortably above and recent regime supported it, fair odds should be materially above 50% but still below near-certainty because bitcoin can move several percent quickly.

## Evidence supporting the claim

- Binance spot at 74065 on Apr 14.
  - Direct/primary.
  - Matters because the contract resolves on Binance BTC/USDT specifically.
  - Weight: high.
- Recent Binance daily closes mostly in the 71k-74k area, with multiple sessions above 70k.
  - Direct/primary contextual evidence.
  - Matters because the threshold sits below the recent center of mass rather than near the upper bound.
  - Weight: high.
- Polymarket rules require only a single close above 70k, not maintenance above a higher threshold or multi-exchange confirmation.
  - Direct contract evidence.
  - Matters because the bar for Yes is relatively forgiving if the current regime persists.
  - Weight: medium.

## Evidence against the claim

- Bitcoin can move 5%+ in a few days, and the current cushion above 70k is only about 5.8%.
  - Indirect but highly relevant market-structure consideration.
  - Matters because a normal crypto drawdown could erase the cushion before Sunday noon ET.
  - Weight: high.
- Resolution depends on one exact minute on Binance, creating timing and venue-specific fragility.
  - Direct contract interpretation plus operational-risk framing.
  - Matters because broader bitcoin strength can still lose if Binance prints below 70k at that minute.
  - Weight: medium-high.
- Weekend / low-liquidity dynamics before April 19 can amplify short-term volatility and liquidation cascades.
  - Contextual evidence.
  - Weight: medium.

## Ambiguous or mixed evidence

- High recent momentum can help hold above 70k, but it may also reflect a stretched move vulnerable to reversal.
- The market's 90% price may encode informed expectations about stable macro conditions, but it may also underprice one-minute settlement risk.

## Conflict between inputs

There is little factual conflict between inputs. The disagreement is mainly weighting-based: whether current price regime dominance should outweigh single-minute settlement fragility and normal bitcoin volatility over five days.

## Key assumptions

- No major macro or crypto-specific downside shock before resolution.
- Binance remains a usable, representative pricing venue at resolution time.
- Recent price regime is informative rather than a temporary blow-off.

## Key uncertainties

- Short-horizon realized volatility from now to Apr 19.
- Whether any macro headline, ETF-flow reversal, or weekend risk-off move arrives before noon ET Sunday.
- Exact ET-to-Binance candle mapping at settlement display level, though the contract wording is clear enough for current analysis.

## Disconfirming signals to watch

- BTC losing 72k/71k support on Binance before Friday/Saturday.
- A sudden leverage unwind or exchange-specific dislocation.
- Material divergence between Binance and other major venues indicating venue-specific risk.

## What would increase confidence

- BTC holding above 72k into the weekend.
- Continued benign macro backdrop with no sharp risk-off move.
- Additional verification that Binance minute-candle display/API handling aligns cleanly with noon ET interpretation.

## Net update logic

Primary evidence pushed the view meaningfully toward Yes because the threshold is already below current and recent Binance trading. The main reason the estimate stops below the market is that this contract resolves on one specific minute, leaving room for ordinary bitcoin volatility and venue/timing fragility to matter more than the current 90%+ market appears to allow.

## Suggested downstream use

Use as orchestrator synthesis input and as a forecast-weighting check against more conviction-heavy bullish personas.