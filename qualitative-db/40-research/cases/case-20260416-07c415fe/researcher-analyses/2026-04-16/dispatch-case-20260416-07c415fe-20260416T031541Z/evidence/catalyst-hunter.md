---
type: evidence_map
case_key: case-20260416-07c415fe
dispatch_id: dispatch-case-20260416-07c415fe-20260416T031541Z
research_run_id: 4f457ed3-7982-427a-9eed-6d9dd9cdb104
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: tokens
entity: sol
topic: sol-above-80-april-19
question: "Will the Binance SOL/USDT 12:00 ET 1-minute candle on 2026-04-19 close above 80?"
driver: reliability
date_created: 2026-04-15T23:24:00-04:00
agent: Orchestrator
status: draft
confidence: medium-high
conflict_status: low
action_relevance: high
related_entities: ["sol", "solana"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-07c415fe/researcher-analyses/2026-04-16/dispatch-case-20260416-07c415fe-20260416T031541Z/personas/catalyst-hunter.md"]
tags: ["evidence-map", "timing-risk", "binance"]
---

# Summary

Current lean is Yes because direct Binance pricing already sits comfortably above the strike and there is no identified scheduled negative catalyst. The main reason this is not near-100% is that the contract settles on a single Sunday noon ET one-minute candle, so weekend volatility can still matter.

## Question being evaluated

Will the Binance SOL/USDT 1-minute candle at 12:00 ET on 2026-04-19 close strictly above 80?

## Current lean

Yes, high probability.

## Prior / starting view

Given the assignment market price of 0.92, the starting baseline was already strong Yes.

## Evidence supporting the claim

- Binance spot price around 85.43 at retrieval.
  - direct
  - high weight
  - matters because Binance is the resolution source and current cushion is meaningful.
- Recent daily Binance closes consistently above 80.
  - direct
  - medium-high weight
  - matters because it shows the market is not hovering right at the threshold.
- Last 72 hourly Binance closes all above 80.
  - direct
  - high weight
  - matters because this specifically addresses short-horizon timing fragility.
- BTC context stayed constructive rather than breaking down.
  - indirect
  - medium weight
  - matters because a crypto-beta shock is the clearest plausible near-term bearish catalyst.

## Evidence against the claim

- Weekend crypto volatility can erase a multi-dollar cushion quickly.
  - indirect but causally important
  - medium-high weight
- Single-candle settlement means path dependence is high.
  - direct contract-interpretation issue
  - medium weight
- No authoritative source can directly settle the future price today.
  - structural limitation
  - low-medium weight

## Ambiguous or mixed evidence

- Polymarket page showed about 89% for the 80 strike while assignment metadata said 92%; this is close enough not to matter directionally but is a reminder that market baseline is moving.
- CoinGecko spot cross-check confirmed general price level but adds limited independent information because crypto spot venues are highly correlated.

## Conflict between inputs

No major factual conflict. The only mild tension is between very high market confidence and the inherent fragility of a one-minute Sunday resolution print.

## Key assumptions

- No major risk-off weekend move before noon ET Sunday.
- No Solana-specific outage or Binance-specific disruption.
- Recent hourly support remains informative into the weekend.

## Key uncertainties

- Weekend macro or crypto sentiment shock.
- Binance-specific microstructure at the exact resolution minute.
- Whether current cushion narrows materially over the next 48-72 hours.

## Disconfirming signals to watch

- SOL hourly closes moving down toward 80.
- BTC sharp downside acceleration.
- Solana operational issue or market-structure disruption.

## What would increase confidence

- Another 24-48 hours of Binance hourly closes mostly above 83.
- Stable BTC and no weekend risk-off headline.
- Sunday-morning ET spot still comfortably above 80.

## Net update logic

The evidence kept the starting strong-Yes view intact and slightly strengthened it. What mattered most was not generic Solana optimism but the combination of explicit contract mechanics plus direct Binance hourly structure. I downweighted broad narrative commentary because no scheduled bullish catalyst appears necessary for Yes; the forecast mostly depends on avoiding a downside shock.

## Suggested downstream use

forecast update
