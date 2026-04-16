---
type: assumption_note
case_key: case-20260413-e2ee488e
dispatch_id: dispatch-case-20260413-e2ee488e-20260413T222544Z
research_run_id: acac250b-229a-4bc5-bd09-8fc5926e4b62
analysis_date: 2026-04-13
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-15
question: "Will the price of Bitcoin be above $70,000 on April 15?"
driver: operational-risk
date_created: 2026-04-13
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: short
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["assumption", "binance", "settlement"]
---

# Assumption

The market will resolve off the ordinary Binance BTC/USDT spot 1-minute candle at 12:00 PM America/New_York on 2026-04-15 without exchange disruption or contract-interpretation surprise.

## Why this assumption matters

If the exchange feed is disrupted, the timezone mapping is interpreted differently, or Polymarket applies a non-obvious fallback, then the simple outside-view comparison between current spot and the 70,000 threshold becomes less trustworthy.

## What this assumption supports

- A high base-rate probability that BTC remains above 70,000 by the settlement minute.
- A narrow focus on short-horizon downside volatility rather than broader market-structure questions.
- Using Binance spot data as the governing evidence floor.

## Evidence or logic behind the assumption

Polymarket's published rules explicitly name Binance BTC/USDT 1-minute candle close at 12:00 ET. Binance spot API endpoints were reachable during this run, server time was current, and BTCUSDT showed active trading status.

## What would falsify it

- A clear Polymarket clarification changing the resolution source or time interpretation.
- Binance outage or missing/corrupted candle around the settlement minute.
- Evidence that the relevant candle is not the ordinary 12:00-12:00:59 ET minute close traders would naturally expect.

## Early warning signs

- Binance spot instability or degraded market-data availability before settlement.
- Polymarket comments or updates flagging ambiguity in candle selection.
- Large cross-exchange divergence suggesting venue-specific price risk.

## What changes if this assumption fails

Confidence should drop and the case would need a contract-interpretation / operational-resolution review rather than a straightforward price-level base-rate analysis.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260413-e2ee488e/researcher-analyses/2026-04-13/dispatch-case-20260413-e2ee488e-20260413T222544Z/personas/base-rate.md
- qualitative-db/40-research/cases/case-20260413-e2ee488e/researcher-source-notes/2026-04-13-base-rate-binance-polymarket-resolution-context.md
