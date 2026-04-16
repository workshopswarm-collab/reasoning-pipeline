---
type: assumption_note
case_key: case-20260414-3ce42d6c
dispatch_id: dispatch-case-20260414-3ce42d6c-20260414T130958Z
research_run_id: fc9667cb-b24a-4bc0-a81f-f501bdd86843
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-14
question: "Will the Binance BTC/USDT 1-minute candle for 2026-04-14 12:00 ET close above 70000?"
driver: operational-risk
date_created: 2026-04-14
agent: Orchestrator
status: active
certainty: medium
importance: medium
time_horizon: intraday
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["variant-view.md"]
tags: ["settlement-assumption", "binance", "noon-candle"]
---

# Assumption

The most important residual risk is not BTC directional weakness but whether the exact Binance noon-ET 1-minute close remains consistent with the broadly observed above-70,000 trading state.

## Why this assumption matters

The market is priced near certainty, so almost all remaining uncertainty is concentrated in contract mechanics and exact timestamp execution rather than in the broader BTC trend.

## What this assumption supports

- A high but not perfect Yes probability.
- A mild discount versus full certainty despite spot/contextual evidence above 70,000.
- The variant-view emphasis on operational/source-specific fragility rather than macro contrarianism.

## Evidence or logic behind the assumption

- Polymarket rules make the exact Binance one-minute candle the sole governing source of truth.
- Binance public BTCUSDT market data showed active trading and prices materially above 70,000 during the research window.
- Because the price buffer above 70,000 was several thousand dollars, broad directional downside large enough to break the threshold looked less plausible than exchange/timestamp edge risk.

## What would falsify it

- Direct confirmation of the exact 12:00 ET Binance 1-minute close above 70,000.
- Evidence that the exact resolving candle already settled cleanly and unambiguously.
- Alternatively, evidence that the noon-ET candle actually closed at or below 70,000.

## Early warning signs

- Inability to reproduce Binance's exact resolving candle from multiple Binance surfaces.
- Any discrepancy between Binance display surfaces and API/history surfaces.
- Any sign of a sudden sharp drop toward 70,000 near 16:00 UTC.

## What changes if this assumption fails

If the exact noon-ET candle is directly confirmed above 70,000, the remaining residual doubt should shrink toward near-zero. If the exact candle is at or below 70,000, the current view fails outright despite broader bullish contextual evidence.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260414-3ce42d6c/researcher-analyses/2026-04-14/dispatch-case-20260414-3ce42d6c-20260414T130958Z/personas/variant-view.md