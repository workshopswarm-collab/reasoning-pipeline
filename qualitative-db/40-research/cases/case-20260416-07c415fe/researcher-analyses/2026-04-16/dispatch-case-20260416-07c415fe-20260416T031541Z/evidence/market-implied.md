---
type: evidence_map
case_key: case-20260416-07c415fe
dispatch_id: dispatch-case-20260416-07c415fe-20260416T031541Z
research_run_id: 8e7ee674-e41f-4159-999d-00129c2c1fc8
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: tokens
entity: sol
topic: solana-above-80-on-april-19
question: "Will the Binance SOL/USDT 12:00 ET one-minute candle on 2026-04-19 close above 80?"
driver: reliability
date_created: 2026-04-16
agent: market-implied
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["sol", "solana"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "market-implied", "crypto"]
---

# Summary

The evidence nets to a high-Yes lean that is close to, but a touch below, the market. The crowd appears to be pricing current spot cushion and recent persistence above 80 correctly, while perhaps slightly underweighting short-horizon crypto downside tails.

## Question being evaluated

Will Binance SOL/USDT's one-minute candle at 12:00 ET on April 19, 2026 close above 80?

## Current lean

Lean Yes, high probability.

## Prior / starting view

Starting view was to respect the 0.92 market prior unless Binance-specific data or contract interpretation suggested a hidden trap.

## Evidence supporting the claim

- Binance spot near 85.26 at check time.
  - Source: Binance API ticker / source note.
  - Why it matters: direct exchange-specific cushion above the strike.
  - Direct or indirect: direct.
  - Weight: high.
- Recent Binance daily closes mostly above 80 for nearly two weeks.
  - Source: Binance API daily klines / source note.
  - Why it matters: suggests the threshold is below the recent active trading regime, not just barely crossed intraday.
  - Direct or indirect: direct.
  - Weight: high.
- Contract resolves at a single minute, not on a tougher sustained-average condition.
  - Source: Polymarket rules / source note.
  - Why it matters: lowers the burden for Yes versus a daily settlement metric.
  - Direct or indirect: direct for rules.
  - Weight: medium-high.
- Polymarket crowd pricing around 89-90% Yes.
  - Source: Polymarket event page / source note.
  - Why it matters: suggests the market is already encoding short-horizon volatility risk rather than treating Yes as certain.
  - Direct or indirect: direct for market prior.
  - Weight: medium.

## Evidence against the claim

- Three trading days is enough time for a high-beta crypto asset to fall more than 6%.
  - Source: inference from recent SOL volatility and hourly range.
  - Why it matters: present cushion is real but not huge in crypto terms.
  - Direct or indirect: indirect/contextual.
  - Weight: high.
- The contract is exchange- and minute-specific.
  - Source: Polymarket rules / source note.
  - Why it matters: a brief wick or Binance-specific dislocation at exactly noon ET could defeat a broadly bullish thesis.
  - Direct or indirect: direct for rules.
  - Weight: medium.

## Ambiguous or mixed evidence

- CoinGecko spot and daily data broadly matched Binance, which is reassuring on recency and direction, but it is not the governing source of truth and therefore mostly serves as a verification check rather than independent decisive evidence.

## Conflict between inputs

No major factual conflict. The only mild tension is between the assignment's listed `current_price: 0.92` and the fetched page snapshot around 89-90%; this looks like ordinary live-market movement / spread noise, not a substantive disagreement.

## Key assumptions

- Current SOL trading regime remains intact through the settlement window.
- No exchange-specific anomaly on Binance SOL/USDT materially distorts the noon ET candle.

## Key uncertainties

- Short-horizon crypto volatility over the next ~72 hours.
- Whether a broader risk-off move hits altcoins disproportionately before settlement.

## Disconfirming signals to watch

- SOL losing 80 before April 19 and failing to regain it.
- A sharp market-wide downside move in majors/high-beta alts.
- Evidence that Binance-specific prints are diverging from the broader market.

## What would increase confidence

- Continued Binance trading above 83-84 into April 18-19.
- Stable broader crypto market tone without a major macro shock.

## Net update logic

The main update from evidence collection was that Binance-specific spot/path data largely validated the market's optimistic prior. That said, the market is near an extreme and the contract is narrow, so I haircut slightly below the market rather than fully matching it.

## Suggested downstream use

Use as orchestrator synthesis input and as a compact audit trail for why the market-implied lane stayed near consensus rather than forcing contrarian downside.