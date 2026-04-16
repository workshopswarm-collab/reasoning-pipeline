---
type: evidence_map
case_key: case-20260415-9a9c8ea3
dispatch_id: dispatch-case-20260415-9a9c8ea3-20260415T192028Z
research_run_id: bcc74157-37b0-48a8-b04a-9097384605e3
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-16
question: "Will the Binance BTC/USDT 1-minute candle for 12:00 PM ET on 2026-04-16 close above 72000?"
driver: operational-risk
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: medium-high
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: ["intraday-volatility"]
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "btc", "catalyst", "timing"]
---

# Summary

This note nets out a simple but timing-sensitive crypto threshold market. The case is already in the money, so the evidence mostly asks whether any sub-24h catalyst can create a >3.7% drop by the exact noon ET settlement minute.

## Question being evaluated

Will Binance BTC/USDT close above 72,000 on the 1-minute candle labeled 12:00 PM ET on 2026-04-16?

## Current lean

Lean Yes, strongly.

## Prior / starting view

Starting view was that a market at 95.5% is probably correct but still deserves extra rule and source verification because the contract is date-specific, exchange-specific, and at an extreme probability.

## Evidence supporting the claim

- Polymarket rule text explicitly names Binance BTC/USDT 1-minute candle close at 12:00 PM ET on Apr 16 as the governing source and condition. Direct; very high weight.
- Binance ticker API showed BTCUSDT at 74,646.39 on Apr 15. Direct; high weight.
- Binance 1-minute klines around the same verification window closed around 74,633 to 74,646, confirming the ticker was broadly consistent with recent minute-level trading. Direct; high weight.
- The current buffer above strike is about 2,646 points or 3.7% with less than 24 hours left. Indirect but mechanically important; medium-high weight.

## Evidence against the claim

- BTC can move more than 3-4% intraday, so the remaining buffer is meaningful but not absolute. Contextual; medium weight.
- The exact settlement depends on one specific exchange pair and one specific minute candle, so venue-specific dislocation risk is real even if the broader market stays strong. Direct to contract mechanics; medium weight.
- No strong independent event calendar source was found to rule out a near-term macro shock; that keeps residual uncertainty above zero. Contextual; low-medium weight.

## Ambiguous or mixed evidence

- Coingecko verification is useful as a broad contextual cross-check that Bitcoin remains a major liquid asset, but it adds little marginal information for this exact settlement because the contract is Binance-specific.

## Conflict between inputs

There is no major factual conflict. The only real tension is between current in-the-money spot evidence and generic crypto volatility risk.

## Key assumptions

- No downside catalyst drives BTC/USDT below 72,000 by the settlement minute.
- Binance price formation remains normal and representative.
- ET-to-UTC timing is correctly interpreted as 16:00 UTC.

## Key uncertainties

- Whether a macro headline, liquidation cascade, or exchange-specific dislocation appears in the remaining window.
- Whether the precise noon ET candle could briefly print below the threshold even if surrounding minutes remain above it.

## Disconfirming signals to watch

- BTC losing most of the current cushion overnight.
- Binance underperforming other major BTC venues.
- Abrupt realized volatility spike before the noon ET window.

## What would increase confidence

- BTC still trading comfortably above 72k several hours before noon ET.
- No evidence of Binance-specific operational or pricing irregularity.
- Stable or rising BTC through the European and US morning sessions.

## Net update logic

The evidence kept the starting lean intact. What mattered most was that the strike is already well below live verified Binance spot and that the contract uses a very clear named source. What I downweighted was generic crypto narrative chatter without a concrete catalyst in the remaining window. The current lean is therefore mostly a path-risk judgment, not a broader Bitcoin thesis.

## Suggested downstream use

Use as orchestrator synthesis input and as an auditable record of why this run treated the case as high-probability Yes but not literally certain.