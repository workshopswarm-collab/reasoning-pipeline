---
type: assumption_note
case_key: case-20260406-6e955d27
dispatch_id: dispatch-case-20260406-6e955d27-20260408T153555Z
research_run_id: ff805c34-4feb-40de-86fc-94ea5759c616
analysis_date: 2026-04-08
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-66-000-on-april-6
question: "Will the price of Bitcoin be above $66,000 on April 6?"
driver: operational-risk
date_created: 2026-04-08
agent: Orchestrator
status: active
certainty: high
importance: high
time_horizon: event-resolution
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260406-6e955d27/researcher-analyses/2026-04-08/dispatch-case-20260406-6e955d27-20260408T153555Z/personas/market-implied.md"]
tags: ["settlement-assumption", "timestamp-mapping", "binance"]
---

# Assumption

The market resolves using the Binance BTCUSDT 1-minute candle that opens at 12:00:00 ET on April 6, 2026, equivalent to 16:00:00 UTC.

## Why this assumption matters

The probability estimate and contract interpretation depend almost entirely on selecting the correct one-minute candle. A one-minute offset would still likely leave the market above 66,000 here, but the exact governing evidence must match the contract wording.

## What this assumption supports

- The conclusion that the market should resolve Yes.
- The judgment that the live market price of 0.825 was conservative relative to the available exchange data.
- The view that settlement ambiguity is low rather than medium/high.

## Evidence or logic behind the assumption

- Polymarket's rules explicitly name the Binance BTC/USDT 1-minute candle for `12:00` ET on the target date.
- Binance kline data are labeled by candle open time, so the 12:00 candle is naturally the interval beginning at 12:00:00 ET.
- Converting 12:00 ET on 2026-04-06 yields 16:00:00 UTC because April is in daylight-saving time.

## What would falsify it

- Clear Polymarket guidance that the relevant candle is the one ending at 12:00 ET rather than opening at 12:00 ET.
- Evidence that Binance's displayed chart labels the candle differently from its API open-time convention for this market.
- A contract clarification specifying a different timezone treatment.

## Early warning signs

- Comment-thread disputes focused on 11:59 vs 12:00 vs 12:01 candle interpretation.
- Inconsistency between Binance UI candle labels and API timestamps.
- Polymarket mods referencing a screenshot or settlement convention not reflected in the raw kline endpoint.

## What changes if this assumption fails

The exact settlement check would need to be rerun on the corrected candle. In this case the directional answer would probably remain Yes unless the intended candle were materially different and below 66,000, which seems unlikely given adjacent minutes also sit near 69.9k.

## Notes that depend on this assumption

- `qualitative-db/40-research/cases/case-20260406-6e955d27/researcher-analyses/2026-04-08/dispatch-case-20260406-6e955d27-20260408T153555Z/personas/market-implied.md`
- `qualitative-db/40-research/cases/case-20260406-6e955d27/researcher-analyses/2026-04-08/dispatch-case-20260406-6e955d27-20260408T153555Z/evidence/market-implied.md`