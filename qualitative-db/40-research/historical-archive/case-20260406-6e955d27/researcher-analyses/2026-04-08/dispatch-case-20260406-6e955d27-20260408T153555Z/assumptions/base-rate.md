---
type: assumption_note
case_key: case-20260406-6e955d27
dispatch_id: dispatch-case-20260406-6e955d27-20260408T153555Z
research_run_id: 56ff017e-c85f-48e7-942a-0e5b0fffb93f
analysis_date: 2026-04-08
persona: base-rate
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
importance: medium
time_horizon: point-in-time
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["assumption", "settlement-logic", "binance", "timezone"]
---

# Assumption

The operative candle is the Binance BTC/USDT 1-minute candle opening at 2026-04-06 16:00:00 UTC, because that timestamp corresponds to 12:00:00 ET on April 6, 2026.

## Why this assumption matters

The case is not about daily closing price or an approximate noon snapshot; it is about one exact minute candle under a timezone-specific rule. A one-minute mapping mistake would flip the relevant observation surface.

## What this assumption supports

- The conclusion that the correct candle close is 69938.59.
- The interpretation that the market should resolve Yes.
- The view that extra narrative research is low-value relative to exact contract-mechanics verification.

## Evidence or logic behind the assumption

- April 6, 2026 is during daylight saving time in New York, so ET equals UTC-4.
- Therefore 12:00 ET maps to 16:00 UTC.
- Binance klines are timestamped in Unix milliseconds and are conventionally keyed by candle open time.
- Querying Binance for startTime 1775491200000 yielded the candle with closeTime 1775491259999, matching the 16:00:00-16:00:59.999 UTC minute.

## What would falsify it

- Clear exchange documentation or market guidance stating that the 12:00 ET candle should instead mean the minute ending at 12:00 ET rather than the minute starting at 12:00 ET.
- Evidence that Polymarket interprets these Binance 1m markets using a different timestamp convention than Binance's standard kline open-time indexing.

## Early warning signs

- Any dispute post noting that noon ET refers to the prior minute's close.
- A mismatch between Binance UI candle label behavior and API open-time semantics.

## What changes if this assumption fails

The correct minute would need to be re-queried and the settlement direction could in principle change, though given BTC was far above 66,000 around the observed minute the practical resolution risk here still appears low.

## Notes that depend on this assumption

- The main agent finding for this run.
- The Binance/Polymarket source note.
- The evidence map for this run.