---
type: evidence_map
case_key: case-20260413-de71fc13
dispatch_id: dispatch-case-20260413-de71fc13-20260413T130158Z
research_run_id: 67b7a757-3f04-4904-be5e-135fea8db74d
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-68k-on-april-13
question: "Will the Binance BTC/USDT 12:00 ET 1m candle close above 68000 on 2026-04-13?"
driver: operational-risk
date_created: 2026-04-13
agent: catalyst-hunter
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-de71fc13/researcher-analyses/2026-04-13/dispatch-case-20260413-de71fc13-20260413T130158Z/personas/catalyst-hunter.md"]
tags: ["evidence-map", "timing", "settlement", "binance"]
---

# Summary

The evidence nets to a strong Yes lean because direct Binance spot candles visible during the run are already far above 68000, but the exact governing minute could not yet be directly retrieved from the public API. This makes the main residual risk operational/timing-related rather than price-related.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-13 have a final Close above 68000?

## Current lean

Strong lean Yes.

## Prior / starting view

Starting view was to respect the market's 92.9% Yes pricing but verify the contract mechanics and exact time mapping because this is a date-sensitive, narrow-resolution market.

## Evidence supporting the claim

- Direct Binance 1m candle outputs during the run show closes around 71118 to 71139.
  - Source: source note `2026-04-13-catalyst-hunter-binance-api-and-contract.md`
  - Causal relevance: underlying price level is comfortably above threshold.
  - Direct or indirect: direct.
  - Weight: high.

- Polymarket contract language is straightforward: settle from Binance BTC/USDT 1m candle close at 12:00 ET.
  - Source: same source note.
  - Causal relevance: defines what all material conditions are.
  - Direct or indirect: direct.
  - Weight: high.

- Binance exchangeInfo confirms BTCUSDT spot pair and 0.01 tick size, reducing precision ambiguity.
  - Source: same source note.
  - Causal relevance: rules out edge-case precision concerns at a 68000 threshold.
  - Direct or indirect: direct.
  - Weight: medium.

## Evidence against the claim

- The exact target candle for 12:00 ET was not yet retrievable from the public Binance API during this run.
  - Source: same source note.
  - Causal relevance: prevents literal direct confirmation of the exact governing candle.
  - Direct or indirect: direct.
  - Weight: high.

## Ambiguous or mixed evidence

- Binance server time and kline availability were not perfectly aligned with what one would expect if the exact target minute were already fully accessible through the queried surface.
- This could reflect harmless API availability quirks, but it is still a non-zero operational ambiguity.

## Conflict between inputs

No major factual conflict across sources. The main issue is not disagreement but incomplete direct access to the exact authoritative minute.

## Key assumptions

- The exact governing Binance minute, once fully accessible, will not differ dramatically from the directly observed nearby price level.
- ET-to-UTC mapping is straightforward and the contract means noon America/New_York = 16:00 UTC on 2026-04-13.

## Key uncertainties

- Exact availability and visibility of the target minute on Binance's settlement surface at research time.
- Whether Binance web UI and public API are perfectly synchronized for this candle.

## Disconfirming signals to watch

- The actual 12:00 ET Binance candle prints at or below 68000.
- A timestamp interpretation issue shows the wrong minute was being inspected.
- Settlement source behavior differs from public API assumptions.

## What would increase confidence

- Direct retrieval or screenshot of the exact 12:00 ET candle from the Binance web chart used in settlement.
- Independent confirmation from another data vendor that mirrors Binance spot minute candles for that exact timestamp.

## Net update logic

The market started very high and the evidence largely supports it. What mattered most was the huge cushion between observed Binance spot prices (~71.1k) and the 68k threshold. What was downweighted was generic crypto narrative noise, because by the time of this run the dominant issue was not directional BTC thesis but exact settlement-surface confirmation. The current lean is therefore a catalyst/timing view: almost all repricing catalysts are exhausted except any last-mile operational verification surprise.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- retrospective evaluation of settlement-surface verification practice