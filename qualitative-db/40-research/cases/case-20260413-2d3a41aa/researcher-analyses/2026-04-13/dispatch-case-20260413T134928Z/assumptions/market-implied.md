---
type: assumption_note
case_key: case-20260413-2d3a41aa
dispatch_id: dispatch-case-20260413-2d3a41aa-20260413T134928Z
research_run_id: 0bf2894c-4f80-46c6-8111-b1ad727360f1
analysis_date: 2026-04-13
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-13
question: Will the price of Bitcoin be above $70,000 on April 13?
driver: reliability
date_created: 2026-04-13
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: intraday
related_entities: [btc]
related_drivers: [reliability, operational-risk]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-2d3a41aa/researcher-analyses/2026-04-13/dispatch-case-20260413-2d3a41aa-20260413T134928Z/personas/market-implied.md]
tags: [assumption, intraday, binance, contract-timing]
---

# Assumption

The market price is mostly embedding the simple premise that BTC/USDT on Binance is already trading sufficiently above 70,000 that ordinary intraday noise is unlikely to push the exact 12:00 ET 1-minute close back below the strike.

## Why this assumption matters

The difference between a 71% market-implied probability and a much higher estimate mainly comes from whether the exact noon-ET minute should be treated as just another minute in an above-threshold regime, or as a material jump-risk event where a brief dip could flip resolution.

## What this assumption supports

- A view that the market is directionally right.
- A modestly bullish estimate above the assignment snapshot.
- Treating operational/timing noise as the main residual risk rather than a broad directional BTC thesis failure.

## Evidence or logic behind the assumption

- Direct Binance spot during the run was 71,593.01.
- Recent 1-minute Binance closes available in-session were repeatedly above 70,000.
- The fetched Polymarket ladder showed the 70,000 line at 94%, suggesting the live market may have updated toward a much more confident above-threshold view.

## What would falsify it

- Direct retrieval of the exact 12:00 ET Binance 1-minute candle showing a close at or below 70,000.
- Evidence of a sharp intraminute selloff into the settlement minute.
- Contract interpretation showing a different timestamping convention than assumed.

## Early warning signs

- Binance price slipping toward the 70,000 threshold shortly before noon ET.
- Data discrepancies between Binance web chart and public API.
- Exchange interruptions or delayed final candle publication.

## What changes if this assumption fails

The probability estimate should move sharply lower, and the market should be interpreted as having underweighted timestamp-specific settlement risk.

## Notes that depend on this assumption

- Main market-implied finding for this run.