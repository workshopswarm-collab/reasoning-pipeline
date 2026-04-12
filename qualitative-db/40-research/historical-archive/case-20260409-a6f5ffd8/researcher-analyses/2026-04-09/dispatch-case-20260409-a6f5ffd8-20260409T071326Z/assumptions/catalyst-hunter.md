---
type: assumption_note
case_key: case-20260409-a6f5ffd8
dispatch_id: dispatch-case-20260409-a6f5ffd8-20260409T071326Z
research_run_id: f3d1073c-9c72-462b-af9d-0deff0b6e8c4
analysis_date: 2026-04-09
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-9
question: "Will the price of Bitcoin be above $70,000 on April 9?"
driver: operational-risk
date_created: 2026-04-09
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: intraday
related_entities: ["bitcoin"]
related_drivers: ["operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260409-a6f5ffd8/researcher-analyses/2026-04-09/dispatch-case-20260409-a6f5ffd8-20260409T071326Z/personas/catalyst-hunter.md"]
tags: ["assumption", "timestamp", "binance", "settlement"]
---

# Assumption

The contract-relevant candle is the Binance BTC/USDT 1-minute candle that opens at 16:00:00 UTC, because that is 12:00:00 ET on 2026-04-09.

## Why this assumption matters

If the relevant candle were misread as 12:00 UTC or as the minute ending at 12:00 ET rather than the minute labeled 12:00 ET, the settlement interpretation could flip from straightforward price monitoring to an avoidable operational error.

## What this assumption supports

- The conclusion that the governing catalyst is simply whether BTC stays above 70,000 into the exact 16:00:00-16:00:59 UTC settlement minute.
- The conclusion that timestamp verification, not macro news flow, is the main non-price risk.

## Evidence or logic behind the assumption

Polymarket rules explicitly say 12:00 in ET timezone. On 2026-04-09, New York is on EDT (UTC-4), so 12:00 ET maps to 16:00 UTC. Binance kline timestamps are UTC-based and represent the candle open time.

## What would falsify it

- Clear Binance documentation or contract adjudication showing that the displayed website candle label uses a different timezone basis for settlement.
- A Polymarket clarification saying the market uses the minute ending at noon ET rather than the minute beginning at noon ET.

## Early warning signs

- Conflicting public interpretations of which Binance candle counts.
- Exchange UI labels that appear inconsistent with API timestamps.
- Any moderator clarification or market comment indicating prior trader confusion on the exact minute.

## What changes if this assumption fails

The current estimate would need a fresh operational review and confidence would drop materially, because the thesis here depends on precise timestamp alignment more than on broad price direction.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260409-a6f5ffd8/researcher-analyses/2026-04-09/dispatch-case-20260409-a6f5ffd8-20260409T071326Z/personas/catalyst-hunter.md