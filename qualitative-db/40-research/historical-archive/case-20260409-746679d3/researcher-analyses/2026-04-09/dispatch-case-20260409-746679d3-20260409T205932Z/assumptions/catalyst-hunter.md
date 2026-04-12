---
type: assumption_note
case_key: case-20260409-746679d3
dispatch_id: dispatch-case-20260409-746679d3-20260409T205932Z
research_run_id: 4e9f9b53-3707-46ac-8a6f-415fdbd92afb
analysis_date: 2026-04-09
persona: catalyst-hunter
domain: crypto
subdomain: short-horizon-price-resolution
entity: ethereum
topic: ethereum-above-2100-on-april-10
question: "Will the price of Ethereum be above $2,100 on April 10?"
driver: reliability
date_created: 2026-04-09
agent: catalyst-hunter
status: active
certainty: medium
importance: high
time_horizon: "<24h"
related_entities: ["ethereum"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: ["binance-global"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["catalyst-hunter.md", "catalyst-hunter.sidecar.json"]
tags: ["assumption", "timezone", "contract-interpretation", "catalyst-timing"]
---

# Assumption

The decisive candle is the Binance ETH/USDT 1-minute candle opened at 12:00:00 ET on Apr 10, 2026, equivalent to 16:00:00 UTC under Eastern Daylight Time, and its final close price is the resolution print.

## Why this assumption matters

The market is highly likely to resolve Yes or No on a very small margin around a single minute print, so a timezone or candle-definition error would be more important than most macro or narrative analysis.

## What this assumption supports

- Using current ETH spot level versus 2100 as the main baseline.
- Treating the catalyst set as any event capable of moving ETH before or into the noon ET minute.
- Viewing contract interpretation risk as manageable rather than dominant.

## Evidence or logic behind the assumption

- Polymarket's market rules explicitly name the Binance ETH/USDT 12:00 ET 1-minute candle and its final close.
- Binance API docs say klines are uniquely identified by open time.
- Apr 10, 2026 is in daylight-saving time for New York, so noon ET maps to 16:00 UTC.
- Live Binance server time endpoint provides a direct UTC-aligned verification surface.

## What would falsify it

- A Binance or Polymarket clarification showing they instead use a different timezone conversion, UI-specific candle labeling rule, or a candle ending at 12:00 rather than opening at 12:00.
- Evidence that Polymarket has historically interpreted these Binance noon markets differently from the plain reading of the rules.

## Early warning signs

- Contradictory moderator guidance or official comments on the event.
- Binance UI showing noon ET labels in a way inconsistent with the API open-time convention.
- Any daylight-saving ambiguity in the displayed chart selection workflow.

## What changes if this assumption fails

Confidence in a simple spot-above-threshold framing would fall sharply, and contract-interpretation risk would need heavier weight than price-level analysis.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260409-746679d3/researcher-source-notes/2026-04-09-catalyst-hunter-binance-rules-and-api.md
- qualitative-db/40-research/cases/case-20260409-746679d3/researcher-analyses/2026-04-09/dispatch-case-20260409-746679d3-20260409T205932Z/personas/catalyst-hunter.md
