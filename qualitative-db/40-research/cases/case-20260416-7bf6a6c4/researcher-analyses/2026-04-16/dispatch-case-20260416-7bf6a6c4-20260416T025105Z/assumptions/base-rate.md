---
type: assumption_note
case_key: case-20260416-7bf6a6c4
dispatch_id: dispatch-case-20260416-7bf6a6c4-20260416T025105Z
research_run_id: e711d43e-5ea4-4790-a7da-2a16d69cb5b3
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin-threshold-close
entity: bitcoin
topic: "BTC/USDT noon ET close staying above 74000"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: short-term
related_entities: ["binance", "polymarket", "bitcoin"]
related_drivers: ["operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-7bf6a6c4/researcher-source-notes/2026-04-16-base-rate-binance-polymarket-context.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-7bf6a6c4/researcher-analyses/2026-04-16/dispatch-case-20260416-7bf6a6c4-20260416T025105Z/personas/base-rate.md"]
tags: ["assumption-note", "bitcoin", "binance", "short-dated", "threshold-close"]
---

# Assumption

The most important assumption is that BTC remains in roughly its current price regime into the Apr 17 noon ET resolving window rather than experiencing a fresh downside move of more than about 1.2% before the specific Binance close that matters.

## Why this assumption matters

The thesis is not that BTC is structurally guaranteed to hold above 74000, only that starting modestly above the threshold one day early makes Yes somewhat more likely than No. If the current regime breaks, the edge disappears quickly.

## What this assumption supports

- A probability estimate modestly above the market-neutral baseline.
- A view that current spot proximity is informative but not decisive.
- The conclusion that this is more likely than not, but not close to certain.

## Evidence or logic behind the assumption

- Binance spot was about 74912 at check time, already above the threshold.
- Recent 1-minute candles over the prior several minutes stayed above 74900 despite intraminute swings.
- In short-dated crypto close markets, starting above the strike usually helps, but the remaining window is long enough for ordinary volatility to matter.

## What would falsify it

- A sustained move back below 74000 well before Apr 17 noon ET.
- New volatility or macro/news shock that pushes BTC materially lower.
- Evidence that Binance-specific prints are persistently weaker than broad BTC spot context.

## Early warning signs

- Repeated hourly trading below 74000 on Binance.
- Broader crypto risk-off move with BTC losing nearby support levels.
- Cross-venue divergence suggesting Binance BTC/USDT is underperforming other reference prices.

## What changes if this assumption fails

The probability should move materially downward, likely to or below 50%, because the contract only cares about one exact closing print and there would then be little cushion left.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260416-7bf6a6c4/researcher-analyses/2026-04-16/dispatch-case-20260416-7bf6a6c4-20260416T025105Z/personas/base-rate.md
