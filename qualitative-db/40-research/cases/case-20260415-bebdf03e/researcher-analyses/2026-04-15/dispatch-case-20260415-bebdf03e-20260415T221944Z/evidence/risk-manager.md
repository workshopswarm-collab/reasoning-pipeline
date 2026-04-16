---
type: evidence_map
case_key: case-20260415-bebdf03e
dispatch_id: dispatch-case-20260415-bebdf03e-20260415T221944Z
research_run_id: 30efc9e9-e421-477e-bf29-ef701cdffe4a
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-21
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-21 be above 72000?"
driver: operational-risk
date_created: 2026-04-15
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-bebdf03e/researcher-analyses/2026-04-15/dispatch-case-20260415-bebdf03e-20260415T221944Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "risk-manager"]
---

# Summary

Net evidence favors Yes because BTC is currently well above 72,000 on the governing venue, but the confidence should be capped because the contract settles on one exact noon-minute Binance close rather than a daily close or broad average.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle at 12:00 ET on 2026-04-21 have a final close price above 72,000?

## Current lean

Lean Yes, but with more fragility than the 81.5% market price suggests.

## Prior / starting view

Starting view was that current BTC level likely makes Yes favored, but the run needed to verify the exact contract mechanics and quantify the path/timing risk.

## Evidence supporting the claim

- `2026-04-15-risk-manager-binance-resolution-and-live-price.md`: Binance live BTCUSDT price was about 75,012, roughly 3,012 above the threshold. Direct evidence, high weight.
- Same note: Binance 24h low was 73,514, still above 72,000. Direct/context hybrid, medium-high weight.
- `2026-04-15-risk-manager-polymarket-contract-and-pricing.md`: the broader ladder implies the crowd centers plausible settlement levels in the low-to-mid 70s, with 72k clearly below the center. Contextual evidence, medium weight.

## Evidence against the claim

- Contract resolves on one exact minute at 12:00 ET on April 21, so even a modest multi-day drawdown or intraminute spike down on Binance can flip the result. Direct contract risk, high weight.
- Current cushion is only about 4.2%; BTC can move that much in less than a day, so this is not a lock despite current spot. Contextual market-risk logic, medium-high weight.
- Single-venue settlement creates exchange-specific microstructure and operational-risk exposure. Direct contract-design risk, medium weight.

## Ambiguous or mixed evidence

- The market price itself is informative but circular: it aggregates crowd judgment rather than independently validating the thesis.
- Coindesk's generic BTC page is useful only as broad context that BTC remains an actively traded macro-sensitive asset; it did not materially move the estimate.

## Conflict between inputs

There was no major factual conflict. The main tension is weighting-based: current spot and 24h range support Yes, while the contract's minute-specific settlement structure argues for discounting overconfidence.

## Key assumptions

- BTC remains above 72,000 on Binance through the settlement window.
- No major exchange-specific dislocation distorts the noon candle.
- Recent price cushion is informative enough to persist for five more days.

## Key uncertainties

- Macro/news catalysts over the next five days.
- Whether volatility clusters around U.S. trading hours near settlement.
- Whether Binance and the visible chart candle align cleanly with API-observed data at settlement.

## Disconfirming signals to watch

- BTCUSDT trading back into the 72,000-73,000 band before April 21.
- A sudden risk-off crypto move that erases the current cushion.
- Exchange-specific anomalies on Binance.

## What would increase confidence

- BTC remaining above roughly 74,000 into April 20-21.
- Continued Binance intraday lows holding comfortably above 72,000.
- No evidence of venue-specific dislocation.

## Net update logic

The decisive update was verifying the exact contract source of truth and then checking live Binance prices. That combination supports Yes, but it also reveals that the market's confidence rests on a narrow operational condition: one minute, one venue, one close print. That is why the risk-manager view is slightly below the market despite agreeing on direction.

## Suggested downstream use

Use as an orchestrator synthesis input and as a caution against treating current spot distance from threshold as equivalent to settlement certainty.